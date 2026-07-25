import asyncio
import argparse

from agent import build_agent
from browser import build_browser

DEFAULT_TASK = (
    "Go to news.ycombinator.com. "
    "Get the titles and point scores of the top 5 posts on the front page."
)


async def run(task=DEFAULT_TASK, headless=True):
    browser = build_browser(headless=headless)
    agent = build_agent(task, browser)
    try:
        result = await agent.run()
        print(f"Done: {result}")
        return result
    except Exception as e:
        print(f"Error: {e}")
        raise


def main():
    parser = argparse.ArgumentParser(description="VENA - Vision-Enabled Navigation Agent")
    parser.add_argument("--task", default=DEFAULT_TASK, help="Natural language task for the agent")
    parser.add_argument("--no-headless", dest="headless", action="store_false", help="Show browser window")
    parser.set_defaults(headless=True)
    args = parser.parse_args()
    asyncio.run(run(task=args.task, headless=args.headless))


if __name__ == "__main__":
    main()