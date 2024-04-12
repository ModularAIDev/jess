from jess.main import create_jess_agent, create_answer_task
from jess.crew.smart_agent import create_smart_agent
from aic import load_agent
from langchain_openai import ChatOpenAI
from crewai import Crew, Process
from dotenv import load_dotenv
from aic_tools_pinecone import init_toolbox_with_gptembeddings, query_from_long_term_memory, store_in_long_term_memory
from openai import OpenAI

import os
import pinecone

load_dotenv()

from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from aic_tools_alpaca.account_info import get_buying_power

PINECONE_KEY = os.getenv('PINECONE_KEY')
USER_ID = "113685807430823249126"

client = OpenAI()


pinecone.init(api_key=PINECONE_KEY, environment='gcp-starter')
init_toolbox_with_gptembeddings(USER_ID, client, pinecone)


def create_crew_for_question(question, verbose=True):
    load_dotenv()
    jess_agent = create_jess_agent(verbose=verbose)
    print(jess_agent.tools)
    #print(jess_agent.tools)
    #smart_agent = create_smart_agent()
    #datetime_agent = create_datetime_agent()
    answer_task = create_answer_task(jess_agent, question)
    #llm = ChatAnthropic(model_name="claude-3-sonnet-20240229")

    return Crew(
      agents=[
        jess_agent,
        load_broker_agent(),
        load_knowledge_keeper_agent()
      ],
      tasks=[answer_task],
      verbose=verbose,
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
        tools=[get_buying_power])

def load_knowledge_keeper_agent():
    llm = ChatOpenAI(model_name="gpt-3.5-turbo-0125")
    return load_agent(
        "KnowledgeKeeper", 
        llm, 
        goal="KnowledgeKeeper that can be used to store and retrieve information about the user or any information that should be memorized long term",
        tools=[query_from_long_term_memory, store_in_long_term_memory])