# Actividad 05. Diagnosticar problemas según la fase

[Índice de actividades](README.md) · [Tema 2](../tema-02.md)

**RA1.c–f · Duración:** 50–60 min · **Material:** ordenador con Python y, si está disponible, GCC o Java.

## Objetivo

Distinguir errores de **sintaxis**, **enlace**, **carga**, **ejecución** y **lógica**.

## Casos para analizar

| Caso | Situación |
|---|---|
| A | Un archivo C contiene `printf("Hola")` sin el punto y coma necesario |
| B | Un programa C llama a `calcular()`, pero no existe una definición enlazable |
| C | Un programa compilado intenta cargar una biblioteca compartida que no está instalada |
| D | Un programa Python divide un número por cero |
| E | Una función calcula un IVA del 10 % cuando el requisito pide 21 %, sin mostrar error |

## Procedimiento

1. Clasifica cada caso: etapa de detección, tipo de problema y herramienta que puede ayudar.
2. Reproduce **como mínimo dos casos seguros** en un proyecto propio, sin modificar instalaciones ni configuraciones del sistema.
3. Registra el mensaje obtenido, si existe, y una hipótesis razonada.
4. Corrige uno de los fallos, registra cómo comprobaste que el problema desapareció.
5. Explica cuál de los casos **solo se detecta normalmente mediante pruebas o revisión funcional**.
6. Elabora un árbol de decisión breve: «¿Se produjo un binario? ¿Arranca el proceso? ¿La salida es correcta?».

## Entrega

Tabla clasificada, dos capturas, árbol de decisión y conclusión breve.

## Evaluación

- [ ] Clasificación correcta con justificación.
- [ ] No confunde error de compilación con error de ejecución.
- [ ] Corrección acompañada de prueba.
- [ ] Árbol de decisión útil para otro compañero.

**Ampliación:** investigar cómo un IDE facilita localizar el error mostrando el archivo y la línea.
