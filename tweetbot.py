import os
import time
import random

#--------------------#
#  User Input Below  #
#--------------------#

username = raw_input('[TweetBot] > Enter your UserName: ')
password = raw_input('[TweetBot] > Enter your Password: ')
string_time = raw_input('[TweetBot] > Enter the Amount of time between Broadcasts in Minutes: ')
real_time = int(string_time) * 60
timer_is_running = raw_input('[TweetBot] > Type yes or no to start timer: ')

#---------------#
#  LOGIC BELOW  #
#---------------#

# Takes the Values from a file and writes
# them to the list provided
def write_to_list(file):
    if not os.path.exists(file):
        open(file, 'w')
    elif os.path.exists(file):
        file = open(file, 'r')
        try:
            for line in file:
                file.append(line)
                return file
        except AttributeError:
            print('[TweetBot] > There is nothing to Write to the list')

# Blacklist and Tweets List
# uses the write_to_list
# function to assign the
# values here
print('[TweetBot] > Reading blacklist.txt & writting to List')
blacklist = write_to_list('./blacklist.txt')
print('[TweetBot] > Reading tweets.text & writting to List')
tweets = write_to_list('./tweets.txt')

# Random number generator that picks a number
# between 0 and len(tweets) *Length of Tweets*
try:
    random = random.randrange(0, len(tweets))
except TypeError:
    print('[TweetBot] > There is nothing within tweets.txt')
# Check to see if Random Number is on blacklist
# If is then generates new number till it isnt
# If Number not on Black List It adds it to
# Black list and posts it
def pick_tweet(random, tweets):
    while random == blacklist:
        random = random(0, len(tweets))
        if not random == blacklist:
            blacklist.append(random)
            return tweets[random]
            break

# Posts the selected tweet to Twitter
def post_tweet(random_num, tweets_list):
    print(pick_tweet(random_num, tweets_list))

# A Timer that keeps up with the time and posts
# after time reaches Zero

def timer(time, random_num, tweets_list):
    while timer_is_running.lower() == 'yes':
        print('[TweetBot] > Timer Started')
        time.sleep(time)
        post_tweet(random_num, tweets_list)

timer(real_time, random, tweets)