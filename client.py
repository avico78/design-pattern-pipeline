from context_task import TaskContext
from interface_data import DataLoadFactory
from interface_transformation import TransformationFactory

data_load_json = '{ "source_db" : "details_to_db" , "query": "select * from table"}'
data_load_csv = '{ "file" : "input.csv" , "query": "select * from input"}'

dataload_context = TaskContext()
data_load_factory = dataload_context.task(DataLoadFactory)
sqldb_connector = data_load_factory.data_source("sqldb")
sql_data = sqldb_connector.get_data(data_load_json)
print("data ",sql_data)
csv_connector = data_load_factory.data_source("csv")
csv_data = csv_connector.get_data(data_load_csv)
print("data ",csv_data)

##### Transormation context

transformation_context = TaskContext()
transformation_factory = transformation_context.task(TransformationFactory)
transformation_1_connector = transformation_factory.transformation_type("Transoform_data_1")
csv_data_transform_1 = transformation_1_connector.transoform_data(csv_data)


