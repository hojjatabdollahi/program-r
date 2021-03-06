from programr.utils.logging.ylogger import YLogger

from programr.config.section import BaseSectionConfigurationData


class BrainSecurityConfiguration(BaseSectionConfigurationData):

    DEFAULT_ACCESS_DENIED = "Access denied!"

    def __init__(self, service_name):
        BaseSectionConfigurationData.__init__(self, service_name)
        self._classname = None
        self._denied_srai = None
        self._denied_text = None

    @property
    def classname(self):
        return self._classname

    @property
    def denied_srai(self):
        return self._denied_srai

    @property
    def denied_text(self):
        return self._denied_text

    def load_config_section(self, configuration_file, configuration, bot_root):
        service = configuration_file.get_section(self.section_name, configuration)
        if service is not None:
            self._classname = configuration_file.get_option(service, "classname", missing_value=None)
            self._denied_srai = configuration_file.get_option(service, "denied_srai", missing_value=None)
            self._denied_text = configuration_file.get_option(service, "denied_text", missing_value=BrainSecurityConfiguration.DEFAULT_ACCESS_DENIED)
        else:
            YLogger.warning(self, "'security' section missing from bot config, using to defaults")


class BrainSecurityAuthenticationConfiguration(BrainSecurityConfiguration):

    def __init__(self, service_name="authentication"):
        BrainSecurityConfiguration.__init__(self, service_name)

    def to_yaml(self, data, defaults=True):
        if defaults is True:
            data['classname'] = "programr.security.authenticate.passthrough.BasicPassThroughAuthenticationService"
            data['denied_srai'] = "AUTHENTICATION_FAILED"
            data['denied_text'] = "Access Denied!"
        else:
            data['classname'] = self._classname
            data['denied_srai'] = self._denied_srai
            data['denied_text'] = self._denied_text


class BrainSecurityAuthorisationConfiguration(BrainSecurityConfiguration):

    def __init__(self, service_name="authorisation"):
        BrainSecurityConfiguration.__init__(self, service_name)
        self._usergroups = None

    @property
    def usergroups(self):
        return self._usergroups

    def load_config_section(self, configuration_file, configuration, bot_root):
        super(BrainSecurityAuthorisationConfiguration, self).load_config_section(configuration_file, configuration, bot_root)
        service = configuration_file.get_section(self.section_name, configuration)
        if service is not None:
            usergroups = configuration_file.get_option(service, "usergroups", missing_value=None)
            if usergroups is not None:
                self._usergroups = self.sub_bot_root(usergroups, bot_root)
            self.load_additional_key_values(configuration_file, service)

    def to_yaml(self, data, defaults=True):
        if defaults is True:
            data['classname'] = "programr.security.authorise.usergroupsauthorisor.BasicUserGroupAuthorisationService"
            data['denied_srai'] = "AUTHORISATION_FAILED"
            data['denied_text'] = "Access Denied!"
            data['usergroups'] = './config/usergroups.txt'
        else:
            data['classname'] = self._classname
            data['denied_srai'] = self._denied_srai
            data['denied_text'] = self._denied_text
            data['usergroups'] = self._usergroups
