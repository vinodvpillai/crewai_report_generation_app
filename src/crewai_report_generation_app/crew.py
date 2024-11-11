from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai import LLM # type: ignore
# Uncomment the following line to use an example of a custom tool
# from report_generation_app.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool
import os
from os.path import join, dirname
from dotenv import load_dotenv


# Load environment variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

@CrewBase
class ReportGenerationAppCrew():
	"""ReportGenerationApp crew"""
	
	# LLM
	llm = LLM(model=os.getenv('GEMINI_MODEL'),api_key=os.getenv('GEMINI_API_KEY'))

	@agent
	def researcher(self) -> Agent:
		return Agent(
			llm=self.llm,
			config=self.agents_config['researcher'], # type: ignore
			tools=[SerperDevTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
      		llm=self.llm,
			config=self.agents_config['reporting_analyst'], # type: ignore
			verbose=True
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'], # type: ignore
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'], # type: ignore
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the ReportGenerationApp crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator # type: ignore
			tasks=self.tasks, # Automatically created by the @task decorator # type: ignore
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)