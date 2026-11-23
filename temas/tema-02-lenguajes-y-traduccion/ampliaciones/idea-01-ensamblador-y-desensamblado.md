# Ampliación 01. Ensamblador y desensamblado

[Volver al índice de ampliaciones](README.md)

**Pregunta:** ¿puede estudiarse qué instrucciones genera GCC sin construir un programa en ensamblador desde cero?

## Propuesta práctica

1. Escribe una función pequeña en C, por ejemplo `int doble(int x) { return 2*x; }`.
2. Compila con `gcc -S ejemplo.c -o ejemplo.s`.
3. Examina el archivo de texto `.s` e identifica etiquetas, registros y al menos una instrucción reconocible.
4. Compila también con `gcc -O2 -S ejemplo.c -o ejemplo_opt.s` y compara cambios.
5. Opcionalmente, en un equipo con binutils, examina el objeto con `objdump -d ejemplo.o`.
6. Explica por qué el código máquina varía según CPU, plataforma y optimización.

## Evidencias

Tabla comparativa, capturas de fragmentos y explicación de tres instrucciones. No obligar a que una línea de C tenga correspondencia uno a uno con una instrucción.
