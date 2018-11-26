from programy.utils.logging.ylogger import YLogger

from programy.security.authorise.authorisor import Authoriser
from programy.security.authorise.authorisor import AuthorisationException
from programy.security.authorise.usergrouploader import UserGroupLoader
from programy.config.brain.security import BrainSecurityAuthorisationConfiguration

class BasicUserGroupAuthorisationService(Authoriser):

    def __init__(self, config: BrainSecurityAuthorisationConfiguration):
        Authoriser.__init__(self, config)
        self.load_users_and_groups()

    def load_users_and_groups(self):

        self._users = {}
        self._groups = {}

        if self.configuration.usergroups is not None:
            loader = UserGroupLoader()
            self._users, self._groups = loader.load_users_and_groups_from_file(self.configuration.usergroups)
        else:
            YLogger.warning(self, "No user groups defined, authorisation tag will not work!")

    def authorise(self, userid, role):
        if userid not in self._users:
            raise AuthorisationException("User [%s] unknown to system!"%userid)

        if userid in self._users:
            user = self._users[userid]
            return user.has_role(role)
        return False
