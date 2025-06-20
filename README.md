# propclip-analyzer

🖥️ CLI tool to collect, clean, and structure clipboard snippets for AI processing _(without web scrapping)_.

## Concept

The main use case is job research:

1. While browsing job sites, you copy job offer snippets (Ctrl+C).
2. Using a configurable global hotkey, you add each snippet (“prop”) to a processing queue.
3. Later, you can preview and manually edit queued entries.
4. Snippets are processed by an AI API (Gemini), normalizing data into analyzable JSON.
5. Results can be organized by language, technology, seniority, and more.

This represents a flexible core for staging and processing any clipboard data with AI.

## Goal

Build a clean, flexible dataset of real-world job offers for:

-   Market trend analysis
-   Identifying top-demand technologies
-   Guiding study and career decisions
-   Publishing actionable insights

## Features

-   Global hotkey to capture clipboard snippets
-   Persistent raw data queue
-   Duplicate prevention
-   Manual preview and editing
-   AI-powered data processing (Google Gemini)
-   Cross-platform sound feedback (via [Notifications tones](https://github.com/akx/Notifications), CC0)
-   Linux desktop notifications (via notify-send)
-   Logging with custom logger
-   CLI designed with Typer

## Tech Stack

-   Python 3.11+
-   Typer (CLI framework)
-   pyperclip (clipboard integration)
-   pynput / keyboard (global hotkey)
-   google-genai (AI API)
-   rich (CLI preview)
-   pydantic (data schemas)
-   simpleaudio (sound feedback)

## Visualization (In Development)

Statistical report generation is planned using:

-   Pandas
-   Seaborn (and Matplotlib if needed)

Reports will be exported as images or notebooks.

---

[**License**: MIT](LICENSE)
