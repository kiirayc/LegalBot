from flask import Flask, request, jsonify
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.embeddings import OpenAIEmbeddings

load_dotenv()

app = Flask(__name__)

# Loads the saved vector database from disk to answer questions at runtime
embedding = OpenAIEmbeddings()
db = FAISS.load_local("faiss_index", embedding)
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(),
    retriever=db.as_retriever()
)

@app.route("/ask", methods=["POST"])
def ask():
    question = request.json["question"]
    answer = qa_chain.run(question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
