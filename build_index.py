from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv
import os

# Loads the .env file
load_dotenv()

data_folder = "data/"
all_docs = []

for filename in os.listdir(data_folder):
    if filename.endswith((".pdf", ".txt")):
        filepath = os.path.join(data_folder, filename)
        # Creates a loader to extract texts from the files
        loader = PyMuPDFLoader(filepath)
        # Returns a list of Document objects
        docs = loader.load() # Actually reads the file
        all_docs.extend(docs)

# Break documents into smaller tokens
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50) # Overlap is for keeping track of the chunks
# Loops internally, break each into chunks, returns a new list
chunks = splitter.split_documents(all_docs)

# Create embeddings and vector store
embedding = OpenAIEmbeddings() # Initializes OpenAI's embedding model
db = FAISS.from_documents(chunks, embedding) # Creates a searchable FAISS database from all chunks
# Semantic search is now possible with vector embeddings
db.save_local("faiss_index")

print("✅ FAISS index created and saved.")
