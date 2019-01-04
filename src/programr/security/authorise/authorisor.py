from programr.config.brain.security import BrainSecurityConfiguration


class AuthorisationException(Exception):

    def __init__(self, msg):
        Exception.__init__(self, msg)


class Authoriser(object):

    def __init__(self, configuration: BrainSecurityConfiguration):
        self._configuration = configuration

    @property
    def configuration(self):
        return self._configuration

    def get_default_denied_srai(self):
        return self.configuration.denied_srai

    def authorise(self, userid, role):
        return False
