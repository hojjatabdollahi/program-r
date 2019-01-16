from programr.utils.logging.ylogger import YLogger


class LicenseKeys(object):

    def __init__(self):
        self._keys = {}

    def add_key(self, name, value):
        if name in self._keys:
            YLogger.warning(self, "License key [%s], already exists", name)
        self._keys[name] = value

    def has_key(self, name):
        return bool(name in self._keys)

    def get_key(self, name):
        if name in self._keys:
            return self._keys[name]
        else:
            raise ValueError("No license key named [%s]"%name)

    def load_license_key_data(self, license_key_data):
        lines = license_key_data.split('\n')
        for line in lines:
            line = line.strip()
            if line:
                self._process_license_key_line(line)

    def load_license_key_file(self, license_key_filename):
        try:
            YLogger.info(self, "Loading license key file: [%s]", license_key_filename)
            with open(license_key_filename, "r", encoding="utf-8") as license_file:
                for line in license_file:
                    self._process_license_key_line(line)
        except Exception:
            YLogger.error(self, "Invalid license key file [%s]", license_key_filename)

    def _process_license_key_line(self, line):
        line = line.strip()
        if line:
            if line.startswith('#') is False:
                splits = line.split("=")
                if len(splits) > 1:
                    key_name = splits[0].strip()
                    # If key has = signs in it, then combine all elements past the first
                    key = "".join(splits[1:]).strip()
                    self._keys[key_name] = key
                else:
                    YLogger.warning(self, "Invalid license key [%s]", line)
