class LatLong(object):
    def __init__(self, latitude, longitude):
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def __str__(self):
        return self.to_string(precision=6)

    def to_string(self, precision=2):
        string_format = "%." + str(precision) + "f"
        string = "Latitude: " + string_format + ", Longitude: " + string_format
        return string % (self.latitude, self.longitude)
