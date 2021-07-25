import types 


class Factory():
    def process(self, input):
        raise NotImplementedError

 

class Extract(Factory):

    def process(self, input, func = None):
        if func is not None:
            self.execute = types.MethodType(func, self)

    def execute(self ,*input):
        print("Here def",input[0] )  

def load_sql(self, *input ):
    print('execute 1' , input)[0]

class Parse(Factory):
    def process(self, input):
        print("Parsing...")
        output = {}
        return output

class Load(Factory):
    def process(self, input):
        print("Loading...")
        output = {}
        return output

pipeline = {
    "Extract" : Extract(),
    "Parse" : Parse(),
    "Load" : Load(),
}

input_data = {} #vanilla input

extract_data = Extract()
extract_data.process(load_sql(1))

# by_sql = extract_data.process(load_sql)
# by_sql.execute(123)
# for process_name, process_instance in pipeline.items():
#     output = process_instance.process(input_data)
#     input_data = output








# # Strategy pattern
# #
# # Upon creation of a new object, define which implementation(s) # should be used. This can be algorithms or another method

# import types 

# class StrategyTrasnform:
#     def __init__(self, func = None):
#         self.name = None
#         if func is not None:
#             self.execute = types.MethodType(func, self)

#     def execute(self ,*arg):
#         print("Here def",self.name ,arg[0] )  

# def transormation_1(self ,*arg):
#     self.name = "hi"
#     print('execute 1',arg[0] )  

# def transormation_2(self):
#     print('execute 2')

