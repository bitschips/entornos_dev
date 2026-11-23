# Vídeo 02. Tres rutas: C, Python y Java

[Volver al índice de vídeos](README.md)

**Estado:** guion, vídeo no generado · **Duración estimada:** 80–95 s.  
**Objetivo:** comparar herramientas, formatos y runtimes.

## Guion

1. **Inicio (0–15 s):** tres paneles con programas que muestran el mismo mensaje. «Mismo objetivo, caminos diferentes».
2. **C (15–35 s):** `.c` → GCC + enlace → binario nativo → CPU y servicios del sistema.
3. **Python / CPython (35–55 s):** `.py` → compilación interna a bytecode → máquina virtual CPython → resultado.
4. **Java (55–75 s):** `.java` → `javac` → `.class` → JVM/JIT → resultado.
5. **Síntesis (75–95 s):** preguntarse qué archivo, runtime y dependencias necesita cada ruta.

## Guía de producción futura

Animación vectorial 16:9; colores distintos para tres tecnologías, archivos reales con extensiones y flechas de izquierda a derecha. Accesibilidad: subtítulos editables, términos legibles y ritmo pausado.

## Validación técnica

- La distinción compilado/interpretado depende de la implementación.
- Bytecode de CPython no equivale a ejecutable nativo.
- Una JVM compatible hace posible la portabilidad condicionada de bytecode Java.
- Evitar comparar velocidad sin pruebas controladas.

**Actividad relacionada:** [06. Tres caminos, el mismo resultado](../actividades/actividad-06-comparar-rutas-ejecucion.md).
