# Generador de presentaciones

## Ejecutar localmente

Requiere Python 3.12 y las dependencias **python-pptx, markdown, beautifulsoup4, cairosvg**.

~~~bash
python -m pip install python-pptx markdown beautifulsoup4 cairosvg
python scripts/generar_presentaciones.py
~~~

Detecta ficheros oficiales **tema-NN.md** y crea HTML/PPTX solo si la huella de teoría e imágenes vinculadas cambia. Los archivos **REVISION-tema-NN.md** y actividades no entran en presentaciones. GitHub Actions ejecuta el mismo script tras cambios relevantes, y sube presentaciones y manifiesto a main.
