from programr.config.client.config import ClientConfigurationData


class TelegramConfiguration(ClientConfigurationData):

    def __init__(self):
        ClientConfigurationData.__init__(self, "telegram")
        self._unknown_command = None
        self._unknown_command_srai = None

    @property
    def unknown_command(self):
        return self._unknown_command

    @property
    def unknown_command_srai(self):
        return self._unknown_command_srai

    def load_configuration(self, configuration_file, bot_root):
        telegram = configuration_file.get_section(self.section_name)
        if telegram is not None:
            self._unknown_command = configuration_file.get_option(telegram, "unknown_command", missing_value="Unknown command")
            self._unknown_command_srai = configuration_file.get_option(telegram, "unknown_command_srai", missing_value=None)
        super(TelegramConfiguration, self).load_configuration(configuration_file, telegram, bot_root)

    def to_yaml(self, data, defaults=True):
        if defaults is True:
            data['unknown_command'] = "Sorry, that is not a command I have been taught yet!"
            data['unknown_command_srai'] = 'YTELEGRAM_UNKNOWN_COMMAND'
        else:
            data['unknown_command'] = self._unknown_command
            data['unknown_command_srai'] = self._unknown_command_srai

        super(TelegramConfiguration, self).to_yaml(data, defaults)