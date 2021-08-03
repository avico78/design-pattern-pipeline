from context_task import TaskType,TaskContext,Workflow
#from interface_data import DataLoadFactory
#from interface_transformation import DataTransformationFactory

configs = [ {'operation': TaskType.LOAD,
     "task" : "some_dict",
     "source": "csv",
     "task_seq": 1,
     "task_params": {"path": "aaa/to/csv1"}
     },
     {'operation': TaskType.LOAD,
     "task" : "some_dict",
     "task_seq": 1,
     "source": "csv",
     "task_params": {"path": "bbb/to/csv2"}
     }]



workflow = Workflow()




tasks = [TaskContext.get_task(config) for config in configs]

workflow.add_task(tasks[0])
workflow.add_task(tasks[1])

print(workflow.show_tasks())
workflow.append_task(1,{"1":3 })
workflow.append_task(9,{"1":4 })
workflow.append_task(2,{"1":8 })
workflow.append_task(5,{"1":10 })
workflow.append_task(8,{"1":100 })
a = workflow.get_workflow_bulk_plan()
print(a.keys())


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