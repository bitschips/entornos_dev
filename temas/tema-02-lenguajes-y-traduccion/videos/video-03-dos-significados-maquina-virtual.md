# Vídeo 03. Máquina virtual de lenguaje y máquina virtual de sistema

[Volver al índice de vídeos](README.md)

**Estado:** idea y guion; vídeo no generado · **Duración:** 60–80 s.

## Objetivo didáctico

Distinguir **JVM**, **máquina virtual de sistema** y **contenedor** sin confundir sus niveles de abstracción.

## Escenas

| Tiempo | Visual y narración |
|---|---|
| 0–20 s | Archivo `.class` se entrega a una JVM. «Se ejecuta código intermedio en un entorno de lenguaje». |
| 20–40 s | Un hipervisor ejecuta un sistema operativo invitado completo. «Aquí virtualizamos hardware para otro sistema». |
| 40–60 s | Dos contenedores Linux comparten núcleo del anfitrión. «Un contenedor aísla procesos y no requiere necesariamente un SO invitado completo». |
| 60–80 s | Comparativa final de requisitos y casos de uso. |

## Instrucciones y comprobación

Crear gráficos 16:9 en los que se vean host, SO invitado, JVM, proceso y núcleo. Subtitular todos los términos. Señalar que algunas implementaciones de contenedores en Windows y macOS utilizan una VM auxiliar; no presentar Docker como equivalente a una VM completa.

**Ampliación relacionada:** [VM y contenedores](../ampliaciones/idea-02-maquinas-virtuales-y-contenedores.md).
