from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from crewai import Agent


def create_smart_agent(verbose=True):
    load_dotenv()
    llm = ChatOpenAI(model_name="gpt-4-turbo-preview")
    #llm = ChatAnthropic(temperature=0, model_name="claude-3-opus-20240229")
    
    return Agent(
        role="genius",
        goal="Provide support to the user, in whatever user might need",
        backstory="You are a genius, you know everything. You are here to help the user.",
        tools=[],
        llm=llm,
        verbose=verbose,
        allow_delegation=True
    )