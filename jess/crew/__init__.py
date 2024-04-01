from jess.main import create_jess_agent, create_answer_task
from jess.crew.smart_agent import create_smart_agent
from jess.crew.date_time_agent import create_datetime_agent
from aic import load_agent
from langchain_openai import ChatOpenAI
from crewai import Crew, Process

from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

from ._tmp_alpaca import print_buying_power


def create_crew_for_question(question, verbose=True):
    load_dotenv()
    jess_agent = create_jess_agent()
    smart_agent = create_smart_agent()
    datetime_agent = create_datetime_agent()
    answer_task = create_answer_task(jess_agent, question)
    llm = ChatAnthropic(model_name="claude-3-sonnet-20240229")

    return Crew(
      agents=[
        jess_agent,
        datetime_agent,
        load_broker_agent()
      ],
      tasks=[answer_task],
      verbose=2,
      allow_delegation=True
      #manager_llm=llm,
      #process=Process.hierarchical
    )


def load_broker_agent():
    llm = ChatOpenAI(model_name="gpt-4-turbo-preview")
    return load_agent(
        "broker", 
        llm, 
        goal="Broker that has access to all financial user details (buying power), can help with anything related to user financial situation",
        tools=[print_buying_power])
