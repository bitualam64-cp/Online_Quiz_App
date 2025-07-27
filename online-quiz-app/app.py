import json
import random
from flask import Flask, render_template, request

app = Flask(__name__)

def load_questions():
    with open('questions.json', 'r') as f:
        questions = json.load(f)
        random.shuffle(questions)
        return questions[:5]  # Limit to 5 questions per quiz attempt

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    questions = load_questions()
    return render_template('quiz.html', questions=questions)

@app.route('/result', methods=['POST'])
def result():
    with open('questions.json', 'r') as f:
        all_questions = json.load(f)

    score = 0
    total = 0

    for q in all_questions:
        user_answer = request.form.get(q["question"])
        if user_answer:
            total += 1
            if user_answer == q["answer"]:
                score += 1

    return render_template('result.html', score=score, total=total)

if __name__ == '__main__':
    app.run(debug=True)
