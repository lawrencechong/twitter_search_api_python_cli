twitter.py
author : Lawrence Chong

twitter.py is a simple python Command Line Interface program that calls on the twitter API and does a search on the keyword that the user provides

To run this program in terminal, simply:

1. run: $ python twitter.py
2. Follow the prompts provided by the program
3. User can quit after providing a keyword, and typing 'n', all other inputs currently just loops back and continues asking for a new keyword

Libraries used:
1. oauth2: used to make requests with Twitter API
2. json: used to interpet json response from API call
3. random: used to make a random number to get a random tweet from statuses returned
4. urllib: used to encode the keyword into a url usable string
5. time: used to stimulate a program wait time
