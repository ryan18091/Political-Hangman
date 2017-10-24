import json
import sqlite3
import time
from datetime import datetime

import tweepy

#Twitter API Keys
with open('config.json', 'r') as f:
    config = json.loads(f.read())
consumer_key = config['consumer_key']
consumer_secret = config['consumer_secret']
access_token = config['access_token']
access_token_secret = config['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


#Opening connection to DB
conn = sqlite3.connect('politicalhangman.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS PolTweets( politician VARCHAR, politician_id INTEGER, datestamp TEXT, tweet TEXT)')

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS game_db(session_id INTEGER, politician VARCHAR, politician_id INTEGER,'
              'datestamp TEXT, turns INTEGER, guess_phrase TEXT, remaining_letters TEXT)')


create_table()
c.close()
conn.close()

while True:

    # for politician in pol_list:
    from src.pol_ids import t_dict

    for politician, politician_id in t_dict.items():

        time.sleep(15)
        for tweet in tweepy.Cursor(api.user_timeline, id=politician_id).items(10):

            # print(tweet)
            # print(type(tweet))
            #
            # import json
            # print(dir(tweet))
            # print(tweet.text)

            if (not tweet.retweeted) and ('RT @' not in tweet.text):
                try:
                    t = (tweet)
                    mystring = str(t)


                    def find_between(mystring, first, last):
                        try:
                            start = mystring.index(first) + len(first)
                            end = mystring.index(last, start)
                            return mystring[start:end]
                        except ValueError:
                            return ""


                    i = (find_between(mystring, "text':", ", 'truncated"))

                    conn = sqlite3.connect('politicalhangman.db')
                    c = conn.cursor()

                    def delete_pre_tweet():
                        query = 'delete from PolTweets WHERE politician=?'
                        c.execute(query, (politician_name,))
                        conn.commit()


                    politician_name = politician
                    politicianid = politician_id

                    delete_pre_tweet()


                    def tweet_entry():
                        politician = politician_name
                        politician_id = politicianid
                        datestamp = str(datetime.now())
                        tweet = i
                        c.execute("INSERT  into PolTweets (politician, politician_id, datestamp, tweet) VALUES (?, ?, ?, ?)",
                                  (politician, politician_id, datestamp, tweet))
                        conn.commit()
                        c.close()
                        conn.close()


                    tweet_entry()
                    print(politician)
                    print(i)
                    print(50 * '#')
                    # c.close()
                    # conn.close()
                    break

                except tweepy.TweepError as e:
                    print(e.reason)
                    sleep(10)
                    continue
                except StopIteration:
                    break

            if (tweet.retweeted) and ('RT @' in tweet.text):
                # print('Retweet')
                continue
