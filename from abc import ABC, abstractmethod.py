from abc import ABC, abstractmethod

class Animal(ABC):
    @property                 
    def food_eaten(self):     
        return self._food

    @food_eaten.setter
    def food_eaten(self, food):
        if food in self.diet:
            self._food = food
        else:
            raise ValueError(f"You can't feed this animal with {food}.")

    @property
    @abstractmethod
    def diet(self):
        pass

    @abstractmethod 
    def feed(self, time):
        pass

class Lion(Animal):
    @property                 
    def diet(self):     
        return ["antelope", "cheetah", "buffaloe"]

    def feed(self, time):
        print(f"Feeding a lion with {self._food} meat! At {time}") 
   

leo = Lion()
leo.food_eaten = "antelope" 
leo.feed("10:10 AM")
