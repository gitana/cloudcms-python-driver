import json
from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session

from .connectionConfig import ConnectionConfig
from .platform import Platform

class CloudCMS:

    def __init__(self):
        pass

    def connect(self, **kwargs):
        if 'filename' in kwargs:
            with open(kwargs['filename']) as f:
                data = json.load(f)
                self.config = ConnectionConfig(data)
        else:
            self.config = ConnectionConfig(kwargs)

        def token_updater(token):
            self.oauth_client.token = token

        self.oauth_client = OAuth2Session(client=LegacyApplicationClient(client_id=self.config.client_id),
                                auto_refresh_kwargs=self.config.extra(),
                                auto_refresh_url=self.config.token_url,
                                token_updater=token_updater)

        self.oauth_client.token = self.oauth_client.fetch_token(token_url=self.config.token_url,
                                username=self.config.username,
                                password=self.config.password,
                                client_id=self.config.client_id,
                                client_secret=self.config.client_secret)

        return self.get_platform()

        
    def get(self, url, params={}):
        return self.request('GET', url, params)

    def post(self, url, params={}, data={}):
        return self.request('POST', url, params, data)

    def request(self, method, url, params={}, data={}):
        # Add "full" to params if not there
        if not 'full' in params:
            params['full'] = True

        # Convert param values to json
        paramsJson = {key: json.dumps(param) for (key, param) in params.items()}        

        res = self.oauth_client.request(method, url, json=data, params=paramsJson).json()
        if 'error' in res and res['error']:
            raise RuntimeError(res['message'])

        return res

    def get_platform(self):
        data = self.get(self.config.base_url)
        return Platform(self, data)
