import os
import random
import sqlite3
import textwrap
from datetime import datetime

from flask import Flask, request, render_template, url_for, redirect, session

alpl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '1', '2', '3', '4', '5', '6', '8', '9', '0', '@', '#', '&']

word_guess = []
turns = ()


app = Flask(__name__)
app.secret_key = os.urandom(24)

conn = sqlite3.connect('politicalhangman.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS game_db(session_id INTEGER, politician VARCHAR, politician_id INTEGER,'
              'datestamp TEXT, guess_phrase TEXT, phrase TEXT, word_guess TEXT, turns INTEGER, alpl TEXT)')
    conn.commit()
    c.close()
    conn.close()

create_table()


def get_phrase():
    conn = sqlite3.connect('politicalhangman.db')
    c = conn.cursor()
    if 'user' in session:
        session_ID = session['user']
    c.execute("SELECT phrase FROM game_db WHERE session_id=?", [session_ID])
    phrase = c.fetchone()
    #converts tuple to str
    phrase = ''.join(phrase)
    conn.commit()
    c.close()
    conn.close()

    return phrase

def get_word_guess():
    conn = sqlite3.connect('politicalhangman.db')
    c = conn.cursor()
    if 'user' in session:
        session_ID = session['user']
    c.execute("SELECT word_guess FROM game_db WHERE session_id=?", [session_ID])
    word_guess = c.fetchone()
    #converts tuple to str with characters broken apart
    word_guess = ''.join(word_guess)
    #converts str to list
    word_guess = list(word_guess)
    conn.commit()
    c.close()
    conn.close()
    return word_guess

def get_alpl():
    conn = sqlite3.connect('politicalhangman.db')
    c = conn.cursor()
    if 'user' in session:
        session_ID = session['user']
    c.execute("SELECT alpl FROM game_db WHERE session_id=?", [session_ID])
    alpl = c.fetchone()
    alpl = ''.join(alpl)
    l_alpl = []
    for char in alpl:
        l_alpl.append(char)
    alpl = l_alpl
    conn.commit()
    c.close()
    conn.close()
    return alpl

def get_turns():
    conn = sqlite3.connect('politicalhangman.db')
    c = conn.cursor()
    if 'user' in session:
        session_ID = session['user']
    c.execute("SELECT turns FROM game_db WHERE session_id=?", [session_ID])
    turns = c.fetchone()
    turns = turns[0]
    return turns

def get_politician():
    conn = sqlite3.connect('politicalhangman.db')
    c = conn.cursor()
    if 'user' in session:
        session_ID = session['user']
    c.execute("SELECT politician FROM game_db WHERE session_id=?", [session_ID])
    politician = c.fetchone()
    politician = ''.join(politician)
    return politician

@app.route('/', methods=['POST', 'GET'])
def Hangman():

    if request.method == 'GET':

        # session['user'] = 'Anthony'
        session['user'] = random.getrandbits(50)

        if 'user' in session:
            session_ID = session['user']
            print(session_ID)

        if 'user' not in session:
            session['user'] = random.getrandbits(50)
            print(session_ID)

        import sqlite3


        conn = sqlite3.connect('politicalhangman.db')
        c = conn.cursor()

        def session_id_enter():
            session_id = session_ID
            datestamp = str(datetime.now())
            c.execute("INSERT into game_db (session_id, datestamp) VALUES (?, ?)",
                        (session_id, datestamp))
            conn.commit()

        session_id_enter()


        #Game resets on returning to the front page
        # global word_guess
        # global phrase_guess
        # global alpl

        word_guess = []
        phrase_guess = []
        alpl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                '1', '2', '3', '4', '5', '6', '8', '9', '0', '@', '#']


        return render_template('twitter2.html')


    elif request.method == 'POST':

        #currently nothing gets posted to the homepage/ not used

        return render_template('twitter2.html')


@app.route('/Politician_choice', methods=['POST','GET'])
def Politician_choice():


    # global politician_id

    if request.method == 'GET':

        if 'user' in session:
            print(session['user'])

        return render_template('Politician_choice.html')

    elif request.method == 'POST':

        # global phrase
        # global politician

        politician = request.form['polititian']

        from src.pol_ids import t_dict

        politician_id = t_dict[politician]

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


        conn = sqlite3.connect('politicalhangman.db')
        c = conn.cursor()

        politician_name = politician

        # def tweet_lookup():
        query = 'SELECT tweet from PolTweets WHERE politician=?'
        c.execute(query, (politician_name,))
        data = c.fetchone()
        conn.commit()
        i = data
        #i is returned as a tuple
        z = " "
        for x in i:
            z = z + x + " "

            # c.close()
            # conn.close()

        # tweet_lookup()



        ''.join(z)
        word = [z]  # Gets list object from lastline
        word = ','.join(word)  # converts list object to str

        print('1')
        print(word)

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

        print('2')
        print(word_guess)
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


        remaining_letters = textwrap.fill(', '.join(alpl), 52)

        conn = sqlite3.connect('politicalhangman.db')
        c = conn.cursor()

        def session_info_enter(politician, politician_id, word_guess, phrase, alpl, turns):
            # remaining_letters =''.join(remaining_letters)
            if 'user' in session:
                session_ID = session['user']

            alpl = "".join(alpl)

            word_guess = ''.join(word_guess)
            if 'user' in session:
                session_ID = session['user']
            c.execute("UPDATE game_db set politician=?, politician_id=?, word_guess=?, phrase=?, alpl=?, turns=? WHERE session_id=?",
                      [politician, politician_id, word_guess, phrase, alpl, turns, session_ID])
            conn.commit()
            c.close()
            conn.close()

        session_info_enter(politician, politician_id, word_guess, phrase, alpl, turns)


        return redirect(url_for('Game'))



@app.route('/About', methods=['GET'])

def About():

    if request.method == 'GET':

        conn = sqlite3.connect('politicalhangman.db')
        c = conn.cursor()

        def delete_db_session():
            query = 'DELETE FROM game_db WHERE session_id=?'
            c.execute(query, ((session['user']),))
            conn.commit()
            c.close()
            conn.close()

        delete_db_session()

        def dropsession():
            session.pop('user', None)

        dropsession()

        return render_template('About.html')



@app.route('/Game', methods=['POST','GET'])

def Game():

    if request.method == 'GET':

        phrase = get_phrase()
        word_guess = get_word_guess()
        alpl = get_alpl()
        turns = get_turns()
        politician = get_politician()

        # print('Test123')
        # print(word_guess)


        #phrase, word_guess(bring in as joined_word(delete word_guess below), remaining_letters

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

        guess_phrase =(' '.join(guess_phrase))


        # print(guess_phrase)

        # guess_phrase = textwrap.fill(guess_phrase, 40)
        # guess_phrase = textwrap.wrap(40)

        remaining_letters = textwrap.fill(', '.join(alpl), 52)

        conn = sqlite3.connect('politicalhangman.db')
        c = conn.cursor()

        def session_info_enter(turns, guess_phrase):
            if 'user' in session:
                session_ID = session['user']
            c.execute("UPDATE game_db set turns=?, guess_phrase=? WHERE session_id=?",
                      [turns, guess_phrase, session_ID])
            conn.commit()
            c.close()
            conn.close()

        session_info_enter(turns, guess_phrase)

        guess_head = 'The latest tweet from %r' % politician

        # conn = sqlite3.connect('politicalhangman.db')
        # c = conn.cursor()



        return render_template('Game.html',guess_head=guess_head, turns=turns, guess_phrase=guess_phrase,
                               remaining_letters=remaining_letters)

    elif request.method == 'POST':


        #Get guess+phrase, convert to list,

        phrase = get_phrase()
        word_guess = get_word_guess()
        alpl = get_alpl()
        turns = get_turns()
        politician = get_politician()



        #GEt all variables from game_db return variables


        guess_head = 'The latest tweet from %r' % politician
        message_line = ' '

        choice = request.form['Char_Choice']
        choice = choice.lower()


        if choice not in alpl:
            message_line = "That letter has already been chosen."

        if choice not in phrase:
            message_line = 'That choice is not in the phrase'
            turns = (turns - 1)
            #--- This throw an error not (local variable turns referenced before assignment)

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


        comp_word = ''.join(word_guess)  # creates an un-joined instance of the word to compare to the guess_word for a win

        if comp_word == phrase:

            conn = sqlite3.connect('politicalhangman.db')
            c = conn.cursor()

            def delete_db_session():
                query = 'DELETE FROM game_db WHERE session_id=?'
                c.execute(query, ((session['user']),))
                conn.commit()
                c.close()
                conn.close()

            delete_db_session()

            def dropsession():
                session.pop('user', None)

            dropsession()

            return render_template('win.html', phrase=phrase)

        joined_word = (''.join(word_guess))

        guess_phrase = textwrap.fill(joined_word, 20)

        guess_phrase = (' '.join(guess_phrase))


        if turns == 0:

            conn = sqlite3.connect('politicalhangman.db')
            c = conn.cursor()

            def delete_db_session():
                query = 'DELETE FROM game_db WHERE session_id=?'
                c.execute(query, ((session['user']),))
                conn.commit()
                c.close()
                conn.close()

            delete_db_session()

            def dropsession():
                session.pop('user', None)

            dropsession()

            print('Game Over')
            return render_template('loose.html', phrase=phrase)
            #Redirect to Game Over page


        conn = sqlite3.connect('politicalhangman.db')
        c = conn.cursor()

        def session_info_enter(turns, guess_phrase, alpl, phrase, word_guess):
            alpl = "".join(alpl)
            word_guess = ''.join(word_guess)
            if 'user' in session:
                session_ID = session['user']
            c.execute("UPDATE game_db set turns=?, guess_phrase=?, alpl=?, phrase=?, word_guess=? WHERE session_id=?",
                      [turns, guess_phrase, alpl, phrase, word_guess, session_ID])
            conn.commit()
            c.close()
            conn.close()

        session_info_enter(turns, guess_phrase, alpl, phrase, word_guess)

        print(guess_phrase)


        return render_template('Game.html', guess_head=guess_head, remaining_letters=remaining_letters,turns=turns,
                               message_line=message_line, guess_phrase=guess_phrase, choice=choice)