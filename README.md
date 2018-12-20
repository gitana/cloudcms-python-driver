# Cloud CMS Python Driver

Basic driver for the [Cloud CMS](https://www.cloudcms.com) API

Runs with Python 3

Currently supports the following functionality:
- Connect to and refresh access tokens with the API
- Read platform, branch, and repositories
- Read, query, search, create, update, and delete nodes

To install, run `pip install cloudcms`

Simple example:
```python
from cloudcms import CloudCMS
import os

# Needed when using http
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# Connect to Cloud CMS
client = CloudCMS()
platform = client.connect(filename="gitana.json")

# List repositories
repositories = platform.list_repositories()

# Read repository
repository = platform.read_repository('<repository_id>')

# List branches
branches = repository.list_branches()

# Read branch
branch = repository.read_branch('<branch_id>')

# Read Node
node = branch.read_node('<node_id>')

# Create node
obj = {
    'title': 'Twelfth Night',
    'description': 'An old play'
}
nodeId = branch.create_node(obj)

# Query nodes
query = {
    '_type': 'store:book'
}
pagination = {
    'limit': 2
}
queried_nodes = branch.query_nodes(query, pagination)

# Search/Find nodes
find = {
    'search': 'Shakespeare',
    'query': {
        '_type': 'store:book'
    }
}
searched_nodes = branch.find_nodes(find)
```