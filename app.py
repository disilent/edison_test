from flask import  Flask, render_template, request, redirect, url_for, flash, make_response, session, g
from psychics import Psychics

app = Flask(__name__)
app.config['SECRET_KEY'] = b"\xba\x003\xd0\x8f\xb3\xf3\xcf\xab\x1f\xf9Q\x8c\xff \x9a''\xd3\x0c \xed\xed\xed"
session_psychics = []

def get_psychics():
    if not 'psychics' in session or len(session_psychics) <= session.get('psychics'):
        session['psychics'] = len(session_psychics)
        session_psychics.append(Psychics(2))

    return session_psychics[session.get('psychics')]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ready')
def ready():
    psychics = get_psychics()
    psychics.generate_numbers()

    numbers = psychics.get_numbers()
    trusts  = psychics.get_trusts()

    return render_template('ready.html', numbers=numbers, trusts=trusts)

@app.route('/check', methods=['POST'])
def check():
    psychics = get_psychics()
    answer = int(request.form['answer'])
    
    if psychics.get_numbers()[0] == 0:
        psychics.generate_numbers()

    psychics.check_answer(answer)

    numbers = psychics.get_numbers()
    trusts  = psychics.get_trusts()

    return render_template('check.html', numbers=numbers, trusts=trusts, answer=answer)

@app.route('/history')
def history():
    psychics = get_psychics()
    history, answers = psychics.get_history()
    count = psychics.get_count()
    return render_template('history.html', history=history, answers=answers, count=count)

if __name__ == "__main__":
    app.run()
