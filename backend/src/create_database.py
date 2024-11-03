import os 
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
"History",
"Maths",
"Physics",
"FutherMaths",
"Biology"
"A-levelBiology",
"A-levelChemistry",
"A-levelEconomics",
"A-levelMaths",
"A-levelHistory",
"A-levelPhysics",
]
model = SentenceTransformer("nomic-ai/nomic-embed-text-v1", trust_remote_code=True)
    
# Define a function to generate embeddings
def get_embedding(data):
    """Generates vector embeddings for the given data."""
    embedding = model.encode(data)
    return embedding.tolist()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=20)

# Setting up metadata for the document
def addfiles():
    for path,folders,files in os.walk(exam_paper_folder):
        for file in files:
            if "Alevel" in path:
                metadata["level"] = "A-level"  
            for subject in subjects:
                if subject in path:
                    metadata["subject"] = subject 
            if "MS" in file:
                metadata["markscheme"] = True
            loader = PyPDFLoader(path + "\\" + file)
            pdf_doc = loader.load()
            for pdf_page in pdf_doc:
                starting_metadata = pdf_page.metadata
                combined_metadata = dict(starting_metadata, **metadata)
                pdf_page.metadata = combined_metadata
            documents = text_splitter.split_documents(pdf_doc)
            # Prepare documents for insertion
            docs_to_insert = [{
                "text": doc.page_content,
                "embedding": get_embedding(doc.page_content),
                "metadata": doc.metadata,
            } for doc in documents]
            result = collection.insert_many(docs_to_insert)

