import sys
import importlib
import agents, tools, tasks

# 1. Force Colab to reload your files in case you edited them
importlib.reload(agents)
importlib.reload(tools)
importlib.reload(tasks)

from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task

# 2. Define the Crew
crew = Crew(
  agents=[blog_researcher, blog_writer],
  tasks=[research_task, write_task],
  process=Process.sequential,
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True
)

# 3. Kickoff
result = crew.kickoff(inputs={'topic':'Best ML projects that give me unfair advantage'})
print(result) 