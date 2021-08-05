class TaskState(object):
    name = "state"
    allowed = []

    def switch(self, state):
        """ Switch to new state """
        if state.name in self.allowed:
            print('Current:', self, ' => switched to new state', state.name)
            self.__class__ = state
        else:
            print('Current:', self, ' => switching to', state.name, 'not possible.')

    def __str__(self):
        return self.name


class NA(TaskState):
    name = "na"
    allowed = ['started']


class Started(TaskState):
    name = "started"
    allowed = ['stop', 'completed']


class Running(TaskState):
    """ State of being running """
    name = "running"
    allowed = ['stopped', 'canceled', 'completed']


class Stopped(TaskState):
    """ State of being running """
    name = "stopped"
    allowed = ['Canceled', 'Resume']


class Canceled(TaskState):
    """ State of being running """
    name = "canceled"
    allowed = ['Resume']


class Completed(TaskState):
    """ State of being running """
    name = "completed"
    allowed = []


class Resume(TaskState):
    """ State of being running """
    name = "canceled"
    allowed = ['running', 'failed']


class Failed(TaskState):
    """ State of being running """
    name = "failed"
    allowed = ['started']
