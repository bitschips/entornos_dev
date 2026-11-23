# Vídeo 01. Del código fuente al ejecutable

[Volver al índice de vídeos](README.md)

**Estado:** guion, vídeo todavía no generado · **Duración propuesta:** 90–110 s · **Objetivo:** representar las etapas de GCC, el enlace y la ejecución.

## Escenas y narración

| Tiempo | Visual propuesto | Narración |
|---|---|---|
| 00–15 s | Editor muestra `hola.c` | «Este texto es el código fuente escrito por una persona». |
| 15–30 s | `gcc -E` genera `hola.i` | «El preprocesador trata directivas y cabeceras». |
| 30–46 s | `gcc -S` genera `hola.s` | «El compilador puede producir instrucciones simbólicas». |
| 46–60 s | `gcc -c` genera `hola.o` | «El ensamblador prepara código objeto: aún no es un ejecutable completo». |
| 60–80 s | Enlazador resuelve referencias y bibliotecas | «Se construye el programa nativo con sus dependencias». |
| 80–100 s | El sistema operativo carga el programa; aparece «Hola» | «El sistema prepara el proceso y la CPU ejecuta instrucciones máquina». |

## Especificaciones para generación futura

Vectorial 16:9, fondo claro u oscuro de alto contraste, flechas legibles y archivos con sus extensiones correctas. No inventar salida de consola. Subtítulos en español, sin datos personales.

## Revisión técnica

- Diferenciar preprocesamiento, compilación, ensamblado, enlace y carga.
- No representar `hola.o` como ejecutable completo.
- No afirmar que GCC es siempre una única herramienta monolítica.
- Mantener etiquetas consistentes con la [actividad 02](../actividades/actividad-02-fases-gcc.md).
