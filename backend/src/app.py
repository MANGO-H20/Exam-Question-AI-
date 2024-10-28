from flask import Flask, request

app = Flask(__name__)


@app.route('/new_exam_question',method=['POST'])
def new_exam_question():
    if request.method == 'POST':
        message = request.form['message']
        subject = request.form['subject']
        level = request.form['level']
        board = request.form['board']
