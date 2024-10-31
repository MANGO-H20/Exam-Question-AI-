import os 
import pymongo
# Step 1 : Insert pdfs into mongo db database with tags 
# Connect database
uri = os.getenv('mongo_pass')

client = pymongo.MongoClient(uri)
db = client['exam-papers']
collection = db['exam-papers']

exam_paper_folder =  "WebScraper"

# Setting up metadata for the document
for path,folders,files in os.walk(exam_paper_folder):
    print(path)
    print(folders)
    print(files)

