# 🧑‍⚖️ AI-Powered LegalBot 

This project is an AI chatbot that answers legal questions based on actual legal documents. It goes beyond simple keyword-matching by using **OpenAI embeddings**, **LangChain**, and **FAISS** for retrieval-based question answering.

## 🚀 Features
- 🗂 Document indexing with vector embeddings
- 🤖 Intelligent Q&A using OpenAI's LLMs
- 📄 PDF and TXT file support
- 🌐 REST API using Flask
- 💾 FAISS vector store for fast similarity search
- 🔐 API key stored securely using `.env`
- 🧪 Easily extensible and testable

## 📁 Folder Structure
legalbot/
│
├── app.py # Flask API to handle incoming questions
├── build_index.py # Indexes documents into FAISS vector store
├── data/ # Folder to store legal PDFs or .txt files
├── faiss_index/ # Saved FAISS vector database
├── templates/ # HTML files (UI)
│ └── index.html
├── static/ # CSS or JS files
│ └── style.css
├── .env # Stores your OpenAI API key
├── requirements.txt # Project dependencies
└── README.md # This file

## 🔧 Setup Instructions
1. Clone the repo
    ```bash
    git clone https://github.com/yourusername/legalbot.git
    cd legalbot
2. Create a virtual environment
    python -m venv venv
    source venv/bin/activate
3. Install dependencies
    pip install -r requirements.txt
4. Create your .env file
    OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx

## Disclaimer
This tool is for **informational purposes only** and does **not** provide legal advice.

## License
MIT License. Free to use, modify, and distribute.

## Acknowledgements
[LangChain FAISS](https://python.langchain.com/docs/integrations/vectorstores/faiss/)
[OpenAI Vector Embeddings](https://platform.openai.com/docs/guides/embeddings?lang=python)
[PyMuPDF Basics](https://pymupdf.readthedocs.io/en/latest/the-basics.html)
[python-dotenv](https://pypi.org/project/python-dotenv/)
