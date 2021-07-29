from context_task import TaskType,TaskContext
#from interface_data import DataLoadFactory
#from interface_transformation import DataTransformationFactory

configs =  {'operation': TaskType.LOAD,
     "task" : "some_dict",
     "source": "csv",
     "params": {"path": "path/to/csv"}
     }

# print(configs.get('params'))
# exit()
# dataload_context = TaskContext()
a = TaskContext.get_task(configs)
print(a)

# print(f"{data_load_factory.__class__}")

#v1