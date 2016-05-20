import os
from time import sleep
import random

#--------------------#
#  User Input Below  #
#--------------------#

username = raw_input('[TweetBot] > Enter your UserName: ')
password = raw_input('[TweetBot] > Enter your Password: ')
string_time = raw_input('[TweetBot] > Enter the Amount of time between Broadcasts in Minutes: ')
real_time = int(string_time) * 10
timer_is_running = raw_input('[TweetBot] > Type yes or no to start timer: ')


#-------------------------------------------#
#  Takes the Values from a file and writes  #
#  them to the list provided                #
#-------------------------------------------#
def write_to_list(file):
    if not os.path.exists(file):
        open(file, 'w')
    elif os.path.exists(file):
        file = open(file, 'r')
        try:
            lines = file.read().split(',')
            return lines
        except AttributeError:
            print('[TweetBot] > There is nothing to Write to the list')


#-----------------------------#
#  Blacklist and Tweets List  #
#  uses the write_to_list     #
#  function to assign the     #
#  values here                #
#-----------------------------#
print('------------------------------------------------------')
print('[TweetBot] > Reading blacklist.txt & writting to List')
blacklist = write_to_list('./blacklist.txt')
print('[TweetBot] > Reading tweets.text & writting to List')
tweets = write_to_list('./tweets.txt')
print('------------------------------------------------------')

#-------------------------------------------------#
#  DEPRECATED FUNCTION                            #
#  Check to see if Random Number is on blacklist  #
#  If is then generates new number till it isnt   #
#  If Number not on Black List It adds it to      #
#  Black list and posts it                        #
#-------------------------------------------------#
'''
def pick_tweet(random_num, tweets_list):
    if random_num not in blacklist:
        blacklist.append(str(random_num) + ',')
        return tweets_list[random_num]
    elif random_num in blacklist:
        while random_num in blacklist:
            random_num2 = random.randrange(0, len(tweets_list))
            if random_num2 not in blacklist:
                blacklist.append(random_num2 + ',')
                return tweets_list[random_num2]
                break
'''


#-------------------------------------------#
#  The index_generator function is used to  #
#  Generate a random integer and check      #
#  if it has been added to the blacklist    #
#  If so then it regenerates the Index      #
#-------------------------------------------#
def index_generator():
    print('[TweetBot] > Generating Random Index')
    random_index = random.randrange(0, len(tweets))
    if random_index in blacklist:
        while True:
            random_index_1 = random.randrange(0, len(tweets))
            if random_index_1 in blacklist:
                print('[TweetBot] > Generated Index ' + str(random_index_1) + ' [Bad]. Regenerating')
                print('-----------------------------------------------------------------------------')
                print('[TweetBot] > To keep from Overloading crappy PC\'s there is a 5 Second delay.')
                print('-----------------------------------------------------------------------------')
                sleep(5)
            elif random_index_1 not in blacklist:
                print('[TweetBot] > Generated Index' + ' ' + str(random_index_1) + ' ' + '[Good]')
                blacklist.append(random_index_1)
                return random_index_1
                break
    elif random_index not in blacklist:
        print('[TweetBot] > Generated Index' + ' ' + str(random_index) + ' ' + '[Good]')
        blacklist.append(random_index)
        return random_index


#-------------------------------------------------#
#  A Timer that keeps up with the time and posts  #
#  after time reaches Zero                        #
#-------------------------------------------------#
def timer(time):
    while timer_is_running.lower() == 'yes':
        print('[TweetBot] > Timer Started')
        sleep(time)
        print('------------------------------------------------------')
        print('[TweetBot] > Message:' + tweets[index_generator()])
        print('------------------------------------------------------')
        print('[TweetBot] > Timer Restarted')
        print('------------------------------------------------------')

timer(real_time)