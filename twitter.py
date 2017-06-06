import tweepy
from textblob import TextBlob
import csv

### consumer key and consumer secret key of twitter api
api_key = 'xxxxxxxxxxxxxxx'
api_secret = 'xxxxxxxxxxxxxxxx'

### access token generated for the applicaton 
access_token = 'xxxxxxxxxxxxxxxxx'
access_secret = 'xxxxxxxxxxxxxxxxxx'

### authenticating
auth = tweepy.OAuthHandler(api_key,api_secret)
auth.set_access_token(access_token,access_secret)
api = tweepy.API(auth)

print("\n#################################################################\n")
user = input("Enter username: ")
print("\nTweets from {0}\n".format(user))

### screen_name :is to get the username
### include_rts :whether the tweets retrive should include retweets or not
### count :is the no of tweet retrived to analyse
tweets = api.user_timeline(screen_name=user, include_rts=True, count=100)
p = 0
nu = 0
n = 0
with open('tsentiments.csv', 'w', newline='\n') as f:
	writer = csv.DictWriter(f, fieldnames=['Tweet', 'Sentiment'])
	writer.writeheader()

	for tweet in tweets:
		polarity = ""
		text = tweet.text
		analysis = TextBlob(text)
		polarity = analysis.sentiment.polarity
		if polarity > 0:
			print("\nTweet: Positive")
			polarity = 'Positive'		
			p = p + 1
		elif polarity == 0:
			print("\nTweet: Neutral")
			polarity = 'Neutral'
			nu = nu + 1
		else:
			print("\nTweet: Negative")
			polarity = 'Negative'
			n = n + 1
		writer.writerow({'Tweet':text, 'Sentiment':polarity})		###use .encode('utf-8') if encode error occurs for text or polarity
		print(tweet.text)
		
print("\n------------------------------")
print("Total: {0}".format(p+nu+n))
print("Positive: {0}".format(p/(p+nu+n)))
print("Negative: {0}".format(n/(p+nu+n)))

