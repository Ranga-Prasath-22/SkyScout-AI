import os
from dotenv import load_dotenv
from browser_use import Agent, ChatGroq

load_dotenv()


def build_agent(task, browser):
    llm = ChatGroq(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        api_key=os.getenv("GROQ_API_KEY"),
    )
    return Agent(task=task, llm=llm, browser=browser)