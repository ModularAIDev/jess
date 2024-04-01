from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from aic import load_agent
from crewai import Task
from dotenv import load_dotenv
from textwrap import dedent


def create_jess_agent(verbose=True):
    load_dotenv()
    jess_character_id = "jess"

    #llm = ChatOpenAI(model_name="gpt-4-turbo-preview")
    #llm = ChatOpenAI(model_name="gpt-3.5-turbo-0125")
    
    llm = ChatAnthropic(model_name="claude-3-sonnet-20240229")
    # llm = ChatAnthropic(temperature=0, model_name="claude-3-opus-20240229")
    goal = "Provide support to the user, in whatever user might need"
    jess = load_agent(jess_character_id, llm, goal=goal)
    jess.allow_delegation = True
    return jess


def create_answer_task(agent, question):
    return Task(description=dedent(f"""
        As a support person, you have full dump of your previosue dialog with the user, you need to answer on the most latest message from the dialog, you can use any knowledge/context from dialog that is needed: {question}
        """),
         expected_output="Answer to the question",
    agent=agent)

