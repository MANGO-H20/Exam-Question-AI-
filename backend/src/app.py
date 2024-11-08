from flask import Flask, request, jsonify
from flask_cors import CORS
from query_AI import query_AI
app = Flask(__name__)

CORS(app) 
data_form_user = {}
@app.route('/',methods=['POST'])
def new_exam_question():
    if request.method == 'POST':
        message = request.form['message']
        subject = request.form['subject']
        level = request.form['level']
        board = request.form['board']
        data_form_user = {
            "message":message,
            "subject": subject,
            "level": level,
            "board": board,
                }
        #relevant_docs = returnToUser(data_form_user)
        question_answer = query_AI(data_form_user) 
        return jsonify(question_answer)

if __name__ == "__main__":
    app.run(debug=True)