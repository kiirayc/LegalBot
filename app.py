import json
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
    answer = LEGAL_QA.get(question, "Sorry, I don't have an answer for that.")
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
