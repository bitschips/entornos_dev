# AGENTS.md — Procedimientos de Entornos de Desarrollo · 1.º DAW

> **Versión:** 1.2.0  
> **Fecha:** 23/11/2026  
> **Repositorio:** bitschips/entornos_dev

Este documento adapta las decisiones operativas de bitschips/digitaliza4 a un curso **genérico de Entornos de Desarrollo de 1.º DAW**, independiente de una comunidad autónoma, institución o normativa concreta. LEER antes de cualquier edición. Los 10 temas y las referencias RA1–RA6 se utilizan como etiquetas de organización pedagógica, no como citas jurídicas.

## 1. Fuente única e índice

- El **Markdown** del tema es la fuente oficial: `temas/tema-NN-slug/tema-NN.md`.
- El archivo raíz **README.md** contiene un único índice por bloques, con **solo títulos y enlaces**. No duplicar allí el contenido interior.
- Los temas aún no desarrollados pueden enlazar a `REVISION-tema-NN.md`, **identificados visiblemente como pendientes**. Esto cumple la petición de enlazar desde el primer día a los 10 temas. No confundir ficha de planificación con tema desarrollado.
- Cada tema tiene carpetas `presentaciones/`, `actividades/`, `videos/`, `ampliaciones/` e `img/`; usar `.gitkeep` para carpetas vacías.
- No crear archivos PDF ni presentación general del índice salvo petición expresa.

## 2. Estados de edición

- **En preparación/revisión:** trabajar en `REVISION-tema-NN.md`. No dispara presentaciones. El profesor revisa y aprueba su paso a definitivo.
- **Tema aprobado:** copiar contenido revisado a `tema-NN.md` y actualizar el enlace del índice. Una modificación posterior del contenido teórico de este archivo **siempre sincroniza automáticamente HTML y PPTX**, incluso cuando se ordene por voz y no se pida expresamente «actualizar las diapositivas».
- **Excepción inicial autorizada:** el profesor ha pedido expresamente **crear presentaciones del tema 1 ahora**, por lo que el tema 1 se publica directamente como `tema-01.md`, con estado «versión inicial para revisión».

## 3. Formato del tema

1. Título, módulo/curso/RA, estado.
2. Enlace «Volver al índice general».
3. **Materiales del tema** al comienzo: SOLO enlaces a presentación HTML, PPTX y material externo realmente disponible (NotebookLM, etc.). Nunca actividades.
4. **Objetivos de aprendizaje**, desarrollo numerado con explicaciones, tablas, ejemplos verificables y esquemas.
5. Al final, un apartado «Actividades propuestas» con **un único enlace** a `actividades/README.md`, antes de preguntas de repaso y glosario.
6. Preguntas de repaso, glosario y **Control de versiones** con versión `MAJOR.MINOR.PATCH`, fecha DD/MM/AAAA, estado.
7. Las secciones opcionales no destinadas a diapositivas se delimitan con las marcas exactas `<!-- PRESENTACION:EXCLUIR -->` y `<!-- PRESENTACION:FIN_EXCLUSION -->`.

## 4. Actividades, vídeos y ampliaciones

- `actividades/README.md` es el índice, con enlaces a `actividad-NN-titulo.md`, cada uno con objetivo, RA/criterios, materiales, pasos, evidencias, evaluación y ampliación si corresponde.
- Las imágenes específicas de una actividad irán en **`actividades/img/`**, nunca en `img/` del tema.
- Agregar/editar actividades **no modifica `tema-NN.md` ni dispara presentaciones**. Una vez enlazado su índice desde el tema, añadir actividades solo actualiza `actividades/README.md` y archivos internos.
- `videos/README.md` contiene ideas de vídeos; cada `video-NN-titulo.md` es un guion con escenas, narración y comprobación técnica. **Una idea/guion NO es un vídeo generado**; no anunciar vídeos inexistentes.
- `ampliaciones/README.md` agrupa temas opcionales. Si se incorporan además al Markdown principal, delimitar el apartado con las marcas PRESENTACION:EXCLUIR salvo petición de incorporarlos a las diapositivas.
- Crear propuestas de vídeo o actividad por voz sin modificar ni regenerar el tema oficial, salvo que se solicite añadir teoría al material central.

## 5. Presentaciones y recursos visuales

- Guardar **dos formatos**: `presentaciones/tema-NN.html` y `presentaciones/tema-NN-slug.pptx`, ambos coherentes con el Markdown teórico, navegables/editables según su formato.
- HTML: navegación teclado y táctil, contador, pantalla completa, presentación adaptable y enlace al tema. PPTX: editable, diapositivas 16:9 con tablas y ejemplos.
- No activar GitHub Pages. Enlace HTML mediante `https://htmlpreview.github.io/?https://github.com/bitschips/entornos_dev/blob/main/RUTA/tema-NN.html`. Enlace PPTX relativo directo al archivo en el repositorio.
- Versiones y fecha dentro de las presentaciones, y metadatos/huella SHA-256 en `presentaciones/manifest.json`.
- Diapositivas exclusivamente **del contenido teórico**. No incluir enunciados completos, códigos de actividades ni guiones de vídeo.
- `img/`: imágenes semánticas creadas/seleccionadas para ilustrar la teoría. Para diapositiva de imagen independiente, usar en `tema-NN.md` `<!-- IMAGEN: img/nombre.svg | TITULO: Descripción | POSICION: DESPUES -->`. Admitir SVG y PNG/JPG/WebP, con recursos existentes y verificables; colocar la marca justo junto al concepto ilustrado.
- HTML propio: enlaces de navegación con `target="_blank" rel="noopener noreferrer"`. **GitHub Markdown no obliga pestaña nueva**: usar enlaces relativos estándar y Ctrl/Cmd+clic si se desea.
- Evitar imágenes externas no comprobadas y enlaces ficticios. No usar servicios externos de IA en la Action.

## 6. Automatización incremental obligatoria

- Workflow: `.github/workflows/actualizar-presentaciones.yml`.
- Generador: `scripts/generar_presentaciones.py` (`markdown`, `beautifulsoup4`, `python-pptx`, `cairosvg`).
- Un `push` en main que cambie `temas/**/tema-*.md`, imágenes teóricas en `temas/**/img/**`, el generador o el workflow ejecuta el generador. Ejecutable manualmente con workflow_dispatch.
- **Excluir expresamente `actividades/**`, `videos/**`, `ampliaciones/**` y `REVISION-tema-NN.md` de los disparadores**.
- El generador calcula una huella del contenido pedagógico visible + imágenes referenciadas, comprueba el manifiesto y regenera **solo los temas modificados**. Una actualización solo de enlaces o versión que no afecte a la docencia no debe regenerar.
- Cambios sustantivos: incrementar versión y fecha. Si se olvida incrementar la versión al cambiar teoría, el generador la subirá automáticamente un PATCH.
- Validar rutas, contenido generado, número de diapositivas, huellas, Action y commits. No afirmar que el workflow acabó si no se ha comprobado.
- No activar GitHub Pages y no publicar ni sobrescribir materiales de otros temas sin necesidad.

## 7. Enfoque didáctico y enseñanza

- Organizar actividades y contenidos alrededor de los objetivos de aprendizaje RA1–RA6 como **referencias pedagógicas internas**, sin citar normas jurídicas, autoridades territoriales ni duraciones impuestas por una administración. El curso debe poder reutilizarse en cualquier centro de FP.
- Desarrollo adaptado a alumnado de 1.º DAW: con profundidad técnica creciente, ejemplos en Python/Java/C cuando proceda, comandos reproducibles en Linux y Windows, conceptos exactos y criterios de evaluación.
- Las explicaciones de tecnologías y las URLs de herramientas se revisan al crear el contenido. No usar cifras de popularidad o licencias sin fuente.
- No introducir soluciones completas para todas las actividades en la diapositiva teórica. Preferir una idea principal y esquemas.
- Cuando se apruebe una regla nueva, actualizar este AGENTS.md y su versión.

## 8. Estado del proyecto (23/11/2026)

- Tema 1: teoría completa, actividades, guiones de vídeo e ideas de ampliación; generar HTML/PPTX y `manifest.json` con GitHub Actions.
- Tema 2: contenido aprobado y publicado como `tema-02.md`, con actividades, guiones de vídeo, ampliaciones, diagramas en `img/` y presentaciones HTML/PPTX autogeneradas.
- Temas 3–10: estructura de carpetas y planificación inicial, todavía sin teoría desarrollada ni presentaciones.

### Historial

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0.0 | 23/11/2026 | Adaptación de las normas de digitaliza4 para 1.º DAW / ED; índice completo, tema 1 y sincronización incremental. |
| 1.1.0 | 23/11/2026 | Curso genérico sin adscripción geográfica ni referencias jurídicas; actualizar estado de tema 2. |
| 1.2.0 | 23/11/2026 | Tema 2 aprobado; publicar su fuente definitiva, diagramas y presentaciones, actualizar enlaces y retirar la versión de revisión. |
