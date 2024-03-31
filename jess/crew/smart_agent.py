from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from crewai import Agent


def create_smart_agent():
    load_dotenv()
    llm = ChatOpenAI(model_name="gpt-4-turbo-preview")
    
    return Agent(
        role="genius",
        goal="Provide support to the user, in whatever user might need",
        backstory="You are a genius, you know everything. You are here to help the user.",
        tools=[],
        llm=llm,
        verbose=True,
        allow_delegation=True
    )