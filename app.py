import ast
import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_marshmallow import Marshmallow
import os
import pyodbc
import sqlite3
import json




app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@localhost/testing'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Question(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String, nullable=False)
    answer = db.Column(db.String, nullable=False, primary_key=True)

def __init__(self , question, answer):
    #self.id = id
    self.question = question
    self.answer = answer
    #self.response = response

class AnswerSchema(ma.Schema):
    class Meta:
        fields = ("question", "answer")

#question_schema =QuestionSchema()
answers_schema = AnswerSchema(many=True)
answer_schema = AnswerSchema()



@app.route('/admin/user=mikkel/pwd=123456', methods=['GET', 'POST'])
def admin():
    if(request.method=='POST'):
        question_ = request.form.get('question')
        answer = request.form.get('answer')
        entry = Question(question=question_, answer=answer)
        db.session.add(entry)
        db.session.commit()
    return render_template("index.html")

@app.route('/api/choice/<answer>', methods=['GET','POST'])
def choice_api(answer):
    """
    for all entry
    #all_question = question.query.all()
    #result = question_schema.dump(all_question)
    # return jsonify(result)
    """
    """
    for single entry result
    """
    if (request.method == 'POST', 'GET'):
        answer = request.form.get('answer')
        all_answer = Question.query.get(answer)
        result = answer_schema.dump(all_answer)

    #choice making

        all_ques = Question.query.all()
        res = answers_schema.dump(all_ques)
        if result in res:
            """
            red = {
                "Answer": answer,
                "Choice": "Correct answer"

            }
            """
            return render_template('home.html', red='Your answer is correct')
        else:
            return render_template('home.html', red='Your answer is not correct')
            """
            red = {
                "Answer": answer,
                "Choice": "Wrong answer"

            }
            """


        #return jsonify(red)

#fetch all data from database and print random data
@app.route('/home', methods=['GET', 'POST', 'PUT'])
def random_api():
    if (request.method == 'GET', 'POST', 'PUT'):
        all_data = Question.query.all()
        res = answers_schema.dump(all_data)
        random_val = random.choice(res)
        question_print = random_val.get('question')
        #return question_print
        return render_template('home.html', rad=question_print)





















if __name__ == '__main__':

    app.run(debug=True)

