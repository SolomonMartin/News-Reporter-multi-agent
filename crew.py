from crewai import Crew,Process
from agents import news_researcher,news_writer
from tasks import research_task,write_task

crew = Crew(
    agents = [news_researcher,news_writer],
    tasks = [research_task,write_task],
    process = Process.sequential,
)

result = crew.kickoff(inputs={'topic': 'Impact of AI on Tech sector and Jobs'})
print(result)