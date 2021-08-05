from typing import Dict, List, Optional

from context_task import TaskContext
from state import State
from task import Task


class Workflow:
    workflow_task_bulk = {}

    def __init__(self, id: int):
        self.id = id
        self.tasks = []
        self.starting_tasks = []
        self.result = None
        self.state = State.SCHEDULED

    def load_tasks(self, configs: List[Dict]):
        self.tasks = [TaskContext.get_task(config) for config in configs if
                      config.get("workflow_id") == self.id]
        self._initialize_workflow()

    def run(self):
        # note that this in real life should be triggered in parallel etc.
        for task in self.starting_tasks:
            task.run()

    def find_task(self, task_id: int) -> Optional[Task]:
        return next((task for task in self.tasks if task.id == task_id), None)

    def _initialize_workflow(self):
        for task in self.tasks:
            task.workflow = self
            if not task.depends_on:
                self.starting_tasks.append(task)
            else:
                task.initialize_relations()
