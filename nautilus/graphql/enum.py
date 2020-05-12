from enum import IntEnum

from ariadne import EnumType

class RequestStatus(IntEnum):
    SUCCESS = 1
    FALIURE = 0


status_enum = EnumType("RequestStatus", RequestStatus)

bindables = [status_enum]
