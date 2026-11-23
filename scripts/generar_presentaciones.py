#!/usr/bin/env python3
"""Generador incremental de presentaciones HTML y PPTX a partir de los temas Markdown.

Uso: python scripts/generar_presentaciones.py
Lee los temas existentes, detecta cambios por SHA-256 y actualiza solo los afectados.
No requiere servicios de IA externos ni GitHub Pages.
"""
from __future__ import annotations
import hashlib
import html
import json
import re
from datetime import datetime
from pathlib import Path
from io import BytesIO
from zoneinfo import ZoneInfo

import markdown
import cairosvg
from bs4 import BeautifulSoup, Tag, Comment
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches, Pt

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_SHA = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
VERSION_RE = re.compile(r"(\*\*Versión del contenido:\*\*\s*)(\d+\.\d+\.\d+)")
DATE_RE = re.compile(r"(\*\*Última actualización:\*\*\s*)(\d\d/\d\d/\d{4})")
PPTX_NAME = "tema-{number:02d}-{slug}.pptx"
COLORS = dict(navy=RGBColor(17, 42, 65), teal=RGBColor(7, 126, 144),
              paper=RGBColor(246, 250, 252), white=RGBColor(255, 255, 255),
              muted=RGBColor(74, 100, 120), line=RGBColor(217, 230, 238))
MAX_ITEMS = 4
MAX_TABLE_ROWS = 7


EXCLUDE_OPEN = "<!-- PRESENTACION:EXCLUIR -->"
EXCLUDE_CLOSE = "<!-- PRESENTACION:FIN_EXCLUSION -->"


def remove_excluded_blocks(text: str) -> str:
    """Elimina bloques optativos antes de calcular huellas y generar diapositivas."""
    if text.count(EXCLUDE_OPEN) != text.count(EXCLUDE_CLOSE):
        raise ValueError("Bloque PRESENTACION sin pareja de marcas EXCLUIR/FIN_EXCLUSION")
    pattern = re.compile(re.escape(EXCLUDE_OPEN) + r".*?" + re.escape(EXCLUDE_CLOSE), re.DOTALL)
    filtered = pattern.sub("", text)
    if EXCLUDE_OPEN in filtered or EXCLUDE_CLOSE in filtered:
        raise ValueError("Marcas PRESENTACION inválidas o anidadas")
    return filtered


def source_content(text: str) -> str:
    """Contenido que realmente aparece en diapositivas, sin bloques excluidos."""
    text = remove_excluded_blocks(text)
    if "## Objetivos de aprendizaje" in text:
        text = "## Objetivos de aprendizaje" + text.split("## Objetivos de aprendizaje", 1)[1]
    text = text.split("## Control de versiones", 1)[0].split("\n---\n\n> **Nota docente:**", 1)[0]
    # Las actividades son independientes y NO entran en presentaciones ni en su huella.
    text = re.sub(r"(?ms)^##\\s+\\d+\\.\\s+Actividades propuestas\\s*\\n.*?(?=^##\\s+\\d+\\.\\s+|\\Z)", "", text)
    return text.strip()


IMAGE_MARK_RE = re.compile(
    r"^IMAGEN:\s*(img/[a-zA-Z0-9_.-]+\.(?:png|jpg|jpeg|webp|svg))"
    r"(?:\s*\|\s*TITULO:\s*([^|]+?))?"
    r"(?:\s*\|\s*POSICION:\s*(ANTES|DESPUES))?\s*$", re.IGNORECASE,
)


def presentation_digest(text: str, folder: Path) -> str:
    """Incluye solamente los recursos de imagen enlazados en la fuente visible."""
    h = hashlib.sha256(text.encode("utf-8"))
    for marker in re.findall(r"<!--\s*(IMAGEN:.*?)\s*-->", text, re.DOTALL):
        match = IMAGE_MARK_RE.fullmatch(marker.strip())
        if not match:
            raise ValueError(f"Marca IMAGEN inválida: {marker[:120]}")
        relative = match.group(1)
        picture = folder / relative
        if not picture.is_file():
            raise FileNotFoundError(f"Falta imagen: {picture}")
        h.update(relative.encode("utf-8"))
        h.update(hashlib.sha256(picture.read_bytes()).digest())
    return h.hexdigest()


def clean(text: str) -> str:
    return " ".join(text.split()).strip()


def parse_slides(text: str, number: int, title: str) -> list[dict]:
    """Transforma todos los apartados del contenido en diapositivas de tamaño legible."""
    soup = BeautifulSoup(markdown.markdown(text, extensions=["tables", "fenced_code"]), "html.parser")
    slides = [{"title": f"Tema {number}. {title}", "subtitle": "Entornos de Desarrollo · 1.º DAW",
               "kind": "cover", "items": ["Contenidos, ejemplos y actividades del tema"]}]
    heading = title
    items: list[str] = []
    def flush() -> None:
        nonlocal items
        while items:
            chunk, items = items[:MAX_ITEMS], items[MAX_ITEMS:]
            slides.append({"title": heading, "items": chunk, "kind": "text"})

    def add_item(value: str) -> None:
        value = clean(value)
        if not value:
            return
        if len(value) > 235:
            pieces = re.split(r"(?<=[.!?])\s+", value)
            buf = ""
            for piece in pieces:
                if len(buf) + len(piece) > 185 and buf:
                    items.append(buf)
                    buf = piece
                else:
                    buf = (buf + " " + piece).strip()
            if buf:
                items.append(buf)
        else:
            items.append(value)

    for element in soup.children:
        if isinstance(element, Comment):
            comment = str(element).strip()
            if comment.startswith("IMAGEN:"):
                match = IMAGE_MARK_RE.fullmatch(comment)
                if not match:
                    raise ValueError(f"Marca IMAGEN inválida: {comment[:120]}")
                rel, label, placement = match.group(1), match.group(2), match.group(3)
                picture = {"title": clean(label or heading), "kind": "image", "image": rel}
                # Una marca se coloca en el punto exacto del texto al que pertenece.
                # ANTES la sitúa antes del texto pendiente; DESPUES cierra primero ese texto.
                if (placement or "DESPUES").upper() == "DESPUES":
                    flush()
                slides.append(picture)
            continue
        if not isinstance(element, Tag):
            continue
        if element.name in ("h2", "h3", "h4"):
            flush()
            heading = clean(element.get_text(" ", strip=True))
        elif element.name in ("p", "blockquote"):
            add_item(element.get_text(" ", strip=True))
        elif element.name in ("ul", "ol"):
            for li in element.find_all("li", recursive=False):
                add_item(li.get_text(" ", strip=True))
        elif element.name == "table":
            flush()
            heads = [clean(x.get_text(" ", strip=True)) for x in element.select("thead th")]
            rows = [[clean(c.get_text(" ", strip=True)) for c in tr.find_all(["td", "th"], recursive=False)]
                    for tr in element.select("tbody tr")]
            if not heads and rows:
                heads, rows = rows[0], rows[1:]
            if heads and rows:
                for start in range(0, len(rows), MAX_TABLE_ROWS):
                    slides.append({"title": heading, "kind": "table", "heads": heads,
                                   "rows": rows[start:start + MAX_TABLE_ROWS]})
    flush()
    # La primera diapositiva real no debe repetir un título vacío.
    return slides


def pptx_text(slide, value, x, y, w, h, sz=18, bold=False, color=None):
    sh = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = sh.text_frame
    tf.clear()
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = Inches(0.03)
    tf.margin_top = Inches(0.04)
    para = tf.paragraphs[0]
    para.text = value
    para.font.name = "Aptos"
    para.font.size = Pt(sz)
    para.font.bold = bold
    para.font.color.rgb = color or COLORS["navy"]
    return sh


def pptx_box(slide, x, y, w, h, color, radius=True):
    kind = MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE
    shape = slide.shapes.add_shape(kind, Inches(x), Inches(y), Inches(w), Inches(h))
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    return shape


def write_pptx(path: Path, slides: list[dict], version: str, date: str, digest: str):
    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
    prs.core_properties.title = slides[0]["title"]
    prs.core_properties.subject = f"Versión {version} · Fuente {digest[:12]}"
    prs.core_properties.keywords = f"Entornos de Desarrollo 1 DAW; {version}; {date}; {digest}"
    for index, data in enumerate(slides, 1):
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        is_cover = data["kind"] == "cover"
        pptx_box(slide, 0, 0, 13.333, 7.5, COLORS["navy"] if is_cover else COLORS["paper"], False)
        pptx_box(slide, .26, .3, .09, 6.8, COLORS["teal"], False)
        fg = COLORS["white"] if is_cover else COLORS["navy"]
        pptx_text(slide, "ENTORNOS DE DESARROLLO  ·  1.º DAW", .75, .38, 9.2, .35, 12, True,
                  COLORS["white"] if is_cover else COLORS["teal"])
        heading = data["title"]
        pptx_text(slide, heading, .75, 1.12 if is_cover else .93, 11.7, 1.05, 36 if is_cover else 29, True, fg)
        if is_cover:
            pptx_text(slide, "Del problema al programa: herramientas y ejecución", .75, 2.55, 11.5, .75, 21,
                      color=COLORS["white"])
            pptx_text(slide, "Material didáctico · fuente: tema en Markdown", .75, 5.55, 11.4, .5, 17,
                      color=COLORS["white"])
        elif data["kind"] == "image":
            image_path = path.parent.parent / data["image"]
            if image_path.suffix.lower() == ".svg":
                raster = BytesIO(cairosvg.svg2png(url=str(image_path), output_width=2400))
                picture = slide.shapes.add_picture(raster, Inches(0), Inches(0))
            else:
                picture = slide.shapes.add_picture(str(image_path), Inches(0), Inches(0))
            max_w, max_h = Inches(11.35), Inches(4.7)
            ratio = min(max_w / picture.width, max_h / picture.height)
            picture.width = int(picture.width * ratio)
            picture.height = int(picture.height * ratio)
            picture.left = int((prs.slide_width - picture.width) / 2)
            picture.top = Inches(2.0) + int((max_h - picture.height) / 2)
        elif data["kind"] == "table":
            heads, rows = data["heads"], data["rows"]
            cols = len(heads)
            if cols > 0:
                table_shape = slide.shapes.add_table(len(rows) + 1, cols,
                                                       Inches(.75), Inches(2.2),
                                                       Inches(11.8), Inches(4.35))
                table = table_shape.table
                for r, vals in enumerate([heads] + rows):
                    for c in range(cols):
                        cell = table.cell(r, c)
                        cell.text = vals[c] if c < len(vals) else ""
                        cell.fill.solid()
                        cell.fill.fore_color.rgb = COLORS["teal"] if r == 0 else (
                            COLORS["white"] if r % 2 else COLORS["paper"])
                        for para in cell.text_frame.paragraphs:
                            para.font.name = "Aptos"
                            para.font.size = Pt(11 if cols >= 4 else 13)
                            para.font.bold = r == 0
                            para.font.color.rgb = COLORS["white"] if r == 0 else COLORS["navy"]
        else:
            n = min(4, len(data["items"]))
            for j, item in enumerate(data["items"]):
                y = 2.05 + j * (4.68 / max(n, 1))
                height = 4.68 / max(n, 1) - .14
                pptx_box(slide, .78, y, 11.74, height, COLORS["white"])
                # El tamaño depende de la longitud del texto para evitar desbordamientos.
                size = 20 if len(item) < 115 else 17 if len(item) < 205 else 15
                pptx_text(slide, "•  " + item, 1.05, y + .12, 11.15, height - .18, size, color=COLORS["navy"])
        pptx_text(slide, f"v{version} · {date}", .78, 7.13, 6.1, .23, 10, color=COLORS["white"] if is_cover else COLORS["muted"])
        pptx_text(slide, f"{index:02d} / {len(slides):02d}", 11.67, 7.13, 1.2, .23, 10,
                  color=COLORS["white"] if is_cover else COLORS["muted"])
    prs.save(path)


CSS = """
*{box-sizing:border-box}body{margin:0;font-family:system-ui,-apple-system,'Segoe UI',sans-serif;background:#e8f1f5;color:#1b344a}
.shell{max-width:1300px;margin:auto;padding:14px}.top{display:flex;justify-content:space-between;gap:14px;align-items:center;padding:8px 6px 16px;color:#0b6477;font-weight:750;font-size:.9rem}
a{color:#0c7183}.stage{box-shadow:0 18px 45px #123c5233;border-radius:18px;overflow:hidden}.slide{padding:clamp(1.1rem,4vw,3.1rem);min-height:min(74vh,690px);background:linear-gradient(126deg,#fff,#edf7fa);position:relative}
.slide[hidden]{display:none}.slide.cover{background:linear-gradient(130deg,#102c49,#0b677e);color:white;display:flex;flex-direction:column;justify-content:center}
.slide.cover[hidden]{display:none}.tag{font-size:.83rem;color:#0b8190;font-weight:800;letter-spacing:.15em;text-transform:uppercase;margin:0 0 14px}.cover .tag{color:#a9f4ef}
h1{font-size:clamp(2.1rem,5vw,4rem);line-height:1.1;letter-spacing:-.035em;max-width:1050px}h2{font-size:clamp(1.45rem,3.7vw,2.65rem);margin:.2rem 0 1.5rem;line-height:1.15;color:#12314b}
.cards{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}.card{background:#fff;border:1px solid #d8e7ed;border-radius:15px;padding:clamp(1rem,2vw,1.6rem);min-height:130px;font-size:clamp(1rem,1.35vw,1.19rem);line-height:1.5;overflow-wrap:anywhere}
.card::first-letter{color:#0c8397}.image-frame{display:flex;align-items:center;justify-content:center;min-height:46vh}.image-frame img{display:block;max-width:100%;max-height:58vh;width:auto;height:auto;object-fit:contain;border-radius:12px}.table-wrap{max-width:100%;overflow-x:auto;background:white;border-radius:14px}
table{width:100%;border-collapse:collapse;min-width:560px}th,td{padding:12px 15px;border-bottom:1px solid #dde9ee;text-align:left;vertical-align:top;font-size:clamp(.88rem,1.2vw,1.1rem)}
th{background:#0b7e93;color:white}tr:nth-child(odd) td{background:#f3f8fb}
.controls{background:white;display:flex;gap:9px;flex-wrap:wrap;padding:15px;align-items:center}.controls button,.controls select{border:1px solid #bfd4df;background:#eff6f9;border-radius:9px;padding:10px 13px;font-weight:700;color:#153d57;font:inherit}
.controls button{cursor:pointer}.controls button:disabled{opacity:.3;cursor:default}#next{background:#143b58;color:white}
.controls select{flex:1 1 230px;min-width:100px}#count{font-size:.86rem;color:#607a89;white-space:nowrap}
.meter{height:5px;background:#d7e8ef}.meter div{background:#0a8999;height:100%;width:0;transition:width .2s}
.foot{margin-top:2rem;font-size:.82rem;color:#5b7a8b}.cover .foot{color:#c6e8ee}
.hint{text-align:center;color:#507184;font-size:.8rem}.cover .subtitle{font-size:1.5rem;color:#d1edf3}
@media(max-width:750px){.cards{grid-template-columns:1fr}.slide{min-height:70vh}.top{font-size:.76rem}.card{min-height:auto}.controls button{padding:8px}}
@media print{@page{size:landscape;margin:0}.shell{padding:0}.top,.controls,.meter,.hint{display:none}.stage{box-shadow:none}.slide,.slide[hidden],.slide.cover[hidden]{display:block!important;page-break-after:always;min-height:100vh}.slide:last-child{page-break-after:auto}}
"""


def write_html(path: Path, slides: list[dict], version: str, date: str, digest: str):
    date_iso = datetime.strptime(date, "%d/%m/%Y").date().isoformat()
    sections = []
    for index, slide in enumerate(slides):
        title = html.escape(slide["title"])
        extra = " cover" if slide["kind"] == "cover" else ""
        inner = f'<p class="tag">Entornos de Desarrollo · Tema {index + 1:02d}</p>'
        inner += f'<h1>{title}</h1>' if index == 0 else f'<h2>{title}</h2>'
        if slide["kind"] == "cover":
            inner += '<p class="subtitle">Comprende cómo se crea, prueba y ejecuta software</p>'
        elif slide["kind"] == "image":
            src = "../" + slide["image"]
            inner += f'<div class="image-frame"><img src="{html.escape(src, quote=True)}" alt="{title}"></div>'
        elif slide["kind"] == "table":
            heads = "".join(f"<th>{html.escape(v)}</th>" for v in slide["heads"])
            rows = "".join("<tr>" + "".join(f"<td>{html.escape(x)}</td>" for x in row) + "</tr>"
                           for row in slide["rows"])
            inner += f'<div class="table-wrap"><table><thead><tr>{heads}</tr></thead><tbody>{rows}</tbody></table></div>'
        else:
            inner += '<div class="cards">' + "".join(f'<div class="card">{html.escape(item)}</div>'
                                                      for item in slide["items"]) + "</div>"
        inner += f'<p class="foot">Tema: v{html.escape(version)} · {html.escape(date)}</p>'
        sections.append(f'<section class="slide{extra}" data-title="{html.escape(slide["title"], quote=True)}"'
                        + (' hidden' if index else '') + f' aria-label="Diapositiva {index + 1}">{inner}</section>')
    page = f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="content-version" content="{version}"><meta name="updated-date" content="{date_iso}">
<meta name="source-sha256" content="{digest}"><meta name="generator-sha256" content="{SCRIPT_SHA}">
<title>{html.escape(slides[0]["title"])} · Presentación HTML</title><style>{CSS}</style></head>
<body><div class="shell"><header class="top"><span>Entornos de Desarrollo · 1.º DAW · v{version}</span><a target="_blank" rel="noopener noreferrer" href="../tema-01.md" id="source">Consultar apuntes ↗</a></header>
<main class="stage" id="stage" aria-label="Presentación del tema">{''.join(sections)}</main>
<div class="meter"><div id="progress"></div></div>
<nav class="controls" aria-label="Control de diapositivas"><button id="prev" type="button">← Anterior</button>
<button id="next" type="button">Siguiente →</button><select id="jump" aria-label="Seleccionar diapositiva"></select>
<span id="count" aria-live="polite"></span><button id="fullscreen" type="button">⛶ Pantalla completa</button><button id="print" type="button">Imprimir</button></nav>
<p class="hint">Navega con ← y →. Puedes imprimir o utilizar pantalla completa.</p></div>
<script>
(()=>{{const slides=[...document.querySelectorAll('.slide')],jump=document.getElementById('jump');
slides.forEach((s,i)=>{{const opt=document.createElement('option');opt.value=String(i);
opt.textContent=(i+1)+' · '+s.dataset.title;jump.appendChild(opt);}});
let n=0;function show(i){{n=Math.max(0,Math.min(i,slides.length-1));slides.forEach((s,k)=>s.hidden=k!==n);
document.getElementById('prev').disabled=n===0;document.getElementById('next').disabled=n===slides.length-1;
document.getElementById('count').textContent=(n+1)+' / '+slides.length;
document.getElementById('progress').style.width=((n+1)*100/slides.length)+'%';jump.value=String(n);}}
document.getElementById('prev').onclick=()=>show(n-1);
document.getElementById('next').onclick=()=>show(n+1);
jump.onchange=()=>show(Number(jump.value));
document.addEventListener('keydown',e=>{{if(['INPUT','SELECT','TEXTAREA'].includes(e.target.tagName))return;
if(['ArrowRight','PageDown'].includes(e.key)){{e.preventDefault();show(n+1);}}
if(['ArrowLeft','PageUp'].includes(e.key)){{e.preventDefault();show(n-1);}}
if(e.key==='Home')show(0);if(e.key==='End')show(slides.length-1);}});
let touch=null;document.getElementById('stage').addEventListener('touchstart',e=>touch=e.touches[0].clientX,{{passive:true}});
document.getElementById('stage').addEventListener('touchend',e=>{{if(touch===null)return;const delta=e.changedTouches[0].clientX-touch;if(Math.abs(delta)>65)show(n+(delta<0?1:-1));touch=null;}},{{passive:true}});
document.getElementById('fullscreen').onclick=()=>{{if(document.fullscreenElement)document.exitFullscreen();else document.documentElement.requestFullscreen?.();}};
document.getElementById('print').onclick=()=>window.print();
show(0);
}})();
</script></body></html>"""
    # Enlaces de retorno: relativo desde carpeta "presentaciones" a tema-NN.md.
    num = re.search(r"Tema (\d+)", slides[0]["title"])
    if num:
        page = page.replace('href="../tema-01.md"', f'href="../tema-{int(num.group(1)):02d}.md"')
    path.write_text(page, encoding="utf-8")


def main() -> None:
    status = []
    now = datetime.now(ZoneInfo("Europe/Madrid")).strftime("%d/%m/%Y")
    for source in sorted(ROOT.glob("temas/tema-*/tema-*.md")):
        folder = source.parent
        present = folder / "presentaciones"
        present.mkdir(exist_ok=True)
        manifest_path = present / "manifest.json"
        old = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
        markdown_text = source.read_text(encoding="utf-8")
        content = source_content(markdown_text)
        digest = presentation_digest(content, folder)
        match = re.search(r"tema-(\d+)-(.+)", folder.name)
        if not match:
            continue
        num, slug = int(match.group(1)), match.group(2)
        v_match, date_match = VERSION_RE.search(markdown_text), DATE_RE.search(markdown_text)
        version = v_match.group(2) if v_match else "1.0.0"
        date = date_match.group(2) if date_match else now
        content_changed = bool(old) and old.get("source_sha256") != digest
        if content_changed and old.get("content_version") == version:
            major, minor, patch = [int(x) for x in version.split(".")]
            version = f"{major}.{minor}.{patch + 1}"
            if v_match:
                markdown_text = VERSION_RE.sub(lambda m: m.group(1) + version, markdown_text, count=1)
            date = now
            if date_match:
                markdown_text = DATE_RE.sub(lambda m: m.group(1) + date, markdown_text, count=1)
            source.write_text(markdown_text, encoding="utf-8")
        elif not v_match or not date_match:
            footer = f"\n\n---\n\n## Control de versiones\n\n- **Versión del contenido:** {version}\n- **Última actualización:** {date}\n- **Estado:** Borrador ampliable\n"
            source.write_text(markdown_text.rstrip() + footer, encoding="utf-8")
        html_path = present / f"tema-{num:02d}.html"
        pptx_path = present / PPTX_NAME.format(number=num, slug=slug)
        signature = dict(source_sha256=digest, content_version=version,
                         updated_date=date, generator_sha256=SCRIPT_SHA)
        skip = (old.get("source_sha256") == digest and old.get("generator_sha256") == SCRIPT_SHA
                and html_path.exists() and pptx_path.exists())
        if skip:
            status.append(f"OMITIDO tema {num:02d}: sin cambios didácticos")
            continue
        name = source.read_text(encoding="utf-8").splitlines()[0].removeprefix("# Tema ").split(". ", 1)[-1]
        slides = parse_slides(content, num, name)
        write_html(html_path, slides, version, date, digest)
        write_pptx(pptx_path, slides, version, date, digest)
        manifest_path.write_text(json.dumps({**signature, "slides": len(slides),
                                             "html": html_path.name, "pptx": pptx_path.name},
                                            ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        status.append(f"ACTUALIZADO tema {num:02d}: {len(slides)} diapositivas, versión {version}")
    print("\n".join(status) if status else "No se encontraron archivos de temas")


if __name__ == "__main__":
    main()
