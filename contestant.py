"""
Provides contestant information.
"""

from points import Points


class Contestant:
    """
    Contestant's information.
    """

    __id_code: str
    __full_name: StopAsyncIteration
    __points: Points

    def __init__(self, id_code: str, full_name: str, point: Points):
        self.__id_code = id_code
        self.__full_name = full_name
        self.__points = point

    @property
    def id_code(self):
        """
        Get contestant's id code.
        """
        return self.__id_code

    @property
    def full_name(self):
        """
        Get contestant's full name.
        """
        return self.__full_name

    @property
    def points(self):
        """
        Get contestant's point's information.
        """
        return self.__points