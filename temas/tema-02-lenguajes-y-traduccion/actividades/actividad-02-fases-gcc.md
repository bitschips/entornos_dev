# Actividad 02. Observar las fases de compilación con GCC

[Índice de actividades](README.md) · [Tema 2 en revisión](../REVISION-tema-02.md)

**RA1.c–d · Duración:** 60–75 min · **Material:** GCC instalado en Linux (o adaptación explícita en otro sistema).

## Objetivo

Generar archivos visibles en **cada etapa** y explicar cuándo aparece un ejecutable.

## Archivo de trabajo

Crea una carpeta llamada `actividad02` y guarda dentro `calculo.c`:

```c
#include <stdio.h>

#define BASE 10

int main(void) {
    int resultado = BASE + 5;
    printf("Resultado: %d\n", resultado);
    return 0;
}
```

## Pasos

1. Comprueba que `gcc --version` funciona y registra la versión.
2. Genera el preprocesado: `gcc -E calculo.c -o calculo.i`.
3. Genera ensamblador: `gcc -S calculo.c -o calculo.s`.
4. Genera código objeto: `gcc -c calculo.c -o calculo.o`.
5. Enlaza: `gcc calculo.o -o calculo`.
6. Ejecuta: `./calculo` y registra la salida.
7. Inspecciona qué archivos se pueden abrir como texto y cuáles son binarios. **No edites los archivos intermedios**.
8. Cambia `BASE` por otro valor, **ejecuta primero el binario antiguo sin recompilar**, anota la salida y después repite la compilación.
9. Introduce un error de sintaxis, registra el diagnóstico y corrígelo.

## Tabla de resultados

| Archivo | Comando que lo origina | Texto / binario | ¿Ejecutable directamente? |
|---|---|---|---|
| calculo.c | Editor | | |
| calculo.i | | | |
| calculo.s | | | |
| calculo.o | | | |
| calculo | | | |

## Cuestiones y entrega

- ¿Qué cambió en `calculo.i` al modificar la macro `BASE`?
- ¿Qué diferencia hay entre ensamblar y enlazar?
- ¿Por qué el ejecutable no cambia cuando solo guardas el archivo fuente?
- Identifica la etapa en la que se produjo el error intencionado.

Entregar código fuente, capturas breves de comandos, tabla y respuestas.

**Comprobación:** se distinguen cinco formatos; se ejecuta el programa; se explica el papel del enlace; se diagnostica el fallo sin inventar causas.

**Ampliación:** ejecutar `gcc -Wall -Wextra calculo.c -o calculo` y explicar qué son los avisos.
