from programy.config.file.xml_file import XMLConfigurationFile
from programy.config.file.yaml_file import YamlConfigurationFile
from programy.config.file.json_file import JSONConfigurationFile


class ConfigurationFactory(object):

    @classmethod
    def load_configuration_from_file(cls, client_configuration, filename, file_format=None, bot_root="."):

        if file_format is None or not file_format:
            file_format = ConfigurationFactory.guess_format_from_filename(filename)

        config_file = ConfigurationFactory.get_config_by_name(file_format)
        return config_file.load_from_file(filename, client_configuration, bot_root)

    @classmethod
    def guess_format_from_filename(cls, filename):
        if "." not in filename:
            raise Exception("No file extension to allow format guessing!")

        last_dot = filename.rfind(".")
        file_format = filename[last_dot + 1:]
        return file_format

    @classmethod
    def get_config_by_name(cls, file_format):
        file_format = file_format.lower()

        if file_format == 'yaml':
            return YamlConfigurationFile()
        elif file_format == 'json':
            return JSONConfigurationFile()
        elif file_format == 'xml':
            return XMLConfigurationFile()
        else:
            raise Exception("Unsupported configuration format:", file_format)
