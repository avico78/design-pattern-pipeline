"The Table Interface"
from abc import ABCMeta, abstractmethod


class IDataLoad(metaclass=ABCMeta):
    "The data load Interface (task)"

    @staticmethod
    @abstractmethod
    def get_data():
        "A static interface method"

class LoadDataSqlDb(IDataLoad):   
    "Load data from LoadDataSqlDb"

    def __init__(self ):
        self._data = "None"
        
    def get_data(self, data_details):
        print("fetch the data by ", data_details)

        self._data = "data return from sqldb"
        
        return {"data" : self._data
        }


class LoadDataFromCsv(IDataLoad):   
    "Load data from LoadDataSqlDb"

    def __init__(self ):
        self._data = "None"
        
    def get_data(self, data_details):
        print("fetch the data by ", data_details)

        self._data = "data return from csv"
        return {"data" : self._data   }

class DataLoadFactory:  
    "The DataLoad Factory Class"

    @staticmethod
    def data_source(datarequest):
        "A static method to fetch data a chair"
        try:
            if datarequest == 'sqldb':
                return LoadDataSqlDb()
            if datarequest == 'csv':
                return LoadDataFromCsv()
                        
            raise Exception('DataResquest type Not Found')
        except Exception as _e:
            print(_e)
        return None

# if __name__ == "__main__":
    
#     data_loaded = DataLoadFactory.get_data("sqldb")
#     print(data_loaded.get_data("spo"))
#     print(data_loaded._data)
#     # print(f"{data_loaded.__class__} : {data_loaded.get_data()}")