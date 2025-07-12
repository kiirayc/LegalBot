import json
from fuzzywuzzy import process
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

with open('data/legal_qa.json') as f:
    LEGAL_QA = json.load(f)

# A route is a URL path that your web app listens to and responds when someone visits or sends a request to it
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form.get('question', '').strip()
    normalized_question = question.strip().lower()

    best_mathch, score = process.extractOne(normalized_question, LEGAL_QA.keys())

    if score > 90:
        answer = LEGAL_QA[best_mathch]
    else:
        answer = "Sorry, I don't have an answer for that."

    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
