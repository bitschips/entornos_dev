# Actividad 03. Mi primer programa Python desde editor y terminal

[Volver al índice de actividades](README.md) · [Volver al tema](../tema-01.md)

**RA:** RA1.a y RA1.f · **Duración:** 35–50 minutos · **Entorno:** KWrite, Geany, VS Code o editor disponible; terminal del sistema.

## Objetivo

Crear, guardar, ejecutar, corregir y documentar un programa sencillo sin confundir editor, intérprete y sistema operativo.

## Pasos

1. Abre un editor de texto **sin formato**. Crea una carpeta de trabajo propia.
2. Escribe en **hola.py**:

~~~python
# Autor: [tu nombre]
# Fecha: [dd/mm/aaaa]
# Versión: 1.0
print("Hola, mundo")
~~~

3. Guarda el archivo y comprueba que su extensión es **.py**.
4. En Linux abre terminal, sitúate en la carpeta con **cd** y ejecuta **python3 hola.py**. En Windows podría usarse **py hola.py**, según la instalación.
5. Modifica el mensaje y vuelve a ejecutar. Describe qué proceso crees que cambió.
6. Introduce voluntariamente un error de sintaxis (por ejemplo, elimina un paréntesis). Ejecuta, copia el mensaje de error, vuelve a corregir y verifica.
7. Explica qué hace el **editor**, qué hace el **intérprete** y por qué el programa necesita **CPU y RAM**.
8. Comprueba de forma opcional **python3 -m py_compile hola.py** y busca el directorio **__pycache__** si tu implementación lo genera. Explica que este bytecode no es un ejecutable nativo independiente.

## Entrega

- **hola.py** correcto con comentarios y versión.
- Capturas de una ejecución válida y del error corregido.
- Tabla de funciones: editor, terminal, intérprete, memoria, CPU y pantalla.
- Reflexión breve: «¿Dónde se produjo el error y cómo lo detecté?».

## Criterios

- [ ] Código sintácticamente correcto.
- [ ] Archivo y carpeta identificables.
- [ ] Ejecución repetible.
- [ ] Diferencia entre editor, intérprete y hardware.
- [ ] Explicación del error basada en evidencias.

**Ampliación:** ejecutar el mismo fuente con dos editores diferentes sin modificar Python y explicar qué permanece igual.
