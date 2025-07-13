import json
import re
from fuzzywuzzy import fuzz, process
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

with open('data/legal_qa.json') as f:
    LEGAL_QA = json.load(f)

SYNONYMS = {
    "officer": ["cop", "police"],
    "police": ["cop", "officer"],
    "immigration": ["ice", "border patrol"],
    "stopped": ["pulled over", "detained", "held up"],
    "document": ["papers", "id", "identification"],
    "rights": ["legal rights", "protections"]
}

def apply_synonyms(text):
    for keyword, synonyms in SYNONYMS.items():
        for syn in synonyms:
            # Replace synonyms with the main keyword
            pattern = r'\b' + re.escape(syn) + r'\b'
            text = re.sub(pattern, keyword, text)
    return text

def normalize_input(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s]', '', text) # remove punctuation
    text = re.sub(r'\s+', ' ', text)
    text = apply_synonyms(text) # apply synonym replacement
    return text

# A route is a URL path that your web app listens to and responds when someone visits or sends a request to it
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form.get('question', '').strip()
    normalized_question = normalize_input(question)

    # Ignores word order and duplicates
    best_match, score = process.extractOne(normalized_question, LEGAL_QA.keys(), scorer=fuzz.token_set_ratio)

    print(f"User asked: {normalized_question}")
    print(f"Top match: {best_match} (Score: {score})")

    if score > 85:
        answer = LEGAL_QA[best_match]
    else:
        answer = "Sorry, I don't have an answer for that."

    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
