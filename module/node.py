from .repository_object import RepositoryObject

class Node(RepositoryObject):
    pass



    @classmethod
    def node_map(cls, repository, data):
        return {node['doc']: Node(repository, node) for node in data}