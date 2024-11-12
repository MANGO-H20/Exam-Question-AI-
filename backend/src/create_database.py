import os
from typing import List 
import pymongo
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
# Step 1 : Insert pdfs into mongo db database with tags 
# Connect database
uri = os.getenv('mongo_pass')

client = pymongo.MongoClient(uri)
db = client['exam-papers']
collection = db['exam-papers']

exam_paper_folder =  "WebScraper"
#get data from 
metadata = {
    "level": "GCSE",
    "subject": "",
    "markscheme":False,
    "board": "AQA"
}
subjects = [
"Chemistry",
"EnglishLanguage",
"EnglishLiterature",
"Maths",
"Physics",
"FutherMaths",
"Biology",
"A-levelBiology",
"A-levelChemistry",
"A-levelEconomics",
"A-levelMaths",
"A-levelPhysics",
]

marks = [
    "[1 Mark]", "[2 Marks]", "[3 Marks]", "[4 Marks]", "[5 Marks]", "[6 Marks]", "[7 Marks]", 
    "[8 Marks]", "[9 Marks]", "[10 Marks]", "[11 Marks]", "[12 Marks]", "[13 Marks]", 
    "[14 Marks]", "[15 Marks]", "[16 Marks]", "[17 Marks]", "[18 Marks]", "[19 Marks]", 
    "[20 Marks]", "[21 Marks]", "[22 Marks]", "[23 Marks]", "[24 Marks]", "[25 Marks]", 
    "[26 Marks]", "[27 Marks]", "[28 Marks]", "[29 Marks]", "[30 Marks]", "[31 Marks]", 
    "[32 Marks]", "[33 Marks]", "[34 Marks]", "[35 Marks]", "[36 Marks]", "[37 Marks]", 
    "[38 Marks]", "[39 Marks]", "[40 Marks]"
]
    
model = SentenceTransformer("nomic-ai/nomic-embed-text-v1", trust_remote_code=True)
# Define a function to generate embeddings
def get_embedding(data):
    """Generates vector embeddings for the given data."""
    embedding = model.encode(data)
    return embedding.tolist()

class QuestionSplitter(RecursiveCharacterTextSplitter):
    def __init__(self, **kwargs: any) -> None:
        separators = marks
        super().__init__(separators=separators, **kwargs)

question_splitter = QuestionSplitter()
markshceme_splitter = RecursiveCharacterTextSplitter(chunk_size = 500)

# Setting up metadata for the document

def addfiles():
    count = 0
    for path,folders,files in os.walk(exam_paper_folder):
        for file in files:
            if "Alevel" in path:
                metadata["level"] = "A-level"  
            for subject in subjects:
                if subject in path:
                    metadata["subject"] = subject 
            if "MS" in file:
                metadata["markscheme"] = True
            else:
                metadata["markscheme"] = False
            loader = PyPDFLoader(path + "\\" + file)
            pdf_doc = loader.load()
            for pdf_page in pdf_doc:
                starting_metadata = pdf_page.metadata
                combined_metadata = dict(starting_metadata, **metadata)
                pdf_page.metadata = combined_metadata
            if metadata["markscheme"] == False:
                documents = question_splitter.split_documents(pdf_doc) 
            else:
                documents = markshceme_splitter.split_documents(pdf_doc) 
            # Prepare documents for insertion
            docs_to_insert = [{
                "text": doc.page_content,
                "embedding": get_embedding(doc.page_content),
                "metadata": doc.metadata,
            } for doc in documents]
            result = collection.insert_many(docs_to_insert) 
            count += 1 
            print(str(count) + " " +metadata["subject"] + " " + metadata["markscheme"] )

addfiles()