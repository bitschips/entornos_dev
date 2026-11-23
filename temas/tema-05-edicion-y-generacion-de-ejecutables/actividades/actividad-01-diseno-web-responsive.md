# Actividad 01. Auditoría y mejora de una página web responsive

**Módulo:** Entornos de Desarrollo · 1.º DAW  
**Tema relacionado:** Tema 5. Edición y gestión de proyectos (actividad práctica transversal de HTML y CSS).  
**Duración orientativa:** 2–3 sesiones de 55 minutos.  
**Modalidad:** individual o por parejas.  
**Nivel:** básico-intermedio.  
**Herramientas:** editor de código (KWrite, VS Code, Geany u otro), navegador, herramientas de desarrollador (F12) y dispositivo móvil opcional.

[Volver al índice de actividades](README.md) · [Volver a la ficha del tema 5](../REVISION-tema-05.md)

## 1. Situación y objetivo

Una empresa tiene un **panel web de proyectos** que funciona en un ordenador de sobremesa, pero en un teléfono aparece demasiado ancho, exige desplazamiento horizontal y muestra textos o botones difíciles de usar.

Tu trabajo consiste en **auditar, corregir y comprobar** esa página para que se adapte al espacio disponible en **móvil, tableta y escritorio**.

Al terminar, debes poder **explicar con ejemplos** para qué sirve cada técnica de diseño adaptable (*responsive web design*): no basta con pegar reglas CSS sin entender qué hacen.

## 2. ¿Qué hace que una página sea responsive?

Una página es responsive cuando su estructura, contenido, tipografía, imágenes y controles se adaptan a distintos tamaños de pantalla **sin perder información ni funcionalidad**. No depende de una única etiqueta ni de utilizar obligatoriamente `vw`: es el resultado de varias decisiones coordinadas.

Investiga, aplica y documenta las siguientes características.

| N.º | Característica | Ejemplo o técnica | Comprobación que debes realizar |
|---|---|---|---|
| 1 | **Documento HTML correcto** | `<!doctype html>`, `<html lang="es">`, `<head>`, `<body>` | Estructura y títulos semánticos reconocibles |
| 2 | **Viewport en el `head`** | `<meta name="viewport" content="width=device-width, initial-scale=1">` | El móvil usa el ancho disponible en píxeles CSS |
| 3 | **Anchura adaptable** | `width: 100%`, `max-width: 70rem`, `margin-inline: auto` | El contenedor se estrecha sin desbordar |
| 4 | **Modelo de cajas** | `box-sizing: border-box` | Relleno y bordes no provocan anchos inesperados |
| 5 | **Unidades relativas** | `%`, `vw`, `vh`, `rem`, `em`, `fr` | Justificas por qué eliges cada unidad |
| 6 | **Tipografía fluida pero legible** | `font-size: clamp(1.2rem, 1rem + 1.5vw, 2rem)` | Los títulos no son minúsculos ni gigantes |
| 7 | **Diseño flexible** | `display: flex`, `flex-wrap: wrap`, `gap` | Menús o grupos se reorganizan si falta espacio |
| 8 | **Cuadrícula adaptable** | `display: grid`, `grid-template-columns`, `minmax()`, `1fr` | Las tarjetas pasan de varias columnas a una |
| 9 | **Mobile first** | Reglas base para móvil; mejoras para pantallas amplias | Móvil funciona sin depender de una media query |
| 10 | **Media queries** | `@media (min-width: 48rem) { ... }` | El diseño cambia cuando el contenido lo necesita |
| 11 | **Imágenes adaptables** | `max-width: 100%`, `height: auto` | La imagen no se sale de su contenedor |
| 12 | **Imágenes según resolución** | `srcset`, `sizes`, `<picture>` (opcional) | Explicas cómo se puede evitar descargar imágenes innecesariamente grandes |
| 13 | **Elementos que desbordan** | `min-width: 0`, `overflow-wrap: anywhere`, `overflow-x: auto` para tablas | No aparece desplazamiento horizontal global |
| 14 | **Controles accesibles** | Etiquetas, `alt`, foco visible, enlaces y botones manejables | Se puede navegar con teclado y pulsar en móvil |
| 15 | **Pruebas reales** | Inspector responsive, zoom y móvil físico si se dispone | Presentas evidencias en distintos anchos |

**Atención a las unidades:**

| Unidad | Significado | Uso recomendado / precaución |
|---|---|---|
| `px` | Píxel CSS | Bordes, detalles y mínimos concretos; no es un píxel físico obligatorio |
| `%` | Porcentaje de una referencia según la propiedad | Anchos y elementos dentro de contenedores |
| `vw` | 1 % del **ancho del viewport** | Espaciado y escalado fluido; `100vw` puede provocar desbordamiento por la barra de desplazamiento |
| `vh` | 1 % de la altura del viewport en su modelo habitual | Secciones verticales; en móviles las barras del navegador pueden cambiar el área visible |
| `dvh` | 1 % de la altura dinámica del viewport | Aplicaciones que necesitan ajustarse a la altura visible móvil |
| `rem` | Relativo al tamaño de letra del elemento raíz | Tipografía, separaciones y límites coherentes |
| `em` | Relativo al tamaño de letra según la propiedad y el contexto | Medidas que escalan con componentes |
| `fr` | Fracción del espacio disponible en CSS Grid | Reparto flexible de columnas |

**Ejemplo para razonar:** `font-size: 5vw` sería aproximadamente **16 px** en un viewport de **320 px**, pero **72 px** en uno de **1440 px**. Por eso no es una buena regla universal para texto normal sin límites: conviene usar `clamp()` o unidades de tipografía apropiadas.

## 3. Archivos de partida

Descarga la [plantilla HTML deliberadamente no responsive](plantilla-no-responsive.html) y el [banner SVG local](img/banner-proyectos.svg). Mantén su estructura de carpetas:

```text
actividad-responsive/
├── index.html                 # Copia y renombra la plantilla
├── styles.css                 # Crea este archivo y mueve aquí el CSS
└── img/
    └── banner-proyectos.svg
```

La plantilla contiene fallos **intencionados**: ancho fijo, menú sin adaptación, imagen rígida, tarjetas que desbordan, tipografía desproporcionada y ausencia de `meta viewport`.

**No borres las secciones del contenido para conseguir que quepa.** Tu misión es mejorar el diseño conservando la información.

## 4. Fase A. Diagnóstico inicial (25 min)

1. Abre la plantilla en un navegador de escritorio y activa **Herramientas de desarrollador → modo dispositivo**.
2. Comprueba anchos de viewport de **320, 375, 768, 1024 y 1440 píxeles CSS**.
3. Identifica **al menos seis problemas**. Anota su causa: ¿falta viewport, hay un ancho fijo, la imagen excede el contenedor, el menú no se ajusta, etc.?
4. Guarda **dos capturas** del diseño inicial: una estrecha y otra ancha.
5. Rellena la primera mitad de esta tabla:

| Problema observado | Elemento / propiedad responsable | Corrección propuesta | Verificación posterior |
|---|---|---|---|
| La página se desplaza horizontalmente | `width: 960px` | Cambiar a anchura fluida limitada con `max-width` | Repetir prueba a 320 px |
| ... | ... | ... | ... |

## 5. Fase B. Corrección paso a paso (60–90 min)

### B1. Documento y viewport

- Añade `lang="es"` al elemento raíz, título significativo y la etiqueta viewport en el **`<head>`**.
- Mantén `<meta charset="utf-8">` y conecta un archivo CSS externo `styles.css`.
- **No uses** `user-scalable=no` ni limites el zoom: el usuario debe poder ampliar el contenido.

```html
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Panel de proyectos</title>
  <link rel="stylesheet" href="styles.css">
</head>
```

### B2. Contenedor fluido y modelo de cajas

Sustituye el ancho fijo por uno adaptable con límite máximo. Por ejemplo:

```css
*, *::before, *::after { box-sizing: border-box; }

.contenedor {
  width: min(100% - 2rem, 72rem);
  margin-inline: auto;
}
```

Explica por qué `max-width` o `min()` es preferible a fijar el ancho principal a `960px`.

### B3. Flexbox y Grid

- Convierte el menú en un diseño que no desborde: Flexbox con `flex-wrap` o un menú vertical móvil.
- Organiza las tarjetas con CSS Grid o Flexbox. Deben mostrarse en **una columna cuando la pantalla sea estrecha**, y varias cuando haya suficiente espacio.
- Utiliza `gap` para la separación; evita colocar columnas con desplazamientos rígidos.
- Aplica **mobile first**: define primero la versión pequeña y después una media query para pantallas anchas.

```css
.tarjetas { display: grid; grid-template-columns: 1fr; gap: 1rem; }

@media (min-width: 48rem) {
  .tarjetas { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
```

**Reto adicional:** sustituye el breakpoint anterior por `repeat(auto-fit, minmax(min(100%, 17rem), 1fr))` y explica en qué situaciones Grid puede adaptarse sin media queries.

### B4. Tipografía, imágenes y texto

- Reemplaza la tipografía `5vw` de los párrafos por una medida legible, justificada y estable.
- Utiliza `rem` para espacios y prueba `clamp()` al menos en un título.
- Haz el banner adaptable con `max-width: 100%; height: auto;`.
- Conserva una descripción alternativa `alt` adecuada para la imagen.
- Evita que cadenas de texto largas desborden sus tarjetas usando una estrategia apropiada: `overflow-wrap: anywhere` o límites de contenido; comprueba también `min-width: 0` si los elementos flex/grid lo necesitan.

### B5. Calidad y accesibilidad

Comprueba que **no desaparece ningún contenido**, que el texto se lee sin zoom obligatorio, que la navegación por **Tab** alcanza los controles y que el foco es visible. Mantén contraste suficiente; no dependas exclusivamente del color para transmitir el estado de un proyecto.

**No se exige JavaScript**. Esta actividad se centra en HTML y CSS.

## 6. Fase C. Pruebas y evidencias (30 min)

Repite la prueba en cinco tamaños y completa la matriz:

| Viewport (px CSS) | Columnas observadas | ¿Desplazamiento horizontal global? | ¿Se lee y utiliza bien? | Captura |
|---:|---:|---|---|---|
| 320 | | Sí / No | Sí / No | |
| 375 | | Sí / No | Sí / No | |
| 768 | | Sí / No | Sí / No | |
| 1024 | | Sí / No | Sí / No | |
| 1440 | | Sí / No | Sí / No | |

También debes realizar estas pruebas:

- Ampliar el navegador hasta **200 %** y comprobar que el contenido sigue siendo utilizable.
- Navegar con **Tab**, **Shift+Tab** y **Enter** por los enlaces y botones.
- Cambiar entre orientación vertical/horizontal si dispones de emulador o móvil.
- Comprobar que la imagen conserva su proporción y que los textos largos no rompen la cuadrícula.
- Usar, si es posible, un dispositivo físico para detectar diferencias con la emulación.

**Criterio de aceptación:** no debe ser necesario desplazarse horizontalmente para utilizar el diseño general a los tamaños indicados. Una tabla ancha puede usar un contenedor con desplazamiento horizontal **interno**, claramente señalado.

## 7. Preguntas de comprensión

Responde brevemente, con ejemplos de tu CSS:

1. ¿Qué hace `width=device-width` dentro de `meta viewport`?
2. ¿Qué diferencia existe entre `width: 100%` y `width: 100vw`?
3. ¿Qué valor toma `10vw` si el viewport mide 500 px de ancho?
4. ¿Qué ventajas tiene `rem` respecto a fijar toda la tipografía en `px`?
5. ¿Por qué `font-size: 5vw` puede resultar inadecuado?
6. ¿Qué resuelve `box-sizing: border-box`?
7. ¿Cuándo elegirías Flexbox y cuándo CSS Grid?
8. ¿Qué significa construir con un enfoque **mobile first**?
9. ¿Cuál es la diferencia entre una media query y `clamp()`?
10. ¿Por qué una imagen con `width: 800px` puede romper el diseño móvil?
11. ¿Qué hacen `srcset` y `sizes`? Indica un caso en el que serían útiles.
12. ¿Por qué un diseño visualmente correcto puede seguir teniendo problemas de accesibilidad?

## 8. Entrega

Entrega una carpeta comprimida llamada `responsive-apellidos.zip` con:

- `index.html`, `styles.css` y el banner de `img/`.
- **Antes y después:** dos capturas de la página inicial y al menos tres de la versión adaptada (móvil, tableta, escritorio).
- Tabla de problemas, correcciones y matriz de pruebas.
- Respuestas a las 12 preguntas.
- Un documento `README.md` breve con qué editor y navegador has usado, instrucciones para abrir la página y resumen de los cambios.

No se valorará añadir bibliotecas externas: la solución debe ser **HTML y CSS propios**, sin frameworks obligatorios.

## 9. Rúbrica de evaluación (10 puntos)

| Criterio | Puntos |
|---|---:|
| HTML semántico y `meta viewport` correctamente configurados | 1 |
| Unidades fluidas, anchura adaptable y tipografía legible | 2 |
| Flexbox o Grid con comportamiento mobile first y media queries | 2 |
| Imagen adaptable, control de desbordamientos y conservación del contenido | 1,5 |
| Accesibilidad básica: zoom, teclado, foco, texto alternativo | 1 |
| Pruebas a cinco tamaños con evidencias antes y después | 1,5 |
| Justificación técnica y respuestas a las preguntas | 1 |
| **Total** | **10** |

## 10. Ampliaciones opcionales

1. Incorporar una **tabla** con un contenedor `overflow-x: auto` para que no desborde el diseño global.
2. Generar dos versiones del banner y utilizar `srcset` y `sizes` o `<picture>`.
3. Comparar `100vh`, `100svh` y `100dvh` en un navegador móvil y explicar el efecto de las barras del navegador.
4. Añadir estilos con `@media (prefers-reduced-motion: reduce)` si se introducen animaciones.
5. Usar **Lighthouse** o una herramienta de auditoría del navegador para encontrar nuevos problemas; interpretar los resultados y proponer soluciones, sin asumir que una puntuación garantiza accesibilidad.

## 11. Fuentes para investigar

- [MDN: diseño web adaptable (español)](https://developer.mozilla.org/es/docs/Learn_web_development/Core/CSS_layout/Responsive_Design)
- [MDN: etiqueta `meta viewport`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport)
- [MDN: media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries)
- [MDN: imágenes responsive](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images)

---

**Versión de la actividad:** 1.0.0 · **Fecha:** 23/11/2026 · **Estado:** lista para clase
