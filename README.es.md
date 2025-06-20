# propclip-analyzer

🖥️ Herramienta CLI para recopilar, limpiar y estructurar fragmentos del portapapeles para procesamiento con IA _(sin web scraping)_.

## Concepto

El caso de uso principal es la investigación de ofertas laborales:

1. Mientras navegas por sitios de empleo, copias fragmentos de ofertas (Ctrl+C).
2. Con una tecla global configurable, añades cada fragmento (“prop”) a una cola de procesamiento.
3. Más tarde, puedes previsualizar y editar manualmente las entradas encoladas.
4. Los fragmentos se procesan mediante una API de IA (Gemini), normalizando los datos en JSON analizable.
5. Los resultados se pueden organizar por lenguaje, tecnología, seniority y más.

Esto representa un núcleo flexible para preparar y procesar cualquier dato del portapapeles con IA.

## Objetivo

Construir un conjunto de datos limpio y flexible de ofertas laborales reales para:

-   Analizar tendencias del mercado
-   Identificar tecnologías más demandadas
-   Orientar decisiones de estudio y carrera
-   Publicar insights accionables

## Funcionalidades

-   Tecla global para capturar fragmentos del portapapeles
-   Cola persistente de datos crudos
-   Prevención de duplicados
-   Previsualización y edición manual
-   Procesamiento con IA (Google Gemini)
-   Feedback sonoro multiplataforma (vía [Notifications tones](https://github.com/akx/Notifications), CC0)
-   Notificaciones de escritorio en Linux (notify‑send)
-   Registro de actividad con logger personalizado
-   CLI diseñada con Typer

## Tecnologías

-   Python 3.11+
-   Typer (framework CLI)
-   pyperclip (integración con portapapeles)
-   pynput / keyboard (tecla global)
-   google‑genai (API de IA)
-   rich (previsualización en CLI)
-   pydantic (esquemas de datos)
-   simpleaudio (reproducción de sonido)

## Visualización (En desarrollo)

Se planea generar informes estadísticos usando:

-   Pandas
-   Seaborn (y Matplotlib si es necesario)

Los informes se exportarán como imágenes o notebooks.

---

[**Licencia**: MIT](LICENSE)
