from enum import Enum


class TaskType(str, Enum):
    LOAD = "Load"
    TRANSFORM = "Transform"