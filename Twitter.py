import tweepy
import matplotlib.pyplot as plt
from  textblob import TextBlob 
import time

# all 4 authentication keys to access twitter API
# to connect as OAth handler or jump serever / revers proxy server
consumer_key = "hAIGnUgnUT9nPw70Fx5LxGgQr"
consumer_sec = "muKnI3JjOzdQPStZNSCbFUdRfk6gH1pW8tDoIgiPOrdlOBnhAB"

# from proxy server we need to connect
access_token = "1414966657416499206-xg0t1rgAE0cIfYHc0XcvZOMIrHlvX4"
access_token_sec = "IlbiDLAIgv0s8uIADrprGQ6kTMm9lWIcA9psTYt5WnYjX"

# tweepy explore
dir(tweepy)

# connected to jump server of twitter
auth=tweepy.OAuthHandler(consumer_key,consumer_sec)

# now we can connect from jump server to web server of twitter
auth.set_access_token(access_token,access_token_sec)

# now we can connect to API storge server of twitter
api_connect=tweepy.API(auth)

# now you can search any topic on twitter
tweet_data=api_connect.search('NLP',count=100)

pos=0
neg=0
neu=0

# printing line by line
for tweet in tweet_data:
   #print(tweet.text)
   analysis=TextBlob(tweet.text) # here it will apply NLP\
   print(analysis.sentiment)
   # now checking polarity only
   if analysis.sentiment.polarity > 0:
      print("posative")
      pos=pos+1
   elif analysis.sentiment.polarity == 0 :
      print("Neutral")
      neu=neu+1
   else :
      print("Negative")
      neg=neg+1
      
# ploting graphs
plt.xlabel("tags")
plt.ylabel("polarity")
#plt.bar(['pos','neg','neu'],[pos,neg,neu])
plt.pie([pos,neg,neu],labels=['pos','neg','neu'],autopct="%1.1f%%")
plt.show()

