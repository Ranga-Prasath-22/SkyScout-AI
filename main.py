import asyncio
import os
from dotenv import load_dotenv

# Browser-Use has built-in LLM wrappers for easy integration
from browser_use import Agent, Browser, ChatGroq

load_dotenv()

async def main():
    # 1. Initialize the Groq LLM with Llama 4 Scout
    # Scout has 30,000 TPM (5x more than Maverick's 6,000 TPM on free tier!)
    # Also multimodal (Vision), 17B active params, 10M context window
    llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

    # 2. Browser Configuration
    # headless=False shows the browser window for debugging
    browser = Browser(headless=False)

    # 3. Create the Agent - Medium complexity task
    agent = Agent(
        task="Go to news.ycombinator.com (Hacker News). Get the titles and point scores of the top 5 posts on the front page.",
        llm=llm,
        browser=browser,
    )

    print("🚀 Groq-powered Agent starting...")
    
    try:
        result = await agent.run()
        print(f"✅ Mission Complete: {result}")
    except Exception as e:
        print(f"❌ Error during execution: {e}")

if __name__ == "__main__":
    asyncio.run(main())