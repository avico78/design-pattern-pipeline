"The Table Interface"
from abc import ABCMeta, abstractmethod


class ITransformation(metaclass=ABCMeta):
    "The traformation Interface"

    @staticmethod
    @abstractmethod
    def transoform_data():
        "A static interface method"

class Transoform_data_1(ITransformation):   
    "Transform data"

    def __init__(self ):
        self._data = "None"
        
    def transoform_data(self, data_details):
        print("transoform_data by 1 ", data_details)

        self._data = "data return from transoform_data_1"
        
        return {"data" : self._data    }


class Transoform_data_2(ITransformation):   
    print("transoform_data_2  data by")

    def __init__(self ):
        self._data = "None"
        
    def transoform_data(self, data_details):
        print("transoform_data by 2", data_details)

        self._data = "data return from transoform_data_2"
        return {"data" : self._data   }

class DataTransformationFactory:  
    "The Transformation Factory Class"

    @staticmethod
    def transformation_type(datarequest):
        "A static method to fetch data a chair"
        try:
            if datarequest == 'Transoform_data_1':
                return Transoform_data_1()
            if datarequest == 'Transoform_data_2':
                return Transoform_data_2()
                        
            raise Exception('Data Trasnformation type Not Found')
        except Exception as _e:
            print(_e)
        return None

# if __name__ == "__main__":
    
#     data_loaded = DataLoadFactory.get_data("sqldb")
#     print(data_loaded.get_data("spo"))
#     print(data_loaded._data)
#     # print(f"{data_loaded.__class__} : {data_loaded.get_data()}")