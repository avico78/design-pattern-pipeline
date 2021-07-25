from abc import ABCMeta, abstractmethod


class TaskContext():

    "This is the object whose behavior will change"
    @staticmethod
    def task(strategy):
        """The request is handled by the class passed in"""
        return strategy()