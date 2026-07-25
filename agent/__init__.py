import os
from dotenv import load_dotenv
from browser_use import Agent
from langchain_groq import ChatGroq

load_dotenv()


def build_agent(task, browser):
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY"),
    )
    return Agent(task=task, llm=llm, browser=browser)