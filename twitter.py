import oauth2 as oauth
import json
from random import randint
import urllib
import time

CONSUMER_KEY = '####'
CONSUMER_SECRET = '####'
ACCESS_KEY = '####' 
ACCESS_SECRET = '####'

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

def random_search_tweet (keyword):

	url_encoded_query = urllib.quote_plus(keyword)
	search_endpoint = "https://api.twitter.com/1.1/search/tweets.json?q=" + url_encoded_query
	response, data = client.request(search_endpoint)
	random_tweet = "random tweet"

	if response['status'] == '200':
		
		tweets = json.loads(data)
		status_count = len(tweets['statuses'])
		
		if status_count > 0:
			random_num = randint(0, status_count - 1)
			screen_name = "@" + tweets['statuses'][random_num]['user']['screen_name']
			tweet = tweets['statuses'][random_num]['text']
			random_tweet = screen_name + " : " + tweet
		else:
			random_tweet = "Couldn't find anything"
	else:
		random_tweet = "Oops something went wrong"

	return random_tweet

def play_again():
	answer = raw_input("Another? 'y' for yes 'n' for no: ")
	if answer != 'y' and answer != 'n':
			print("Not a valid response")
			play_again()
	return answer

def main():
	play = 0
	while (play == 0):
	    print("\nRandom tweet, input keyword")
	    keyword = raw_input()
	    print("\n" + random_search_tweet(keyword) + "\n")
	    time.sleep(1)
	    play_more = play_again()
	    if play_more == 'n':
	    	play = 1
	    	print("finish")
	    
if __name__ == "__main__":
    main()




