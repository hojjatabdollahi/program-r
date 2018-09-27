


class FacialExpressionRecognition():


    def __init__(self):
        self._values = []



    @property
    def values(self):
        return self._values

    @property
    def last_fer_value(self):
        return self._values[-1]

    def append(self, fer):
        self._values.append(fer)