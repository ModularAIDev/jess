from langchain.chat_models import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from aic import load_character
from crewai import Agent, Task
from dotenv import load_dotenv
from textwrap import dedent


def create_jess_agent():
    load_dotenv()
    jess_character_id = "jess"
    jess_character = load_character(jess_character_id)

    #llm = ChatOpenAI(model_name="gpt-4-turbo-preview")
    llm = ChatOpenAI(model_name="gpt-3.5-turbo-0125")
    
    #llm = ChatAnthropic(
    #    temperature=0., model_name="claude-3-opus-20240229")
    return Agent(
        role=jess_character.roleName,
        goal='Provide support to the user, in whatever user might need',
        backstory=jess_character.backstory,
        tools=[],
        llm=llm,
        verbose=True,
        allow_delegation=True
    )


def create_answer_task(agent, question):
    return Task(description=dedent(f"""
        As a support person, answer user to the input question: {question}
        """),
    agent=agent)

