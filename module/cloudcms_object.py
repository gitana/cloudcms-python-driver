class CloudCMSObject:
    
    def __init__(self, client, data):
        self.client = client
        self._doc = data['_doc']
        self.base_url = client.config.base_url

        self.data = data

    