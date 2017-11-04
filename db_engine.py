import json
import sqlite3
import time
from datetime import datetime

import tweepy

from models import *

# Twitter API Keys
# with open('config_secret.json', 'r') as f:
#     config = json.loads(f.read())
# consumer_key = config['consumer_key']
# consumer_secret = config['consumer_secret']
# access_token = config['access_token']
# access_token_secret = config['access_token_secret']

# Twitter API Keys
# with open('config_secret.json', 'r') as f:
#     config = json.loads(f.read())
consumer_key = "tgOf65xyMVuk98JMIJ6o8OV0w"
consumer_secret = "FUc8m2bpTIDKK6FoSBYj5jpsC5sG7fcFqS5ZGAuMdLLJqkS7CS"
access_token = "2401698925-jgzfZofScmvzyzfUWdxgI9FZuIXmjMrdt3NalJa"
access_token_secret = "U8LWL3VwHg4BTAgWWEDLitjrpoRG2MkKoKWTIXgtMKUDn"

# "consumer_key": "tgOf65xyMVuk98JMIJ6o8OV0w",
# "consumer_secret": "FUc8m2bpTIDKK6FoSBYj5jpsC5sG7fcFqS5ZGAuMdLLJqkS7CS",
# "access_token": "2401698925-jgzfZofScmvzyzfUWdxgI9FZuIXmjMrdt3NalJa",
# "access_token_secret": "U8LWL3VwHg4BTAgWWEDLitjrpoRG2MkKoKWTIXgtMKUDn"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


#Opening connection to DB
# conn = sqlite3.connect('politicalhangman.db')
# c = conn.cursor()
#
# def create_table_PolTweets():
#     c.execute('CREATE TABLE IF NOT EXISTS PolTweets(politician VARCHAR, politician_id INTEGER, datestamp TEXT, tweet TEXT)')
#
# def create_table_Gamedb():
#     c.execute('CREATE TABLE IF NOT EXISTS game_db(session_id INTEGER, politician VARCHAR, politician_id INTEGER,'
#               'datestamp TEXT, turns INTEGER, guess_phrase TEXT, remaining_letters TEXT, word_guess TEXT, phrase TEXT, alpl TEXT)')


# create_table_PolTweets()
# create_table_Gamedb()
# c.close()
# conn.close()

# while True:

    # for politician in pol_list:
from pol_ids import t_dict

for politician, politician_id in t_dict.items():

    time.sleep(6)
    print("Twitter API Engine Running...")
    for tweet in tweepy.Cursor(api.user_timeline, id=politician_id, tweet_mode='extended').items(10):


        if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
            try:
                t = (tweet)
                # print(t)
                i = (tweet.full_text)
                # created_at = (tweet.created_at)
                # print(created_at)
                # screen_name = (tweet.screen_name)
                # print(screen_name)
                mystring = str(t)

                screen_name = (tweet.user)
                screen_name = (screen_name.screen_name)
                print(screen_name)



                def find_between1(first, last):
                    mystring = str(t)
                    try:
                        start = mystring.index(first) + len(first)
                        end = mystring.index(last, start)
                        background_url= mystring[start:end]
                        background_url = background_url[4:]
                        background = background_url[:-4]
                        return background
                    except ValueError:
                        return ""


                background = (find_between1('profile_banner_url' , 'profile_link_color'))
                # print(background)

                def find_between2(first, last):
                    try:
                        start = mystring.index(first) + len(first)
                        end = mystring.index(last, start)
                        profile_url = mystring[start:end]
                        profile_url = profile_url[4:]
                        profile = profile_url[:-4]
                        return profile
                    except ValueError:
                        return ""


                profile = (find_between2('profile_image_url', 'profile_image_url_https'))
                # print(profile)





                def delete_pre_tweet(politician):


                    tweetdelete = tweets.query.filter_by(politician=politician).first()
                    db.session.delete(tweetdelete)
                    db.session.commit()

                politician_name = politician
                politicianid = politician_id


                selection = tweets.query.filter_by(politician=politician).first()

                if 'http' in i:
                    i = i[:-24]

                if 'https' in i:
                    num = i.find('https')
                    l = len(i)
                    p = num - l
                    i = i[:p]

                if '&amp' in i:
                    i = i.replace("&amp", "&")



                def tweet_entry():
                    politician = politician_name
                    # politician_id = politicianid
                    datestamp = str(datetime.now())
                    tweet = i
                    # background_url = background
                    # profile_url = profile
                    # print(politician)
                    # # print(politician_id)
                    # # print(datestamp)
                    # # print(tweet)
                    # # print(background_url)
                    # # print(profile_url)
                    # tweetupdate = tweets(politician=politician, politician_id=politician_id, datestamp=datestamp, tweet=tweet, background_url=background_url, profile_url=profile_url)
                    tweetupdate = tweets(politician=politician, datestamp=datestamp, tweet=tweet, screen_name=screen_name)

                    db.session.add(tweetupdate)
                    db.session.commit()

                def delete_pre_tweet(politician):
                    tweetdelete = tweets.query.filter_by(politician=politician).first()
                    db.session.delete(tweetdelete)
                    db.session.commit()

                politician_name = politician
                politicianid = politician_id

                if selection == None:
                    # print('No pre-tweet')
                    tweet_entry()
                    continue
                if politician == selection.politician:
                    # print('Updated Tweet')
                    delete_pre_tweet(politician)
                    tweet_entry()


                break

            except tweepy.TweepError as e:
                print('Tweepy Error')
                print(e.reason)
                sleep(10)
                continue
            except StopIteration:
                break

        if (tweet.retweeted) and ('RT @' in tweet.text):
            # print('Retweet')
            continue
