from task_type import TaskType
from workflow import Workflow

configs = [
    {'task_id': 1,
     'operation': TaskType.LOAD,
     "name": "load_csv",
     "operator": "read_csv",
     "depends_on": [],
     "source": "csv",
     "task_params": {"path": "./data/sample.csv"},
     "workflow_id": 1
     },
    {'task_id': 2,
     'operation': TaskType.TRANSFORM,
     "name": "clean",
     "operator": "remove_whitespace",
     "depends_on": [1],
     "task_params": {},
     "workflow_id": 1
     },
    {'task_id': 3,
     'operation': TaskType.TRANSFORM,
     "name": "get dictionaries",
     "operator": "convert_to_dictionary",
     "depends_on": [2],
     "task_params": {},
     "workflow_id": 1
     },
    {'task_id': 4,
     'operation': TaskType.TRANSFORM,
     "name": "lowercase",
     "operator": "rename_fields",
     "depends_on": [3],
     "task_params": {
         "field_map": {
             "field_1": "ID",
             "field_2": "Position",
             "field_3": "Name",
             "field_4": "City",
             "field_5": "Age",
             "field_6": "Potential",
             "field_7": "Year",
         }
     },
     "workflow_id": 1
     },
    {'task_id': 5,
     'operation': TaskType.TRANSFORM,
     "name": "uppercase",
     "operator": "uppercase",
     "depends_on": [4],
     "task_params": {"fields_to_apply": {"ID", "Name", "Age"}},
     "workflow_id": 1
     }
]

workflow = Workflow(id=1)
workflow.load_tasks(configs)
workflow.run()
print(workflow.state)
for line in workflow.result:
    print(line)
