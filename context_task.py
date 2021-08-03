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

    def __init__(self, config: Dict):
        self.task = config.get('task')
        self.last_name = config.get('task_params')

    @abstractmethod
    def execute_task(self):
        pass

    #    return getattr(DayaframeTransformation, self.task)(self.task_params)
       # return f"{self.first_name} {self.last_name}"

    @abstractmethod
    def get_task(self):
        pass
 
    # @abstractmethod
    # def construct_task(self,config: Dict) -> "Task":
    #     self.task = config.get('task')




class DataLoadFactory(TaskFactory):

    "The DataLoad Factory Class"

    def __init__(self, config: Dict):
        self.task = config.get('task')
        self.task_params = config.get('task_params')
        self.task_seq = config.get('task_seq')

    def get_task(self):
        return self.task
    
    def execute_task(self) -> Callable :
        return getattr(DayaframeTransformation, self.task)(self.task_params)



class DataTransformationFactory(TaskFactory):
    "The DataLoad Factory Class"

def append_value(dict_obj, key, value):
    # Check if key exist in dict or not
    if key in dict_obj:
        # Key exist in dict.
        # Check if type of value of key is list or not
        if not isinstance(dict_obj[key], list):
            # If type is not list then make it list
            dict_obj[key] = [dict_obj[key]]
        # Append the value in list
        dict_obj[key].append(value)
    else:
        # As key is not in dict,
        # so, add key-value pair
        dict_obj[key] = value
# Dictionary of strings and ints
word_freq = {1: {"some": 12},2: {"some": 12},3: {"some": 12}
}

append_value(word_freq, 1, {"some": 1222})
print(word_freq)

class TaskBulk:
    task_start = 0

    def __init__(self):
        self.task_seq = []
 


class Workflow:
    workflow_task_bulk = {}

    def __init__(self):
        self.tasks = []

    def add_task(self, task: DataLoadFactory):
        self.tasks.append(task)

    def show_tasks(self):
        return [task.get_task() for task in self.tasks]

    def append_task(self,key, value):
        if key in self.workflow_task_bulk:
            # Key exist in dict.
            # Check if type of value of key is list or not
            if not isinstance(self.workflow_task_bulk[key], list):
                # If type is not list then make it list
                self.workflow_task_bulk[key] = [self.workflow_task_bulk[key]]
            # Append the value in list
            self.workflow_task_bulk[key].append(value)
        else:
            # As key is not in dict,
            # so, add key-value pair
            self.workflow_task_bulk[key] = value
        print(self.workflow_task_bulk)
    
    def get_workflow_bulk_plan(self):
        return self.workflow_task_bulk

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
        return factory(config)



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

   


    # @abstractmethod
    # def do_something(self):
    #     pass

    # @property                 
    # def construct_task(self):     
    #     return self._task

    # @construct_task.setter
    # def construct_task(self,config: Dict) -> str:
    #     print("Here", config.get('task'))

    # @property                 
    # def task_state(self):     
    #     pass

    #    return self._task
        # if food in self.diet:
        #     self._food = food
        # else:
        #     raise ValueError(f"You can't feed this animal with {food}.")
    # @staticmethod