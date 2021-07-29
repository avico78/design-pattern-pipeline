from context_task import TaskType,TaskContext
#from interface_data import DataLoadFactory
#from interface_transformation import DataTransformationFactory

configs = [ {'operation': TaskType.LOAD,
     "task" : "some_dict",
     "source": "csv",
     "task_params": {"path": "aaa/to/csv1"}
     },
     {'operation': TaskType.LOAD,
     "task" : "some_dict",
     "source": "csv",
     "task_params": {"path": "bbb/to/csv2"}
     }]



tasks = [TaskContext.get_task(config) for config in configs]

a = [task.execute_task() for task in tasks]

print(a)
# # print(configs.get('params'))
# # exit()
# # dataload_context = TaskContext()
# a = TaskContext.get_task(configs)
# print(a.execute_task())

# # print(f"{data_load_factory.__class__}")

#v1