# VENA — Vision-Enabled Navigation Agent

An agentic system that autonomously navigates websites using a vision-language model and browser control. Describe a task in plain English; VENA figures out the clicks, scrolls, and inputs to get it done.

Built with [browser-use](https://github.com/browser-use/browser-use) and Groq's Llama 3.3 70B.

## How it works

```
User Task (natural language)
        |
   Agent Loop
        |
 [Observe]  Screenshot + DOM state
 [Reason]   LLM decides next action
 [Act]      Playwright executes click/type/scroll
 [Evaluate] Success or retry
```

The agent handles dynamic UIs — popup modals, JavaScript-heavy SPAs, lazy-loaded content — without brittle CSS selectors.

## Project structure

```
agent/         # LLM initialization and agent config
browser/       # Browser setup (headless by default)
runner.py      # CLI entry point with --task argument
main.py        # Thin wrapper calling runner
Dockerfile     # Containerized deployment with Playwright Chromium
requirements.txt
```

## Setup

```bash
git clone https://github.com/Ranga-Prasath-22/VENA.git
cd VENA

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt
playwright install chromium
```

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

Get a free key at https://console.groq.com

## Usage

```bash
# Default task (Hacker News top 5)
python runner.py

# Custom task
python runner.py --task "Find the top 3 AI papers on arxiv today"

# Show browser window for debugging
python runner.py --no-headless
```

## Docker

```bash
docker build -t vena .
docker run --env-file .env vena
```

## Stack

| Component | Tool |
|---|---|
| LLM | Groq Llama 3.3 70B Versatile |
| Browser control | Playwright (via browser-use) |
| Agent framework | browser-use 0.13.6 |
| Python | 3.11+ |

## Why Groq?

Fast inference is critical for web agents — each browser action requires an LLM round-trip. Groq's LPU hardware keeps latency low enough for interactive-speed automation.