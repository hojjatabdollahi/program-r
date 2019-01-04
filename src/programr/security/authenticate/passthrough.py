from programr.config.brain.security import BrainSecurityConfiguration
from programr.security.authenticate.authenticator import Authenticator


class BasicPassThroughAuthenticationService(Authenticator):

    def __init__(self, configuration: BrainSecurityConfiguration):
        Authenticator.__init__(self, configuration)

    def authenticate(self, client_context):
        return True
