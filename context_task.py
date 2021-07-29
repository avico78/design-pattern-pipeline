from enum import Enum
from typing import Callable, Dict

from task_state import TaskState

# from interface_data import DataLoadFactory
# from interface_transformation import  DataTransformationFactory
from abc import ABC, abstractmethod,abstractproperty

from transformations.dataframe_transformations import DayaframeTransformation


# class TaskStatus(str, Enum):
#     NA = "Na"
#     STARTED = "Started"
#     COMPLETED = "Complepted"
#     CANCELED = "Canceled"



class TaskType(str, Enum):
    LOAD = "Load"
    TRANSFORM = "Transform"


class TaskFactory(ABC):
    @property                 
    def construct_task(self):     
        return self._task

    @construct_task.setter
    def construct_task(self,config: Dict) -> "Task":
        print("Here", config.get('task'))

    @property                 
    def task_state(self):     
        pass

    #    return self._task
        # if food in self.diet:
        #     self._food = food
        # else:
        #     raise ValueError(f"You can't feed this animal with {food}.")
    # @staticmethod
    # @abstractmethod
    # def construct_task(self,config: Dict) -> "Task":
    #     pass



    def run_task(task: Callable) :
        pass


class DataLoadFactory(TaskFactory):

    "The DataLoad Factory Class"
    
            
    def task_state(self):
        return self.currstate

    # def __init__(self, execution_step: Callable, depends_on: "Task" = None,
    #              **kwargs) -> None:
    #     self.depends_on = depends_on
    #     self.execution_step = execution_step
    #     self._kwargs = kwargs

      
    # def construct_task(config: Dict) -> "Task": 
    #     @property
    #     def task(self)   :
    #         return "spme"
    #     # print("Here", config.get('task'))
    #     # print("selee", task_state)
        

    def run_task(task: Callable) :
        return getattr(DayaframeTransformation, task)(config.get('params'))
        #return f"Task {config.get('task')}"
        


class DataTransformationFactory(TaskFactory):
    "The DataLoad Factory Class"



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
        return factory.construct_task(config)



# class TaskContext():

#     available_factories = {
#         TaskType.LOAD: DataLoadFactory,
#         TaskType.TRANSFORM: DataTransformationFactory
#     }

#     @staticmethod
#     def get_context(config: Dict) -> TaskFactory:
#         #print(config)
#         task_type = config['operation']
#       #  print(task_type)
#         factory = TaskContext.available_factories.get(task_type)
#         if factory is None:
#              raise ValueError(f"No factory for task type: {task_type}")
#         return factory()