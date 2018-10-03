
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
    def __init__(self, command, question, emotion):
        arguments = [question, emotion]
        super().__init__(command, arguments)
        self._question = question
        self._emotion = emotion


    @property
    def question(self):
        return self._question

    @property
    def emotion(self):
        return self._emotion


class ServiceRequest(Request):
    def __init__(self, command, arguments):
        super().__init__(command, arguments)
        self._service_name = arguments

    @property
    def service_name(self):
        return self._service_name


class ReadyRequest(Request):
    def __init__(self, command):
        super().__init__(command, arguments=None)


class SessionUserRequest(Request):

    def __init__(self, command, session_number, username):
        arguments = [session_number, username]
        super().__init__(command, arguments)
        self._session_number = session_number
        self._username = username

    @property
    def session_number(self):
        return self._session_number

    @property
    def username(self):
        return self._username