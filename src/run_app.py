import os
import sqlite3

from Twitter_App import app

# from twitter_apptest import app


conn = sqlite3.connect('politicalhangman.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS game_db(session_id INTEGER, politician VARCHAR, politician_id INTEGER,'
              'datestamp TEXT, guess_phrase TEXT, phrase TEXT, word_guess TEXT, turns INTEGER, alpl TEXT)')
    conn.commit()
    c.close()
    conn.close()

create_table()



if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 5000))
    # port = int(os.environ.get('PORT', 8910))

    app.run(host=host, port=port)

#Background image distorted on hangman game screen
#replace &amp with &
