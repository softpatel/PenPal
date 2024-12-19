from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class PenPals():
	"""PenPals crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def health_advisor(self) -> Agent:
		return Agent(
			config=self.agents_config['health_advisor'],
			verbose=True
		)
	
	@agent
	def financial_advisor(self) -> Agent:
		return Agent(
			config=self.agents_config['financial_advisor'],
			verbose=True
		)
		
	@agent
	def career_advisor(self) -> Agent:
		return Agent(
			config=self.agents_config['career_advisor'],
			verbose=True
		)

	@task
	def advise_health_task(self) -> Task:
		return Task(
			config=self.tasks_config['advise_health_task'],
			output_file='health report.md'
		)
	
	@task
	def advise_finances_task(self) -> Task:
		return Task(
			config=self.tasks_config['advise_finances_task'],
			output_file='finance report.md'
		)
	
	@task
	def advise_career_task(self) -> Task:
		return Task(
			config=self.tasks_config['advise_career_task'],
			output_file='career report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the PenPals crew"""

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True
		)
