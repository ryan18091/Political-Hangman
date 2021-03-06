import time
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tweepy
from os import environ


from models import *

consumer_key = (environ.get('consumer_key'))
consumer_secret = (environ.get('consumer_secret'))
access_token = (environ.get('access_token'))
access_token_secret = (environ.get('access_token_secret'))

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

global switch
switch = 'on'


def PH_Email():
    print('sending email...')
    user = (environ.get('EMAIL_USER'))
    password = (environ.get('EMAIL_PASSWORD'))
    send = (environ.get('EMAIL_SEND'))

    email_user = user
    email_password = password
    email_send = send
    subject = 'Political Hangman Twitter API Error.'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    body = t
    msg.attach(MIMEText(body, 'plain'))

    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, email_password)

    server.sendmail(email_user, email_send, text)
    server.quit()


from pol_ids import t_dict

for politician, politician_id in t_dict.items():



    time.sleep(6)
    print("Twitter API Engine Running...")
    try:

        for tweet in tweepy.Cursor(api.user_timeline, id=politician_id, tweet_mode='extended').items(10):
            print('in')

            if (not tweet.retweeted) and ('RT @' not in tweet.full_text):
                try:
                    t = (tweet)
                    i = (tweet.full_text)

                    switch = 'off'

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
                        datestamp = str(datetime.now())
                        tweet = i
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
                        tweet_entry()
                        continue
                    if politician == selection.politician:
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


    except tweepy.TweepError as e:
        t = str(e) + "\n" + politician
        print('Tweepy Error Except')
        PH_Email()

    if switch == 'on':
        print('Tweepy Error If')
        t = "Twitter API Error" + politician
        PH_Email()

