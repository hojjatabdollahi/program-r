


class Request():

    def __init__(self, command, arguments):
        self._command = command
        self._arguments = arguments

    @property
    def command(self):
        return self._command


    @property
    def arguments(self):
        return self._arguments



class SessionRequest(Request):
    def __init__(self, command, arguments):
        super().__init__(command, arguments)
        self._session_number = arguments

    @property
    def session_number(self):
        return self._session_number



class UserRequest(Request):
    def __init__(self, command, arguments):
        super().__init__(command, arguments)
        self._username = arguments

    @property
    def username(self):
        return self._username


class QuestionRequest(Request):
    def __init__(self, command, arguments):
        super().__init__(command, arguments)
        self._question = arguments


    @property
    def question(self):
        return self._question


class ReadyRequest(Request):
    def __init__(self, command):
        super().__init__(command, arguments=None)




