from programy.security.authorise.authorisor import Authoriser
from programy.config.brain.service import BrainServiceConfiguration


class PassThroughAuthorisationService(Authoriser):

    def __init__(self, config: BrainServiceConfiguration):
        Authoriser.__init__(self, config)

    def authorise(self, userid, role):
        return True
