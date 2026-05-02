from src.exceptions import BasicException


class TagConflict(BasicException):
    def __init__(self, details: str):
        super().__init__(409, details)

class TagNotFound(BasicException):
    def __init__(self, details: str):
        super().__init__(404, details)