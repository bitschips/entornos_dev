# Ampliación 02. Máquina virtual de lenguaje, de sistema y contenedores

[Volver al índice de ampliaciones](README.md)

**Pregunta:** ¿una JVM, VirtualBox y Docker hacen lo mismo?

| Tecnología | Qué abstrae | Ejemplo |
|---|---|---|
| JVM | Instrucciones y servicios para bytecode Java | Ejecutar un `.class` compatible |
| VirtualBox / KVM | Hardware virtualizado para un SO invitado | Arrancar Linux dentro de otro equipo |
| Contenedor | Procesos y recursos aislados en un sistema anfitrión | Ejecutar un servidor web aislado |

## Actividad

Dibujar tres esquemas con «anfitrión, invitado, proceso, runtime»; elegir un ejemplo DAW para cada arquitectura y explicar cómo se instalan dependencias. Distinguir contenedores de máquinas virtuales completas, aunque algunas instalaciones de contenedores utilicen internamente una VM.

**Evidencia:** tres diagramas y cinco diferencias razonadas.
