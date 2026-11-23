# Actividad 03. Explorar el bytecode de CPython

[Índice de actividades](README.md) · [Tema 2 en revisión](../REVISION-tema-02.md)

**RA1.d y RA1.e · Duración:** 50–60 min · **Material:** Python 3 (implementación CPython recomendada).

## Objetivo

Comprobar experimentalmente que Python puede generar **bytecode** y que ese bytecode **no es código máquina nativo**.

## Pasos

1. Comprueba la implementación y versión ejecutando en la terminal:
   - `python3 --version`
   - `python3 -c "import platform; print(platform.python_implementation())"`
   En Windows la orden puede ser `py` según la instalación.
2. Crea `operaciones.py`:

```python
def doble(numero):
    return numero * 2

print(doble(7))
```

3. Ejecuta el script: `python3 operaciones.py`.
4. Genera bytecode de forma expresa: `python3 -m py_compile operaciones.py`.
5. Examina el contenido de la carpeta `__pycache__` (si la implementación lo crea). Registra el nombre del archivo `.pyc`, pero **no intentes abrirlo como código fuente**.
6. Ejecuta `python3 -m dis operaciones.py` y localiza al menos **dos instrucciones de bytecode**.
7. Modifica la operación de multiplicación por una suma, vuelve a ejecutar y desensamblar, y registra un cambio observable.
8. Investiga qué herramienta ejecuta ese bytecode y por qué no equivale a `operaciones.exe`.

## Registro

| Evidencia | Qué demuestra |
|---|---|
| Versión de Python | |
| Salida del script | |
| Archivo .pyc | |
| Captura de dis | |
| Cambio entre las dos versiones | |

## Evaluación

- [ ] Se documenta qué versión e implementación se utilizan.
- [ ] Se distingue fuente, bytecode y ejecutable nativo.
- [ ] Se comparan observaciones de dos variantes.
- [ ] Se reconoce que las instrucciones `dis` pueden cambiar según la versión.

**Ampliación:** investigar por qué un `.pyc` puede no ser válido para otra versión del intérprete.
