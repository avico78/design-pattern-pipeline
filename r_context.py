from enum import Enum
from typing import Dict


class TaskType(str, Enum):
    LOAD = "Load"
    TRANSFORM = "Transform"





class TaskFactory:
    "Factory classes should also have interface"


class DataLoadFactory(TaskFactory):
    "The DataLoad Factory Class"


class DataTransformationFactory(TaskFactory):
    "The DataLoad Factory Class"


class TaskContext:
    available_factories = {
        TaskType.LOAD: DataLoadFactory,
        TaskType.TRANSFORM: DataTransformationFactory
    }

    @staticmethod
    def get_context(config: Dict) -> TaskFactory:
        task_type = config.get('operation')
        print(task_type)
        factory = TaskContext.available_factories.get(task_type)
        if factory is None:
            raise ValueError(f"No factory for task type: {task_type}")
        return factory()