from typing import Dict, List

from exceptions import WorkflowConfigurationError
from operators import none_operator, operators
from state import State


class Task:

    def __init__(self, config: Dict):
        self.name = config.get('name')
        self.id = config.get('task_id')
        self.depends_on = config.get('depends_on', [])
        self.task_params = config.get('task_params', {})
        self.operator = operators.get(config.get('operator'), none_operator)
        self.workflow = None
        self.parents: List["Task"] = []
        self.children: List["Task"] = []
        self.result = None
        self.state = State.SCHEDULED

    def run(self):
        try:
            self.result = self.operator(*[child.result for child in self.children],
                                        **self.task_params)
        except Exception as e:
            self.state = State.FAILED
            self.workflow.state = State.FAILED
            self.result = e
        self.state = State.FINISHED
        self._notify_parents()

    def initialize_relations(self):
        for required in self.depends_on:
            child = self.workflow.find_task(required)
            if not child:
                raise WorkflowConfigurationError(
                    f"Task {required} does not exists in workflow {self.workflow.id}"
                    f" but it's required by task {self.id}")
            self.children.append(child)
            child.parents.append(self)

    def register_result(self, child):
        if not child.state == State.FINISHED:
            self.state = State.CANCELLED
            self._notify_parents()
        elif all(child.state == State.FINISHED for child in self.children):
            self.run()

    def _notify_parents(self):
        # this is a simplification that ou have one last task i.e. save to db
        # if they can be multiple ones you can do something similar to start_tasks
        # and notify workflow that checks if all last tasks are finished
        if not self.parents:
            self.workflow.result = self.result
            self.workflow.state = State.FINISHED
        else:
            for parent in self.parents:
                parent.register_result(self)
