from programy.utils.logging.ylogger import YLogger
import importlib

class ModuleLoader(object):

    @staticmethod
    def instantiate_module(module_string):
        module_path = module_string.strip()

        YLogger.debug(None, "Importing module [%s]", module_path)
        imported_module = importlib.import_module(module_path)

        return imported_module
