"""
The Strategy Pattern Concept

"""
from abc import ABCMeta, abstractmethod

class Context():
    "This is the object whose behavior will change"
    @staticmethod
    def request(strategy):
        """The request is handled by the class passed in"""
        return strategy()

class IStrategy(metaclass=ABCMeta):
    "A strategy Interface"
    @staticmethod
    @abstractmethod
    def __str__():
        "Implement the __str__ dunder"

class ConcreteStrategyA(IStrategy):
    "A Concrete Strategy Subclass"
    print("hi")
    def __str__(self):
        return "I am ConcreteStrategyA" 
    def test_pass(self,pa):
        return "I am tes" +pa
class ConcreteStrategyB(IStrategy):
    "A Concrete Strategy Subclass"
    def __str__(self):
        return "I am ConcreteStrategyB"

class ConcreteStrategyC(IStrategy):
    "A Concrete Strategy Subclass"
    def __str__(self):
        return "I am ConcreteStrategyC"
# The Client
CONTEXT = Context()
a = CONTEXT.request(ConcreteStrategyA)
print(a.test_pass("hh"))
# print(CONTEXT.request(ConcreteStrategyB))
# print(CONTEXT.request(ConcreteStrategyC))