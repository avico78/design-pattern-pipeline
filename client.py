from context_task import TaskType,TaskContext,Workflow
#from interface_data import DataLoadFactory
#from interface_transformation import DataTransformationFactory

configs = [ {'operation': TaskType.LOAD,
     "task" : "uppercase",
     "depends_on": [1],
     "source": "csv",
     "task_params": {"key": "from_task_1"}
     },
     {'operation': TaskType.LOAD,
     "task" : "lowercase",
     "depends_on": [],
     "source": "csv",
     "task_params": {"key": "from_task_1"}
     },
     {'operation': TaskType.LOAD,
     "task" : "lowercase",
     "depends_on": [0,1],
     "source": "csv",
     "task_params": {"key": "from_task_2"}
     }]



workflow = Workflow()




tasks = [TaskContext.get_task(config) for config in configs]
for task in tasks:
   
     workflow.add_task(task)


workflow.execute_workflow()



#workflow.add_task(tasks[1])



# od = dict(sorted(a.items(), key=lambda item: item[1]))
# print(od)
# a = [task.execute_task() for task in tasks]

# print(a)








# # print(configs.get('params'))
# # exit()
# # dataload_context = TaskContext()
# a = TaskContext.get_task(configs)
# print(a.execute_task())

# # print(f"{data_load_factory.__class__}")

#v1