# Actividad 04. Java: de .java a .class y JVM

[Índice de actividades](README.md) · [Tema 2 en revisión](../REVISION-tema-02.md)

**RA1.c–e · Duración:** 50–70 min · **Material:** JDK instalado, terminal.

## Objetivo

Diferenciar el **compilador Java** y el **entorno Java** por sus comandos y salidas.

## Preparación

Comprueba `javac -version` y `java -version`. Si no existe `javac`, probablemente falta instalar o configurar correctamente un **JDK**.

## Archivo de inicio

Guarda **HolaED.java** con este contenido:

```java
public class HolaED {
    public static void main(String[] args) {
        int total = 3 + 4;
        System.out.println("Suma: " + total);
    }
}
```

## Pasos

1. Ejecuta `javac HolaED.java`; observa qué archivo nuevo aparece.
2. Ejecuta `java HolaED` (sin extensión) y captura el resultado.
3. Examina las instrucciones intermedias con `javap -c HolaED`.
4. Cambia `3 + 4` por `3 * 4`. Ejecuta **sin repetir `javac`** y explica qué versión se ejecuta.
5. Recompila y repite el paso anterior.
6. Cambia temporalmente el nombre de la clase sin cambiar el nombre del archivo, intenta compilar y registra el diagnóstico; revierte la modificación.
7. Investiga qué necesita otro ordenador para ejecutar el archivo `.class`.

## Respuestas

- ¿Qué función tienen `javac`, `javap` y `java`?
- ¿Puede el procesador ejecutar directamente las instrucciones de `javap`?
- ¿En qué consiste la portabilidad del bytecode y qué condiciones impone?
- ¿Por qué es importante controlar la versión del JDK/JRE?

## Criterios de logro

- [ ] Fuente Java correcto.
- [ ] Bytecode `.class` identificado.
- [ ] Secuencia compilación/ejecución reproducible.
- [ ] Respuestas justificadas con las salidas.

**Ampliación:** consultar `javap -verbose HolaED` y distinguir metadatos de instrucciones.
