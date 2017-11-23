import os
import random
import textwrap
from datetime import datetime

from flask import Flask, request, render_template, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# import os
#
# import os

#for local
app.config.from_object('config.BaseConfig')


#for Heroku
# import os
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

# def screen_name(politician):
#
#     screenget = tweets.query.filter_by(politician=politician).first()
#     screen_name = screenget.screen_name
#
#
#     return screen_name()

def get_word_guess(session_id):

    word_guessget = Sessions.query.filter_by(session_id=session_id).first()
    word_guess = word_guessget.word_guess
    word_guess = list(word_guess)

    return word_guess


def get_alpl(session_id):

    alplget = Sessions.query.filter_by(session_id=session_id).first()
    alpl = alplget.alpl
    alpl = list(alpl)


    # conn = sqlite3.connect('politicalhangman.db')
    # c = conn.cursor()
    # if 'user' in session:
    #     session_ID = session['user']
    # c.execute("SELECT alpl FROM game_db WHERE session_id=?", [session_ID])
    # alpl = c.fetchone()
    # alpl = ''.join(alpl)
    # l_alpl = []
    # for char in alpl:
    #     l_alpl.append(char)
    # alpl = l_alpl
    # conn.commit()
    # c.close()
    # conn.close()
    #
    # print(alpl)
    # print('alpl')

    return alpl


def get_turns(session_id):
    # if 'user' in session:
    #     session_ID = session['user']
    #     return session_ID
    # # session_ID = session_ID
    # session_id = session_ID
    turnsget = Sessions.query.filter_by(session_id=session_id).first()
    turns = turnsget.turns
    turns = int(turns)


    # conn = sqlite3.connect('politicalhangman.db')
    # c = conn.cursor()
    # if 'user' in session:
    #     session_ID = session['user']
    # c.execute("SELECT turns FROM game_db WHERE session_id=?", [session_ID])
    # turns = c.fetchone()
    # turns = turns[0]
    #
    # print(turns)
    # print('turns')
    return turns


def get_politician(session_id):
    # if 'user' in session:
    #     session_ID = session['user']
    #     return session_ID
    # # session_ID = session_ID
    # session_id = session_ID
    politicianget = Sessions.query.filter_by(session_id=session_id).first()
    politician = politicianget.politician


    # conn = sqlite3.connect('politicalhangman.db')
    # c = conn.cursor()
    # if 'user' in session:
    #     session_ID = session['user']
    # c.execute("SELECT politician FROM game_db WHERE session_id=?", [session_ID])
    # politician = c.fetchone()
    # politician = ''.join(politician)
    #
    # print(politician)
    # print('politician')

    return politician
#
# def get_backgroun_url(politician_name):
#     backgroundget = tweets.query.filter_by(politician=politician_name).first()
#     image = backgroundget.background_url
#     print(image)
#     print('test1')
#     return image




@app.route('/', methods=['POST', 'GET'])
def Hangman():
    if request.method == 'GET':

        # session['user'] = 'Anthony'
        # session['user'] = random.getrandbits(31)

        # if 'user' in session:
        #     session_ID = session['user']
        # print(session_ID)
            # return session_ID




        if 'user' not in session:
            session['user'] = random.getrandbits(31)

        # conn = sqlite3.connect('politicalhangman.db')
        # c = conn.cursor()

        def session_id_enter(session_ID):

            # if 'user' in session:
            #     session_ID = session['user']
            #     return session_ID
            # # session_ID = session_ID
            session_id = session_ID
            datestamp = str(datetime.now())
            # print('session id')
            # print(type(session_id))
            # print('datestamp')
            # print(type(datestamp))
            id_enter = Sessions(session_id=session_id, datestamp=None, politician=None, guess_phrase=None,
                                phrase=None, word_guess=None, turns=None, alpl=None)
            db.session.add(id_enter)
            db.session.commit()


            # session_id = session_ID
            # datestamp = str(datetime.now())
            # c.execute("INSERT into game_db (session_id, datestamp) VALUES (?, ?)",
            #             (session_id, datestamp))
            # conn.commit()


        session_ID = session['user']
        session_id_enter(session_ID)

        # Game resets on returning to the front page
        # global word_guess
        # global phrase_guess
        # global alpl

        # word_guess = []
        # phrase_guess = []
        # alpl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        #         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        #         '1', '2', '3', '4', '5', '6', '8', '9', '0', '@', '#']


        # return render_template('twitter2.html')
        return render_template('index.html')

    elif request.method == 'POST':

        # currently nothing gets posted to the homepage/ not used

        # return render_template('twitter2.html')
        return render_template('index.html')


@app.route('/indexPolChoice', methods=['POST', 'GET'])
def Politician_choice():
    # global politician_id

    if request.method == 'GET':

        # if 'user' in session:


        return render_template('indexPolChoice.html')

    elif request.method == 'POST':

        # global phrase
        # global politician

        politician = request.form['polititian']

        from pol_ids import t_dict

        # politician_id = t_dict[politician]

        session_ID = session['user']


        # conn = sqlite3.connect('politicalhangman.db')
        # c = conn.cursor()
        #
        # def session_info_enter(politician, politician_id):
        #     if 'user' in session:
        #         session_ID = session['user']
        #     c.execute("UPDATE game_db set politician=?, politician_id=? WHERE session_id=?", [politician, politician_id,
        #               session_ID])
        #     conn.commit()
        #     c.close()
        #     conn.close()
        #
        # session_info_enter(politician, politician_id)

        # def tweet_lookup():

        # global remaining_letters
        # global turns
        # global i
        # global politician
        # global z


        # conn = sqlite3.connect('politicalhangman.db')
        # c = conn.cursor()

        politician_name = politician

        tweet = tweets.query.filter_by(politician=politician_name).first()
        word = tweet.tweet
        screen = tweets.query.filter_by(politician=politician_name).first()
        screen_name = screen.screen_name
        print(screen_name)

        # image = get_backgroun_url(politician_name)


        # print('tweet')
        # print(word)


        # print(type(data))
        #
        # # def tweet_lookup():
        # query = 'SELECT tweet from PolTweets WHERE politician=?'
        # c.execute(query, (politician_name,))
        # data = c.fetchone()
        # conn.commit()
        # print(data)
        # print('tweet')
        #
        # i = data
        # #i is returned as a tuple
        # z = " "
        # for x in i:
        #     z = z + x + " "
        #
        #     # c.close()
        #     # conn.close()
        #
        # # tweet_lookup()
        #
        #
        #
        # ''.join(z)
        # word = [z]  # Gets list object from lastline
        # word = ','.join(word)  # converts list object to str
        #
        # print('1')
        # print(word)
        # print(type(word))

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

        # print('2')
        # print(word_guess)
        phrase = ''.join(phrase)
        # print(phrase)

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

        # remaining_letters = textwrap.fill(', '.join(alpl), 52)

        # conn = sqlite3.connect('politicalhangman.db')
        # c = conn.cursor()

        def session_info_enter(politician, word_guess, phrase, alpl, turns, session_ID):

            # remaining_letters =''.join(remaining_letters)
            # if 'user' in session:
            #     session_ID = session['user']

            alpl = "".join(alpl)

            word_guess = ''.join(word_guess)
            # if 'user' in session:
            # session_ID = session['user']
            # # c.execute("UPDATE game_db set politician=?, politician_id=?, word_guess=?, phrase=?, alpl=?, turns=? WHERE session_id=?",
            # #           [politician, politician_id, word_guess, phrase, alpl, turns, session_ID])
            # # conn.commit()
            # # c.close()
            # # conn.close()
            # session_id = session_ID
            # if 'user' in session:
            #     session_ID = session['user']
            #     return session_ID
            # session_ID = session_ID
            session_id = session_ID
            sessioninfo = Sessions.query.filter_by(session_id=session_id).first()
            sessioninfo.politician = politician
            # sessioninfo.politician_id = politician_id
            sessioninfo.word_guess = word_guess
            sessioninfo.phrase = phrase
            sessioninfo.alpl = alpl
            sessioninfo.turns = turns
            db.session.commit()
            # print('politician')
            # print(type(politician))
            # # print('politician id')
            # # print(type(politician_id))
            # print('word_guess')
            # print(type(word_guess))
            # print('phrase')
            # print(type(phrase))
            # print('alpl')
            # print(type(alpl))
            # print('turns')
            # print(type(turns))
            # print('session id')
            # print(type(session_id))
            # print('session_info_enter')

        session_info_enter(politician, word_guess, phrase, alpl, turns, session_ID)


        return redirect(url_for('Game', screen_name=screen_name))
        # return redirect(url_for('gameplay.html'))
        # return render_template('gameplay.html')

        # # return redirect(url_for('Game', image=image))


@app.route('/About', methods=['GET'])
def About():
    if request.method == 'GET':

        # conn = sqlite3.connect('politicalhangman.db')
        # c = conn.cursor()
        # print('get')

        def delete_db_session():

            # if 'user' in session:
            #     session_ID = session['user']
            # session_id = session_ID
            if 'user' in session:
                session_ID = session['user']
                return session_ID
            # session_ID = session_ID
            session_id = session_ID
            deletesession = Sessions.query.filter_by(session_id=session_id).first()
            db.session.delete(deletesession)
            db.session.commit()

            # query = 'DELETE FROM game_db WHERE session_id=?'
            # c.execute(query, ((session['user']),))
            # conn.commit()
            # c.close()
            # conn.close()

        delete_db_session()

        def dropsession():
            session.pop('user', None)

        dropsession()

        return render_template('About.html')


@app.route('/Game', methods=['POST', 'GET'])
def Game():
    if request.method == 'GET':

        # if 'user' in session:
        #     session_ID = session['user']
        #     return session_ID
        #     # session_ID = session_ID
        # session_id = session_ID
        session_id = session['user']

        phrase = get_phrase(session_id)
        word_guess = get_word_guess(session_id)
        alpl = get_alpl(session_id)
        turns = get_turns(session_id)
        politician = get_politician(session_id)



        # print('Test123')
        # print(word_guess)


        # phrase, word_guess(bring in as joined_word(delete word_guess below), remaining_letters

        # global guess_phrase
        # global turns

        # if 'user' in session:
        #     print(session['user'])

        # print('get')

        # l = len(phrase)
        #
        # l = int(l / 10)
        #
        # if l >= 10:
        #     turns = 4
        # if l <= 9 and l >= 7:
        #     turns = 5
        # if l <= 6 and l >= 5:
        #     turns = 6
        # if l <= 4 and l >= 3:
        #     turns = 7
        # if l <= 2:
        #     turns = 8

        # print(word_guess)

        joined_word = (''.join(word_guess))

        guess_phrase = textwrap.fill(joined_word, 20)

        guess_phrase = (' '.join(guess_phrase))

        # print(guess_phrase)

        # guess_phrase = textwrap.fill(guess_phrase, 40)
        # guess_phrase = textwrap.wrap(40)

        remaining_letters = textwrap.fill(', '.join(alpl), 52)

        # conn = sqlite3.connect('politicalhangman.db')
        # c = conn.cursor()

        def session_info_enter(turns, guess_phrase, session_id):
            # if 'user' in session:
            # session_ID = session['user']
            # # c.execute("UPDATE game_db set turns=?, guess_phrase=? WHERE session_id=?",
            # #           [turns, guess_phrase, session_ID])
            # # conn.commit()
            # # c.close()
            # # conn.close()
            # session_id = session_ID
            # if 'user' in session:
            #     session_ID = session['user']
            #     return session_ID
            # session_ID = session_ID
            # session_id = session_ID
            # print('session_info_enter')
            sessioninfo = Sessions.query.filter_by(session_id=session_id).first()
            sessioninfo.turns = turns
            sessioninfo.guess_phrase = guess_phrase
            db.session.commit()

        session_info_enter(turns, guess_phrase, session_id)

        # guess_head = 'The latest tweet from %r' % politician
        guess_head = politician
        print(guess_head)


        # conn = sqlite3.connect('politicalhangman.db')
        # c = conn.cursor()

        screen = tweets.query.filter_by(politician=politician).first()
        screen_name = screen.screen_name

        return render_template('Game.html', guess_head=guess_head, turns=turns, guess_phrase=guess_phrase,
                               remaining_letters=remaining_letters, screen_name=screen_name)
        # return render_template('gameplay.html.html', guess_head=guess_head, turns=turns, guess_phrase=guess_phrase,
        #                    remaining_letters=remaining_letters)

    elif request.method == 'POST':

        # Get guess+phrase, convert to list,

        session_id = session['user']

        phrase = get_phrase(session_id)
        word_guess = get_word_guess(session_id)
        alpl = get_alpl(session_id)
        turns = get_turns(session_id)
        politician = get_politician(session_id)

        # GEt all variables from game_db return variables


        guess_head =  politician
        message_line = ' '

        choice = request.form['Char_Choice']
        choice = choice.lower()

        if choice not in alpl:
            message_line = "That letter has already been chosen."

        if choice not in phrase:
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

            # conn = sqlite3.connect('politicalhangman.db')
            # c = conn.cursor()

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

            return render_template('win.html', phrase=phrase)

        joined_word = (''.join(word_guess))

        guess_phrase = textwrap.fill(joined_word, 20)

        guess_phrase = (' '.join(guess_phrase))

        if turns == 0:

            # conn = sqlite3.connect('politicalhangman.db')
            # c = conn.cursor()

            def delete_db_session():
                # if 'user' in session:
                #     session_ID = session['user']
                # session_id = session_ID
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

            # print('Game Over')
            return render_template('loose.html', phrase=phrase)
            # Redirect to Game Over page

        # conn = sqlite3.connect('politicalhangman.db')
        # c = conn.cursor()

        def session_info_enter(turns, guess_phrase, alpl, word_guess, session_id):
            alpl = "".join(alpl)
            word_guess = ''.join(word_guess)
            # if 'user' in session:
            #     session_ID = session['user']
            # c.execute("UPDATE game_db set turns=?, guess_phrase=?, alpl=?, phrase=?, word_guess=? WHERE session_id=?",
            #           [turns, guess_phrase, alpl, phrase, word_guess, session_ID])
            # conn.commit()
            # c.close()
            # conn.close()

            # if 'user' in session:
            # session_ID = session['user']
            # session_id = session_ID
            # if 'user' in session:
            #     session_ID = session['user']
            #     return session_ID
            # # session_ID = session_ID
            # session_id = session_ID
            session_update = Sessions.query.filter_by(session_id=session_id).first()
            session_update.turns = turns
            session_update.guess_phrase = guess_phrase
            session_update.alpl = alpl
            # session_update.phrase = phrase
            session_update.word_guess = word_guess
            db.session.commit()

        session_info_enter(turns, guess_phrase, alpl, word_guess, session_id)

        # print(guess_phrase)
        screen = tweets.query.filter_by(politician=politician).first()
        screen_name = screen.screen_name

        return render_template('Game.html', guess_head=guess_head, remaining_letters=remaining_letters, turns=turns,
                               message_line=message_line, guess_phrase=guess_phrase, choice=choice, screen_name=screen_name)
        # return render_template('gameplay.html', guess_head=guess_head, remaining_letters=remaining_letters, turns=turns,
        #                        message_line=message_line, guess_phrase=guess_phrase, choice=choice)


if __name__ == '__main__':
    app.run()
    app.debug = True


    # host = os.environ.get('IP', '0.0.0.0')
    # port = int(os.environ.get('PORT', 8910))
    #
    # app.run(host=host, port=port)
