from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from crewai import Agent
from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from crewai_tools import tool


@tool("Check time")
def get_time(timezone: str) -> str:
    """Returns current time in timezone."""
    try:
        timezone = ZoneInfo(timezone)
        now = datetime.now(timezone)
        return now.strftime('%Y-%m-%d %H:%M:%S')
    except ZoneInfoNotFoundError:
        return "Unknown timezone"


def create_datetime_agent(verbose=True):
    load_dotenv()
    llm = ChatOpenAI(model_name="gpt-3.5-turbo")
    
    return Agent(
        role="Guy Who Knows Current Date and Time",
        goal="Your goal is to provide the current date and time, when asked.",
        backstory="You have a clock and calendar, you can use it.",
        tools=[get_time],
        llm=llm,
        verbose=verbose,
        allow_delegation=False
    )