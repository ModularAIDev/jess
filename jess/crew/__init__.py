from jess.main import create_jess_agent, create_answer_task
from jess.crew.smart_agent import create_smart_agent
from crewai import Crew


def create_crew_for_question(question, verbose=True):
    jess_agent = create_jess_agent()
    smart_agent = create_smart_agent()
    answer_task = create_answer_task(jess_agent, question)

    return Crew(
      agents=[
        jess_agent,
        smart_agent
      ],
      tasks=[answer_task],
      verbose=verbose,
      allow_delegation=True
    )
