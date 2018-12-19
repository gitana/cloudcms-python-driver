import json
from .repository_object import RepositoryObject
from .node import Node

class Branch(RepositoryObject):

    def __init__(self, repository, data):
        super(Branch, self).__init__(repository, data)
        self.branch_url = '%s/branches/%s' % (self.repository_url, self._doc) 

    def read_node(self, node_id):
        url = self.branch_url + "/nodes/" + node_id
        res = self.client.get(url)

        return Node(self.repository, res)
    
    def query_nodes(self, query, pagination={}):
        url = self.branch_url + "/nodes/query"

        res = self.client.post(url, params=pagination, data=query)
        return Node.node_map(self.repository, res['rows'])

    def search_nodes(self, search, pagination={}):
        url = self.branch_url + "/nodes/search"

        res = self.client.post(url, params=pagination, data=search)
        return Node.node_map(self.repository, res['rows'])

    def create_node(self, obj, options):
        url = self.branch_url + "/nodes"

        params = {}
        params['rootNodeId'] = options.get('rootNodeId') or 'root'
        params['associationType'] = options.get('associationType') or 'a:child'

        if 'parentFolderPath' in options:
            params['parentFolderPath'] = options['parentFolderPath']
        elif 'folderPath' in options:
            params['parentFolderPath'] = options['folderPath']
        elif 'folderpath' in options:
            params['parentFolderPath'] = options['folderpath']  
        
        if 'filePath' in options:
            params['filePath'] = options['filePath']
        elif 'filepath' in options:
            params['filePath'] = options['filepath']

        res = self.client.post(url, params=params, data=obj)
        print(res)
        return res['_doc']


    @classmethod
    def branch_map(repository, data):
        return {branch['_doc']: Branch(repository, branch) for branch in data}