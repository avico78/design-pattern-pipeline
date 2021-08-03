from typing import Dict

class DayaframeTransformation():
    def uppercase(**kwargs):
        print(kwargs)
        return ", ".join(f"{key}={value}" for key, value in kwargs.items())

    def lowercase(**kwargs) :
        print(kwargs)
        return ", ".join(f"{key}={value}" for key, value in kwargs.items())

