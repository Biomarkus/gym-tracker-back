from src.exceptions import BasicException

class SessionNotFound(BasicException):
    def __init__(self, details: str):
        super().__init__(404, details)