import os
import random
import textwrap
from datetime import datetime

from flask import Flask, request, render_template, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#for local
app.config.from_object('config.BaseConfig')


#for Heroku
import os
# app.config.from_object(os.environ['APP_SETTINGS'])

#for local
# DEBUG = False
# SECRET_KEY = '\xc0\xc3\xe42\xb6\x0cl\x93\xfd\x8e\xfd(\xb7\x8de\x9an\x86\x19\xea\x87\xb5\x1f\xea'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///political_hangmanPSQL.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from models import *

alpl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '#', '&']

word_guess = []
turns = ()

# app = Flask(__name__)
# app.secret_key = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'


def get_phrase(session_id):

    phraseget = Sessions.query.filter_by(session_id=session_id).first()
    phrase = phraseget.phrase


    return phrase


def get_word_guess(session_id):

    word_guessget = Sessions.query.filter_by(session_id=session_id).first()
    word_guess = word_guessget.word_guess
    word_guess = list(word_guess)

    return word_guess


def get_alpl(session_id):

    alplget = Sessions.query.filter_by(session_id=session_id).first()
    alpl = alplget.alpl
    alpl = list(alpl)


    return alpl


def get_turns(session_id):

    turnsget = Sessions.query.filter_by(session_id=session_id).first()
    turns = turnsget.turns
    turns = int(turns)

    return turns


def get_politician(session_id):


    politicianget = Sessions.query.filter_by(session_id=session_id).first()
    politician = politicianget.politician

    return politician


@app.route('/', methods=['POST', 'GET'])
def Hangman():
    if request.method == 'GET':


        if 'user' in session:
            session['user'] = random.getrandbits(31)

        if 'user' not in session:
            session['user'] = random.getrandbits(31)

        def session_id_enter(session_ID):


            session_id = session_ID
            id_enter = Sessions(session_id=session_id, datestamp=None, politician=None, guess_phrase=None,
                                phrase=None, word_guess=None, turns=None, alpl=None)
            db.session.add(id_enter)
            db.session.commit()



        session_ID = session['user']
        session_id_enter(session_ID)

        return render_template('index.html')

    elif request.method == 'POST':

        return render_template('index.html')


@app.route('/indexPolChoice', methods=['POST', 'GET'])
def Politician_choice():

    if request.method == 'GET':



        return render_template('indexPolChoice.html')

    elif request.method == 'POST':


        politician = request.form['polititian']



        if 'user' not in session:
            session['user'] = random.getrandbits(31)
        session_ID = session['user']



        politician_name = politician

        tweet = tweets.query.filter_by(politician=politician_name).first()
        word = tweet.tweet
        screen = tweets.query.filter_by(politician=politician_name).first()
        screen_name = screen.screen_name
        print(screen_name)



        word_guess = []
        phrase = []

        for char in word:
            for l in alpl:
                if char == l:
                    word_guess.append('_')
                    phrase.append(l)

                    break

                if char == l.upper():
                    word_guess.append('_')
                    phrase.append(l.upper())
                    break

                if char == ' ':
                    word_guess.append(' ')
                    phrase.append(' ')
                    break


        phrase = ''.join(phrase)

        l = len(phrase)

        l = int(l / 10)

        if l >= 10:
            turns = 4
        if l <= 9 and l >= 7:
            turns = 5
        if l <= 6 and l >= 5:
            turns = 6
        if l <= 4 and l >= 3:
            turns = 7
        if l <= 2:
            turns = 8


        def session_info_enter(politician, word_guess, phrase, alpl, turns, session_ID):



            alpl = "".join(alpl)

            word_guess = ''.join(word_guess)

            session_id = session_ID
            sessioninfo = Sessions.query.filter_by(session_id=session_id).first()
            sessioninfo.politician = politician
            sessioninfo.word_guess = word_guess
            sessioninfo.phrase = phrase
            sessioninfo.alpl = alpl
            sessioninfo.turns = turns
            db.session.commit()

        session_info_enter(politician, word_guess, phrase, alpl, turns, session_ID)


        return redirect(url_for('Game', screen_name=screen_name))



@app.route('/About', methods=['GET'])
def About():
    if request.method == 'GET':


        def delete_db_session():


            if 'user' in session:
                session_ID = session['user']
                return session_ID

            session_id = session_ID
            deletesession = Sessions.query.filter_by(session_id=session_id).first()
            db.session.delete(deletesession)
            db.session.commit()


        delete_db_session()

        def dropsession():
            session.pop('user', None)

        dropsession()

        return render_template('About.html')


@app.route('/Game', methods=['POST', 'GET'])
def Game():
    if request.method == 'GET':


        session_id = session['user']

        phrase = get_phrase(session_id)
        word_guess = get_word_guess(session_id)
        alpl = get_alpl(session_id)
        turns = get_turns(session_id)
        politician = get_politician(session_id)


        joined_word = (''.join(word_guess))

        guess_phrase = textwrap.fill(joined_word, 20)

        guess_phrase = (' '.join(guess_phrase))


        remaining_letters = textwrap.fill(', '.join(alpl), 52)



        def session_info_enter(turns, guess_phrase, session_id):

            sessioninfo = Sessions.query.filter_by(session_id=session_id).first()
            sessioninfo.turns = turns
            sessioninfo.guess_phrase = guess_phrase
            db.session.commit()

        session_info_enter(turns, guess_phrase, session_id)

        guess_head = politician
        print(guess_head)




        screen = tweets.query.filter_by(politician=politician).first()
        screen_name = screen.screen_name

        return render_template('Game.html', guess_head=guess_head, turns=turns, guess_phrase=guess_phrase,
                               remaining_letters=remaining_letters, screen_name=screen_name)


    elif request.method == 'POST':


        session_id = session['user']

        phrase = get_phrase(session_id)
        word_guess = get_word_guess(session_id)
        alpl = get_alpl(session_id)
        turns = get_turns(session_id)
        politician = get_politician(session_id)


        guess_head =  politician
        message_line = ' '

        choice = request.form['Char_Choice']
        choice = choice.lower()

        if choice not in alpl:
            message_line = "That letter has already been chosen."

        compare = phrase.lower()
        if choice not in compare:
            message_line = 'That choice is not in the phrase'
            turns = (turns - 1)

        if choice == '@' or '#':
            for letter in range(len(phrase)):
                if choice == phrase[letter]:
                    word_guess[letter] = choice

        if str.isnumeric(choice):
            for letter in range(len(phrase)):
                if choice == phrase[letter]:
                    word_guess[letter] = choice
                elif ' ' == phrase[letter]:
                    word_guess[letter] = ' '

        if str.islower(choice):
            for letter in range(len(phrase)):
                if choice == phrase[letter]:
                    word_guess[letter] = choice
                elif ' ' == phrase[letter]:
                    word_guess[letter] = ' '

        if choice in alpl:
            alpl.remove(choice)

        remaining_letters = textwrap.fill(', '.join(alpl), 52)

        choice = choice.upper()

        if str.isupper(choice):
            for letter in range(len(phrase)):
                if choice == phrase[letter]:
                    word_guess[letter] = choice
                elif ' ' == phrase[letter]:
                    word_guess[letter] = ' '

        comp_word = ''.join(
            word_guess)  # creates an un-joined instance of the word to compare to the guess_word for a win

        if comp_word == phrase:



            def delete_db_session():

                if 'user' in session:
                    session_ID = session['user']
                    return session_ID
                session_id = session_ID
                deletesession = Sessions.query.filter_by(session_id=session_id).first()
                db.session.delete(deletesession)

            delete_db_session()

            def dropsession():
                session.pop('user', None)

            dropsession()

            return render_template('win.html', phrase=phrase)

        joined_word = (''.join(word_guess))

        guess_phrase = textwrap.fill(joined_word, 20)

        guess_phrase = (' '.join(guess_phrase))

        if turns == 0:


            def delete_db_session():

                if 'user' in session:
                    session_ID = session['user']
                    return session_ID
                # session_ID = session_ID
                session_id = session_ID
                deletesession = Sessions.query.filter_by(session_id=session_id).first()
                db.session.delete(deletesession)

            delete_db_session()

            def dropsession():
                session.pop('user', None)

            dropsession()

            return render_template('loose.html', phrase=phrase)
            # Redirect to Game Over page



        def session_info_enter(turns, guess_phrase, alpl, word_guess, session_id):
            alpl = "".join(alpl)
            word_guess = ''.join(word_guess)

            session_update = Sessions.query.filter_by(session_id=session_id).first()
            session_update.turns = turns
            session_update.guess_phrase = guess_phrase
            session_update.alpl = alpl
            session_update.word_guess = word_guess
            db.session.commit()

        session_info_enter(turns, guess_phrase, alpl, word_guess, session_id)

        screen = tweets.query.filter_by(politician=politician).first()
        screen_name = screen.screen_name

        return render_template('Game.html', guess_head=guess_head, remaining_letters=remaining_letters, turns=turns,
                               message_line=message_line, guess_phrase=guess_phrase, choice=choice, screen_name=screen_name)



if __name__ == '__main__':
    app.run()
    # app.debug = True



