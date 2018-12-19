from .cloudcms_object import CloudCMSObject
from .branch import Branch

class Repository(CloudCMSObject):

    def __init__(self, client, data):
        super(Repository, self).__init__(client, data)

        self.platform_id = data['platformId']
        self.repository_url = client.config.base_url + '/repositories/' + self._doc

    def list_branches(self):
        url = self.repository_url + '/branches/'
        res = self.client.get(url)
        return Branch.branch_map(self, res['rows'])

    def read_branch(self, branch_id):
        url = self.repository_url + '/branches/' + branch_id
        res = self.client.get(url)
        return Branch(self, res)
