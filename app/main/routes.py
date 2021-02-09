from app.main import bp
from flask import render_template, redirect, send_file, request
import os
import subprocess
from dotenv import load_dotenv
from pathlib import Path
from textblob import TextBlob
import tweepy
import pandas as pd
from twitter_sentiment_classifier import sentiment_classifier
import logging

env_path = Path('..','..') / '.env'
load_dotenv(dotenv_path=env_path, verbose=True)

logging = logging.getLogger("applicationLogger")

@bp.route('/')
@bp.route('/index')
@bp.route('/index.html')
def index():
    return render_template('main/index.html')


@bp.route('/submit', methods=['POST'])
def submit():
    consumer_key = os.getenv('CONSUMER_KEY')
    consumer_secret = os.getenv('CONSUMER_SECRET')
    access_key = os.getenv('ACCESS_KEY')
    access_secret = os.getenv('ACCESS_SECRET')

    hashtag = str(request.form.get('hashtag'))
    number = int(request.form.get('quantity'))
    #print("Looking for: {} {}".format(hashtag, number))

    if number > 200:
        number = 200
    if int(len(hashtag)) > 50:
        hashtag = '#Corona'

    logging.info("Looking for: {} {}".format(hashtag, number))

    try:
        login = tweepy.OAuthHandler(consumer_key, consumer_secret)
        login.set_access_token(access_key, access_secret)
        api = tweepy.API(login)

        tweets = tweepy.Cursor(api.search, hashtag, lang="en", tweet_mode='extended').items(number)

        result = [tweet for tweet in tweets]
        result_set = list()

        for tweet in result:
            username = tweet.user.screen_name
            name = tweet.user.name
            created_at = tweet.created_at

            try:
                full_text = tweet.retweeted_status.full_text
            except AttributeError:
                full_text = tweet.full_text

            sentiment = sentiment_classifier(full_text)

            result_set.append([full_text, sentiment, username, created_at])

        writer = pd.ExcelWriter('excel_output.xlsx', engine='xlsxwriter', datetime_format='DD-MM-YYYY HH:MM:SS',
                                date_format='DD-MM-YYYY')
        dataframe = pd.DataFrame(result_set, columns=['tweet_message', 'sentiment', 'username', 'created_at'])
        dataframe.to_excel(writer, sheet_name='result', engine='xlsxwriter', index=False, encoding='UTF-8')
        writer.save()

    except Exception as error:
        logging.error(error)

    return render_template('main/index.html')


@bp.route('/download_report', methods=['GET'])
def download_report():
    return send_file(os.path.join('..','excel_output.xlsx'), as_attachment=True, cache_timeout=-1)
