from programr.utils.logging.ylogger import YLogger
from abc import ABCMeta, abstractmethod
from programr.utils.classes.loader import ClassLoader
from programr.config.brain.service import BrainServiceConfiguration


class Service(object):
    __metaclass__ = ABCMeta

    def __init__(self, config: BrainServiceConfiguration):
        self._config = config

    @property
    def configuration(self):
        return self._config

    def load_additional_config(self, service_config):
        pass

    @abstractmethod
    def ask_question(self, client_context, question: str):
        """
        Never knowingly Implemented
        """


class ServiceFactory(object):

    services = {}

    @classmethod
    def preload_services(cls, services_config):
        YLogger.debug(None, "In preload_services in ServiceFactory")
        loader = ClassLoader()
        for service_name in services_config.services():
            name = service_name.upper()
            service_config = services_config.service(service_name)
            YLogger.debug(None, "Preloading service [%s] -> [%s]", name, service_config.classname)
            meta_class = loader.instantiate_class(service_config.classname)
            new_class = meta_class(service_config)
            ServiceFactory.services[name] = new_class

    @classmethod
    def service_exists(cls, name):
        return bool(name.upper() in ServiceFactory.services)\

    @classmethod
    def get_service(cls, service):

        name = service.upper()
        if name in ServiceFactory.services:
            return ServiceFactory.services[name]
        else:
            raise Exception("Unknown service [%s]" % name)
