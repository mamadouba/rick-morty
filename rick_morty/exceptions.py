class NotFoundError(Exception):
    def __init__(self, name: str, key: str, value: str):
        super().__init__(self, f"Not found: {name} with {key}={value} does not exist")


class ConflictError(Exception):
    def __init__(self, name: str, key: str, value: str):
        super().__init__(self, f"Conflict: {name} with {key}={value} already used")


class InternalError(Exception):
    def __init__(self, text: str):
        super().__init__(self, f"Internal error: {text}")
