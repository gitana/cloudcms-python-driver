from module import CloudCMS
import os

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

client = CloudCMS()
platform = client.connect(filename="gitana.json")

repository = platform.read_repository('2e746f5ff87eb5b3508d')

branch = repository.read_branch('d107851fe8c4d19a99de')

query = {
    '$or': [
        {
            '_type': 'store:book'
        }
    ]
}
pagination = {
    'limit': 2
}

nodes = branch.query_nodes(query)

print([node._doc for node in nodes.values()])

node = branch.read_node('4126317a8b4794de8c51')
print(node.data)

# print(platform.data)