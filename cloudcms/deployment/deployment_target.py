from collections import OrderedDict
from ..platform import CloudCMSObject

class DeploymentTarget(CloudCMSObject):

    def __init__(self, client, data):
        super(DeploymentTarget, self).__init__(client, data)

    def uri(self):
        return '/deployment/targets/' + self._doc
    
    @classmethod
    def deployment_target_map(cls, client, data):
        return OrderedDict((deployment_target['_doc'], DeploymentTarget(client, deployment_target)) for deployment_target in data)