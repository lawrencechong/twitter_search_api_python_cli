import oauth2 as oauth
import json
from random import randint
import urllib
import time

CONSUMER_KEY = 'kamB48MVVA2B9feX9gfS7R46g'
CONSUMER_SECRET = 'QQCBnVdWhgXYeXSZCfFOV1sAgcT6mmyRRQ8VL6N6FObQumUT36'
ACCESS_KEY = '704055394805665793-EAL6wtwQMYCGljMCeFHk2BYG7kO2d3y' 
ACCESS_SECRET = 'SwXZWtOX9y21NDYwN7cdMl0FVWxjR7Cip0uP0WbEAWRew'

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

def main():
	play = 0
	while (play == 0):
	    print("\nRandom tweet, input keyword")
	    keyword = raw_input()
	    print("\n" + random_search_tweet(keyword) + "\n")
	    time.sleep(3)
	    play_again = raw_input("Another? 'y' for yes 'n' for no: ")
	    if play_again == 'n':
	    	play = 1
	    	print("finish")

if __name__ == "__main__":
    main()




