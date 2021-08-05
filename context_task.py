from typing import Dict

from factories import DataLoadFactory, DataTransformationFactory
from task import Task
from task_type import TaskType


class TaskContext:
    available_factories = {
        TaskType.LOAD: DataLoadFactory,
        TaskType.TRANSFORM: DataTransformationFactory
    }

    @staticmethod
    def get_task(config: Dict) -> "Task":
        task_type = config.get('operation')
        factory = TaskContext.available_factories.get(task_type)
        if factory is None:
            raise ValueError(f"No factory for task type: {task_type}")
        return factory.get_task(config)
