from programy.clients.restful.config import RestConfiguration


class WebChatConfiguration(RestConfiguration):

    def __init__(self):
        RestConfiguration.__init__(self, "webchat")
        self._cookie_id = "ProgramYSession"
        self._cookie_expires = 90

    @property
    def cookie_id(self):
        return self._cookie_id

    @property
    def cookie_expires(self):
        return self._cookie_expires

    def load_configuration(self, configuration_file, bot_root):
        webchat = configuration_file.get_section(self.section_name)
        if webchat is not None:
            self._cookie_id = configuration_file.get_option(webchat, "cookie_id", missing_value="ProgramYSession")
            self._cookie_expires = configuration_file.get_int_option(webchat, "cookie_expires", missing_value=90)
        super(WebChatConfiguration, self).load_configuration(configuration_file, bot_root)

    def to_yaml(self, data, defaults=True):
        if defaults is True:
            data['cookie_id'] = "ProgramYSession"
            data['cookie_expires'] = 90
        else:
            data['cookie_id'] = self._cookie_id
            data['cookie_expires'] = self._cookie_expires

        super(WebChatConfiguration, self).to_yaml(data, defaults)