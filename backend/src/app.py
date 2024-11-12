from flask import Flask, request, jsonify
from flask_cors import CORS
from query_AI import query_AI
app = Flask(__name__)

CORS(app) 
@app.route('/',methods=['POST'])
def new_exam_question():
    if request.method == 'POST':
        #gets data of user from webpage
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
        question_answer = query_AI(data_form_user) #returns question
        return jsonify(question_answer) #returns json file

#set contasnt loop
if __name__ == "__main__":
    app.run(debug=True)