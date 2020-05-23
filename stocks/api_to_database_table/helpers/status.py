from enum import Enum


class Status(Enum):
    Success = 0
    Failed = 1
    Invalid = 2
    API_Limit = 3
