from programr.config.brain.security import BrainSecurityConfiguration


class Authenticator(object):

    def __init__(self, configuration: BrainSecurityConfiguration):
        self._configuration = configuration

    @property
    def configuration(self):
        return self._configuration

    def get_default_denied_srai(self):
        return self.configuration.denied_srai

    def authenticate(self, client_context):
        return False
