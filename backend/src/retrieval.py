import os 
import pymongo
import time 
from sentence_transformers import SentenceTransformer
uri = os.getenv('mongo_pass')

client = pymongo.MongoClient(uri)
db = client['exam-papers']
collection = db['exam-papers']

model = SentenceTransformer("nomic-ai/nomic-embed-text-v1", trust_remote_code=True)    
# Define a function to generate embeddings
def get_embedding(data):
    """Generates vector embeddings for the given data."""
    embedding = model.encode(data)
    return embedding.tolist()
#Create index model with filters 
index_name="try-13"

#function will query database from requirments specified
def get_query_results(query):
    """Gets results from a vector search query."""
    query_embedding = get_embedding(query["message"])
    vector_pipeline = [
        {
                "$vectorSearch": {
                "index": index_name,
                "queryVector": query_embedding,
                "path": "embedding",
                "exact": True,
                "limit": 9,  

                
                "filter": {
                    "$and":[
                        {
                            "metadata.subject": query["subject"],
                            "metadata.board": query["board"],
                            "metadata.level": query["level"],
                            "metadata.markscheme": False
                        }
                    ]
                    
                }
                },
        }, 
        {
                "$project": {
                "_id": 0,
                "text": 1,
                "metadata": 1
            }
        }
    ]

    #filter documents in the database that meet requirments from filter
    results_vector = collection.aggregate(vector_pipeline)
    array_of_results = []

    #loops through all doccuments and appends them to the list
    for doc in results_vector:
        array_of_results.append(doc)
    return array_of_results


