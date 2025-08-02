from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_community.vectorstores import FAISS
# Combines a retriever (FAISS) and a language model (OpenAI)
from langchain.chains import RetrievalQA
from langchain_openai import OpenAIEmbeddings

# Load environmental variables e.g. OPENAI_API_KEY from a .env file
# OpenAIEmbeddings() and ChatOpenAI() automatically grab the key
load_dotenv() # Ensure API keys are not hardcoded

# Core object running the server
app = Flask(__name__)

# Loads the saved vector database from disk to answer questions at runtime
embedding = OpenAIEmbeddings() # Create embeddings (a tool for vector representations of text)
# Loads the saved FAISS database with the same embedding object
# Loads docstore (original documents) and index_to_docstore_id
db = FAISS.load_local("faiss_index", embedding, allow_dangerous_deserialization=True)

# Creates a RetrievalQA chain: Retrieves relevant documents from db using retriever,
# Passes the documents and user questions to llm 
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(), # A wrapper for OpenAI’s GPT model
    retriever=db.as_retriever()
)

# API route to Flask app
@app.route('/') # Route decorator that runs the function below if someone accesses the root URL
def home():
    return render_template('index.html')

@app.route("/ask", methods=["POST"])
def ask():
    # Provides the parsed JSON data as a Python dictionary
    question = request.json["question"] # Access by keys
    # (1) The query is used to retrieve information from the vector store, 
    # using the retriever component within the chain
    # (2) The retrieved information along with the query is formatted into a prompt
    # that provides context for a LLM 
    # (3) The prompts are passed to a LLM which generates an answer
    answer = qa_chain.run(question)
    # JSON serialization, automatically sets the Content-Type to application/json
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
