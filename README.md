# Smart-Flight-Agent

[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Automation](https://img.shields.io/badge/Automation-Playwright-green.svg)](https://playwright.dev/)
[![AI](https://img.shields.io/badge/AI-LangChain-orange.svg)](https://langchain.com/)

> **A Python-based automation tool that autonomously searches and aggregates flight data using AI.**

## 📋 Overview

**Smart-Flight-Agent** is a practical demonstration of integrating Large Language Models (LLMs) with browser automation. It solves the problem of retrieving flight data from complex, dynamic travel websites that are difficult to scrape with traditional methods (like BeautifulSoup).

By allowing an LLM (Groq Llama 4) to "see" the page structure and control a headless browser, this tool can adapt to changing UI layouts and popup modals without hard-coded selectors.

## 🛠️ Tech Stack

I built this project to explore modern automation and AI engineering practices:

*   **Python 3.11**: Core logic and asynchronous execution.
*   **Playwright**: For reliable, cross-browser automation and rendering.
*   **LangChain**: To manage the reasoning loop between the agent and the browser.
*   **Docker**: Containerized the environment to ensure it runs consistently on any machine.
*   **Groq API**: utilized for high-speed inference to minimize agent latency.

## ⚙️ How It Works

1.  **Input**: The user defines a natural language goal (e.g., "Find the cheapest flight from JFK to LHR").
2.  **Reasoning**: The agent analyzes the current browser state (DOM).
3.  **Action**: It determines the next step (Click, Type, Submit) and executes it via Playwright.
4.  **Extraction**: Once the results page is reached, structured data is parsed and returned.

## 🚀 Getting Started

### Prerequisites
*   Python 3.11+
*   Docker Desktop (Optional, for containerized run)
*   Groq API Key

### Installation

```bash
# Clone the repository
git clone https://github.com/Ranga-Prasath-22/SkyScout-AI.git

# Install dependencies
pip install -r requirements.txt

# Setup Environment
# Create a .env file with your API key:
# GROQ_API_KEY=your_key
```

### Usage

```bash
python main.py
```

## 🤝 Context

This project was built to demonstrate proficiency in:
*   **Systems Engineering**: connecting distinct components (LLM, Browser, Python).
*   **Robustness**: Handling errors and unexpected UI states.
*   **Modern tooling**: Working with Containers and AsyncIO.

License: MIT
