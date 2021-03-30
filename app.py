from flask import  Flask, render_template, request, redirect, url_for, flash, make_response, session, g
from psychic import Psychic

app = Flask(__name__)
app.config['SECRET_KEY'] = b"\xba\x003\xd0\x8f\xb3\xf3\xcf\xab\x1f\xf9Q\x8c\xff \x9a''\xd3\x0c \xed\xed\xed"
psychics = []

def get_psychics():
    if not 'psychic' in session or len(psychics) <= session.get('psychic'):
        session['psychic'] = len(psychics)
        psychics.append(Psychic(2))

    return psychics[session.get('psychic')]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ready')
def ready():
    psychic = get_psychics()
    psychic.generate_numbers()

    numbers = psychic.get_numbers()
    trusts  = psychic.get_trusts()

    return render_template('ready.html', numbers=numbers, trusts=trusts)

@app.route('/check', methods=['POST'])
def check():
    psychic = get_psychics()
    answer = int(request.form['answer'])
    
    if psychic.get_numbers()[0] == 0:
        psychic.generate_numbers()

    psychic.check_answer(answer)

    numbers = psychic.get_numbers()
    trusts  = psychic.get_trusts()

    return render_template('check.html', numbers=numbers, trusts=trusts, answer=answer)

if __name__ == "__main__":
    app.run()
