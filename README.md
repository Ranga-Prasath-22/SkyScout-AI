# VENA

[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Multi-Modal LLM](https://img.shields.io/badge/Model-Llama%204%20Vision-purple.svg)](https://ai.meta.com/)
[![Agentic AI](https://img.shields.io/badge/Agent-Autonomous-red.svg)](https://en.wikipedia.org/wiki/Intelligent_agent)

> **Autonomous Web Navigation Agent with Multi-Modal LLM Reasoning**

## 🌐 The Problem
**Solves**: Traditional web scraping breaks on dynamic Single Page Applications (SPAs).
**Solution**: VENA uses vision-language models to understand and navigate websites like a human, adapting to changing UIs in real-time.

## 📋 Overview

**VENA** handles the complexity of the modern web where standard selectors fail. By leveraging **Groq's Llama 4** for high-speed inference, it visually parses DOM structures, handles asynchronous loading states, and interacts with complex elements (modals, dropdowns) autonomously.

## 🛠️ Tech Stack

*   **Python 3.11**: Core logic and asynchronous execution.
*   **Playwright**: For reliable, cross-browser automation and rendering.
*   **LangChain**: To manage the reasoning loop between the agent and the browser.
*   **Docker**: Containerized the environment to ensure it runs consistently on any machine.
*   **Groq API**: utilized for high-speed inference to minimize agent latency.

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

This project demonstrates:
*   **Vision-Language Navigation**: Crossing the gap between text-based agents and visual interfaces.
*   **Large Action Models (LAM)**: Implementing agents that *do* things, not just *say* things.
*   **Resilient Engineering**: Building systems that self-heal against UI updates.

License: MIT
