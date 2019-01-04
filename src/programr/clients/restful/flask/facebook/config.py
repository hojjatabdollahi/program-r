from programr.clients.restful.config import RestConfiguration


class FacebookConfiguration(RestConfiguration):
    
    def __init__(self):
        RestConfiguration.__init__(self, "facebook")

    def to_yaml(self, data, defaults=True):
        super(FacebookConfiguration, self).to_yaml(data, defaults)