from flask import Flask, request
from flask_cors import CORS
from retrieval import returnToUser
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
        
        return data_form_user

if __name__ == "__main__":
    app.run(debug=True)