"""
Provides contestant's point fields.
"""


class Points:
    """
    Contestant's points.
    """

    __math: float
    __literature: float
    __foreign: float
    __spec: float
    __isspec: bool
    __foreign_lang: str
    __spec_subject: str

    def __init__(self, math, literature, foreign, foreign_lang, spec=0.0, isspec=False, spec_subject=""):
        self.__math = math
        self.__literature = literature
        self.__foreign = foreign
        self.__foreign_lang = foreign_lang
        self.__spec = spec
        self.__isspec = isspec
        self.__spec_subject = spec_subject

    @property
    def math(self):
        """
        Get contestant's math point.
        """
        return self.__math

    @property
    def literature(self):
        """
        Get contestant's literature point.
        """
        return self.__literature

    @property
    def foreign(self):
        """
        Get contestant's foreign language point.
        """
        return self.__foreign

    @property
    def spec(self):
        """
        Get contestant's specialized subject point.
        """
        return self.__spec

    @property
    def isspec(self):
        """
        Check contestant had taked specialized subject test.
        """
        return self.__isspec

    @property
    def foreign_lang(self):
        """
        Get contestant's foreign language.
        """
        return self.__foreign_lang

    @property
    def spec_subject(self):
        """
        Get contestan't specialized subject.
        """
        return self.__spec_subject
