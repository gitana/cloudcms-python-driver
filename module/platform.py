from .cloudcms_object import CloudCMSObject
from .repository import Repository

class Platform(CloudCMSObject):

    def __init__(self, client, data):
        super(Platform, self).__init__(client, data)

        self.base_url = client.config.base_url

    def list_repositories(self):
        return self.client.get(self.base_url + '/repositories')['rows']

    def read_repository(self, repository_id):
        res = self.client.get(self.base_url + '/repositories/' + repository_id)
        return Repository(self.client, res)