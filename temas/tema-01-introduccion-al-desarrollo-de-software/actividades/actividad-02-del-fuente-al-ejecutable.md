# Actividad 02. Del código fuente al ejecutable con C

[Volver al índice de actividades](README.md) · [Volver al tema](../tema-01.md)

**RA:** RA1.c, RA1.d · **Duración:** 50–60 minutos · **Sistema:** Linux o Windows con GCC/MinGW o compilador compatible.

## Objetivo

Observar diferencias entre **código fuente**, **código objeto**, **enlace** y **ejecutable**.

## Preparación

En terminal, prueba **gcc --version**. Si no está instalado, realiza la parte de inspección con material proporcionado por el profesor; **no descargues software de sitios no oficiales**.

## Pasos

1. Crea una carpeta **ed_tema1** y dentro el archivo **hola.c**.
2. Copia exactamente el código de ejemplo:

~~~c
#include <stdio.h>

int main(void) {
    puts("Hola, desarrollo");
    return 0;
}
~~~

3. Compila sin enlazar: **gcc -c hola.c -o hola.o**.
4. Inspecciona el directorio: identifica los tamaños y extensiones de **hola.c** y **hola.o**. En Linux puedes usar **ls -l**.
5. Enlaza: **gcc hola.o -o hola**. En Windows puede generarse **hola.exe**.
6. Ejecuta **./hola** en Linux, o el nombre del ejecutable adecuado en Windows.
7. Modifica el mensaje, vuelve a ejecutar el ejecutable **sin recompilar** y observa el resultado. Después recompila y vuelve a ejecutar.
8. Si tienes Linux, prueba **file hola.o** y **file hola**. Si no dispones de `file`, describe las diferencias observables sin inventar el formato del fichero.

## Tabla de resultados

| Archivo | ¿Es texto legible? | ¿Se puede ejecutar directamente? | Papel |
|---|---|---|---|
| hola.c | ... | ... | Fuente |
| hola.o | ... | ... | Objeto |
| hola / hola.exe | ... | ... | Ejecutable |

## Preguntas

- ¿Qué fase añadió el enlazador?
- ¿Por qué modificar el archivo C no modifica de inmediato el ejecutable ya generado?
- ¿Para qué sirve un archivo objeto si aún no es un programa ejecutable?

## Entrega y evaluación

Entregar **hola.c**, capturas de los comandos y de la ejecución, la tabla rellena y las respuestas.

- [ ] Identifica tres archivos y explica sus funciones.
- [ ] Distingue compilación de enlace.
- [ ] Obtiene una ejecución válida o documenta con precisión el bloqueo.
- [ ] Explica el efecto de modificar solo el fuente.

**Ampliación:** compilar con **gcc -Wall -Wextra** y explicar el propósito de los avisos. No confundir avisos con errores.
