import os
import time
import random
import twitter
import main_thread as mt

blacklist = []
random = random
tweets = []

def load_tweets(file):

    if not os.path.exists(file):
        file_object = open(file, 'w')
        file_object.write('This is a Test Tweeeeeeet!')
    elif os.path.exists(file):
        file_object = open(file, 'r')
        for line in file:
            tweets.append(line)
        return tweets

def count_objects(tweets):
    return len(tweets)


random = random.randrange(0, count_objects(load_tweets('./tweets.txt')))

def pick_tweet(random, tweets):
    while random == blacklist:
        random = random(0, 5)
        if not random == blacklist:
            blacklist.append(random)
            return tweets[random]
            break

def post_tweet(tweets):
# Plug in API to Post Tweet
# pretend API is asking for Text
# pick_tweet(random, tweets)
    print(tweets)


def timer(running, tweets):
    if not running == 1:
        print('Timer not Running')
    elif running == 1:
        while running == 1:
            time.sleep(mt.actual_time * 60)
            post_tweet(tweets)