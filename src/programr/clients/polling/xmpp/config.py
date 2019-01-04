from programr.config.client.config import ClientConfigurationData


class XmppConfiguration(ClientConfigurationData):

    def __init__(self):
        ClientConfigurationData.__init__(self, "xmpp")
        self._server = None
        self._port = 5222
        self._xep_0030 = False
        self._xep_0004 = False
        self._xep_0060 = False
        self._xep_0199 = False

    @property
    def server(self):
        return self._server

    @property
    def port(self):
        return self._port

    @property
    def xep_0030(self):
        return self._xep_0030

    @property
    def xep_0004(self):
        return self._xep_0004

    @property
    def xep_0060(self):
        return self._xep_0060

    @property
    def xep_0199(self):
        return self._xep_0199

    def load_configuration(self, configuration_file, bot_root):
        xmpp = configuration_file.get_section(self.section_name)
        if xmpp is not None:
            self._server = configuration_file.get_option(xmpp, "server")
            self._port = configuration_file.get_int_option(xmpp, "port", missing_value=5222)
            self._xep_0030 = configuration_file.get_bool_option(xmpp, "xep_0030")
            self._xep_0004 = configuration_file.get_bool_option(xmpp, "xep_0004")
            self._xep_0060 = configuration_file.get_bool_option(xmpp, "xep_0060")
            self._xep_0199 = configuration_file.get_bool_option(xmpp, "xep_0199")
        super(XmppConfiguration, self).load_configuration(configuration_file, xmpp, bot_root)

    def to_yaml(self, data, defaults=True):
        if defaults is True:
            data['server'] = "talk.google.com"
            data['port'] = 5222
            data['xep_0030'] = True
            data['xep_0004'] = True
            data['xep_0060'] = True
            data['xep_0199'] = True
        else:
            data['server'] = self._server
            data['port'] = self._port
            data['xep_0030'] = self._xep_0030
            data['xep_0004'] = self._xep_0004
            data['xep_0060'] = self._xep_0060
            data['xep_0199'] = self._xep_0199

        super(XmppConfiguration, self).to_yaml(data, defaults)