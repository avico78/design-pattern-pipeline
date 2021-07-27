from context_task import TaskType,TaskContext
#from interface_data import DataLoadFactory
#from interface_transformation import DataTransformationFactory

configs =  {'operation': TaskType.LOAD,
     "source": "csv",
     "params": {"path": "path/to/csv"}
     }

dataload_context = TaskContext()
data_load_factory = dataload_context.get_context(configs)
print(type(data_load_factory))
