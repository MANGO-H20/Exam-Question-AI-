
import os 
import pymongo
from pymongo.operations import SearchIndexModel
import time 

uri = os.getenv('mongo_pass')
client = pymongo.MongoClient(uri)
db = client['exam-papers']
collection = db['exam-papers']

index_name="try-13"
def createIndex(index_name):
    search_index_model = SearchIndexModel(
    definition = {
        "fields": [
        {
            "type": "vector",
            "numDimensions": 768,
            "path": "embedding",
            "similarity": "cosine"
        },
        {
            "type": "filter",
            "path": "metadata.level",  
        },
        {
            "type": "filter",
            "path": "metadata.subject",
        },
        {
            "type": "filter",
            "path": "metadata.board",
        },
        {
            "type": "filter",
            "path": "metadata.markscheme"
        }

        ]
    },
    name = index_name,
    type = "vectorSearch"
    )
    collection.create_search_index(model=search_index_model)
    # Wait for initial sync to complete
    print("Polling to check if the index is ready. This may take up to a minute.")
    predicate=None
    if predicate is None:
        predicate = lambda index: index.get("queryable") is True
    while True:
        indices = list(collection.list_search_indexes(index_name))
        if len(indices) and predicate(indices[0]):
            break
        time.sleep(5)
    print(index_name + " is ready for querying.")