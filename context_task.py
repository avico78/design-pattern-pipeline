from enum import Enum
from typing import Callable, Dict

import sys
import time

from task_state import NA, TaskState
import itertools
from abc import ABC, abstractmethod,abstractproperty

from transformations.dataframe_transformations import DayaframeTransformation


class TaskType(str, Enum):
    LOAD = "Load"
    TRANSFORM = "Transform"


class TaskFactory(ABC):

    @abstractmethod
    def get_task(self):
        pass

    @abstractmethod
    def get_task_id(self):
        pass


class DataLoadFactory(TaskFactory,TaskState):

    "The DataLoad Factory Class"
    newid = itertools.count()

    def __init__(self, config: Dict):
        self.task = config.get('task')
        self.task_id = next(DataLoadFactory.newid) 
        self.depends_on = config.get('depends_on')
        self.task_params = config.get('task_params')
        self.task_state = NA()
        self.task_seq = config.get('task_seq')

    def get_task(self):
        return self.task
    
    def get_task_id(self):
        return self.task_id

    def set_state(self, state: str ):
        self.task_state.switch(getattr(sys.modules['task_state'], state))
    
    def get_state(self):
        return self.task_state.name
        #self.task_state = getattr(sys.modules['task_state'], state)
    
    
    # def execute_task(self) -> Callable :
    #     return getattr(DayaframeTransformation, self.task)(self.task_params)



class DataTransformationFactory(TaskFactory):
    "The DataLoad Factory Class"
 


class Workflow:
    workflow_task_bulk = {}

    def __init__(self):
        self.tasks = []

    def add_task(self, task: DataLoadFactory):
        self.tasks.append(task)

    def show_tasks(self):
        return [task.get_task() for task in self.tasks]

    def execute_task(self, task):
        
        if task.depends_on :
            # check requied tasks
            self.required_task(task)
        else:
            ##no dependedcy - can execute the task
            print("executing task", task.task_id)
          
            self.tasks[task.task_id].set_state('Started')
            
            return_from_task = getattr(DayaframeTransformation, task.task)(**task.task_params)
            self.tasks[task.task_id].set_state('Completed')
            return return_from_task
    

    def required_task(self,task):
        # loop through all requied (parent) task ONLY for those which wasn't executed (na)
        for required_task_id in (required_task_id for required_task_id in task.depends_on
                                           if self.tasks[required_task_id].get_state() == 'na'):
            return self.tasks[required_task_id]
        

    def execute_workflow(self):
        #iterating thrgouh each task - assumption all tasks started as na
        
        for task in (task for task in self.tasks if task.get_state() == 'na' ):
            print("Main -> task_id:", task.task_id)
            if task.depends_on :
                
                print("Depended task only -> task_id:", task.task_id ,"depands on", task.depends_on)
          #      self.check_depended_task_are_completed(task)

                #iterate on the required tasks id (list)
                for required_task_id in task.depends_on:
                    print("task requied in loop",self.tasks[required_task_id].task_id,"State",
                    self.tasks[required_task_id].get_state())

                    if self.tasks[required_task_id].get_state() == 'completed':
                        continue
                    #Try to execute the parent task
                    else:
                        print("task ",self.tasks[required_task_id].task_id,"State",
                    self.tasks[required_task_id].get_state())
                        self.execute_task(self.tasks[required_task_id])
          
            self.execute_task(task)
                    
    # def check_depended_task_are_completed(self,task):
    #     sleepless = True
    #     while (sleepless):
    #         for required_task_id in task.depends_on :
    #             if self.tasks[required_task_id].get_state() in ('completed','failed'):
    #                 sleepless = False
    #                 break
    #             else:
    #                 sleepless = False
    #             time.sleep(2)



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


