from programy.utils.logging.ylogger import YLogger
import importlib

class ClassLoader(object):

    @staticmethod
    def instantiate_class(class_string):
        processor_path = class_string.strip()
        YLogger.debug(None, "Processor path [%s]", processor_path)

        last_dot = processor_path.rfind(".")
        module_path = processor_path[:last_dot]
        class_name = processor_path[last_dot+1:]

        YLogger.debug(None, "Importing module [%s]", module_path)
        imported_module = importlib.import_module(module_path)

        YLogger.debug(None, "Instantiating class [%s]", class_name)
        new_class = getattr(imported_module, class_name)
        return new_class
