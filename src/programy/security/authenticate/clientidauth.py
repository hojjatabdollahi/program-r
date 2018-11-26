from programy.utils.logging.ylogger import YLogger

from programy.config.brain.security import BrainSecurityConfiguration
from programy.security.authenticate.authenticator import Authenticator


class ClientIdAuthenticationService(Authenticator):

    def __init__(self, configuration: BrainSecurityConfiguration):
        Authenticator.__init__(self, configuration)
        self.authorised = [
            "console"
        ]

    def user_auth_service(self, client_context):
        return False

    # Its at this point that we would call a user auth service, and if that passes
    # return true, appending the user to the known authorised list of user
    # This is a very naive approach, and does not cater for users that log out, invalidate
    # their credentials, or have a TTL on their credentials
    # #Exercise for the reader......
    def _auth_clientid(self, client_context):
        authorised = self.user_auth_service(client_context)
        if authorised is True:
            self.authorised.append(client_context.userid)
        return authorised

    def authenticate(self, client_context):
        try:
            if client_context.userid in self.authorised:
                return True
            else:
                if self._auth_clientid(client_context) is True:
                    return True

                return False
        except Exception as excep:
            YLogger.error(client_context, str(excep))
            return False
