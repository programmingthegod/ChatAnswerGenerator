from flask import Flask, render_template, request, jsonify
from model.model import answer_generator

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    question = request.form.get('question')
    context = request.form.get('context')

    answer = answer_generator.generate_answer(question, context)

    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
