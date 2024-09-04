from enum import Enum

class PageEnums(Enum):
    HOME_PAGE = 1
    PROJECT = 2

    @classmethod
    def choices(cls):
        return [(i, i.value) for i in cls]

class WorkEnums(Enum):
    PART_TIME = "PART TIME"
    FULL_TIME = "FULL TIME"

    @classmethod
    def choices(cls):
        return [(i, i.value) for i in cls]
