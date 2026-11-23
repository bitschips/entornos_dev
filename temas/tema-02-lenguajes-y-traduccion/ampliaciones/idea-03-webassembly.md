# Ampliación 03. WebAssembly

[Volver al índice de ampliaciones](README.md)

**Pregunta:** ¿cómo puede ejecutarse en un navegador un módulo que no está escrito originalmente en JavaScript?

## Conceptos

- **WebAssembly (Wasm)**: formato binario portátil y modelo de ejecución basado en una máquina abstracta.
- **Cadena de compilación**: ciertos compiladores pueden producir Wasm a partir de C, C++ u otros lenguajes.
- **Entorno**: navegador o runtime de Wasm que aporta APIs y límites de seguridad.
- **Diferencia clave**: Wasm no equivale a un ejecutable nativo independiente del runtime.

## Propuesta

Investiga una demo oficial, identifica `.wasm` y sus dependencias, y dibuja la cadena `fuente → herramienta de compilación → módulo Wasm → runtime`. Contrasta cómo se expone entrada/salida respecto a un programa de C en Linux.

**Fuentes de apoyo:** [webassembly.org](https://webassembly.org/) y [MDN WebAssembly](https://developer.mozilla.org/es/docs/WebAssembly).
