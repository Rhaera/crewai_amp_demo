from typing import List

from crewai import Agent, Crew, Process, Task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class NouriCrew():
    """Nouri Crew – deployable on CrewAI AMP and exposed as MCP.
    
    MVP scope: Smart List Manager and Deal Hunter agents only.
    Post-MVP agents (Substitution, Household Coordinator, Approval Gatekeeper) 
    are deferred per descoped MVP requirements.
    """

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def smart_list_manager(self) -> Agent:
        return Agent(
            config=self.agents_config["smart_list_manager"],  # type: ignore[index]
            verbose=True,
        )

    @agent
    def deal_hunter(self) -> Agent:
        return Agent(
            config=self.agents_config["deal_hunter"],  # type: ignore[index]
            verbose=True,
        )

    # Tasks loaded from YAML (crew/config/tasks.yaml)

    @task
    def smart_list_generation(self) -> Task:
        return Task(
            config=self.tasks_config["smart_list_generation"],  # type: ignore[index]
        )

    @task
    def deal_hunting(self) -> Task:
        return Task(
            config=self.tasks_config["deal_hunting"],  # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Nouri crew."""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
