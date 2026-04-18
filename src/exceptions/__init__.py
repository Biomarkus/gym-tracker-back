class BasicException(Exception):
    def __init__(self, status_code: int, details: str):
        self.status_code = status_code
        self.details = details


class FiltersEmpty(BasicException):
    def __init__(self, details: str):
        super().__init__(400, details)


class EmptyString(BasicException):
    def __init__(self, details: str):
        super().__init__(422, details)


class WrongDateFormat(BasicException):
    def __init__(self, details: str):
        super().__init__(422, details)