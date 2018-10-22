class ApplicationException(RuntimeError):
    def __init__(self,arg):
        self.message = arg

class CoreException(ApplicationException):
    def __init__(self,arg):
        self.message = arg

class DatabaseException(CoreException):
    def __init__(self,arg):
        self.message = arg
