import tweetbot as tb
import time

file_path = './tweets.txt'
tweets = []
username = raw_input('Enter your UserName: ')
password = raw_input('Enter your Password: ')
time = raw_input('Enter the Amount of time between Broadcasts in Minutes: ')
is_running = raw_input('Type yes or no to start timer: ')
actual_time = int(time)

if is_running == 'yes':
    running = 1
elif is_running == 'no':
    running = 0

tb.timer(running, tb.load_tweets(file_path))
