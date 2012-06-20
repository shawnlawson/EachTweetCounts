# python EachTweetCounts.py

import tweepy

consumer_key=""
consumer_secret=""

access_token=""
access_token_secret=""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890()[]{}<>!@#$%^&*~`-_=+|;:,./?"\\\' '
tweet = []

#open file to find where we left off
fileIn = open( "currentTweet.txt", "r" )
for line in fileIn:
    tweet.append( int(line) )
fileIn.close()


#recursive bit that looks to the right
def right( at ):
    if at < len(tweet):
        tweet[ at ] = (tweet[ at ] + 1) % len(chars)
        if tweet[ at ] == 0:
            right( at+1 )
    elif at < 140 and at == len(tweet):
        tweet.append( 0 )


#print or tweet latest from file data
status = ""
for i in range( len(tweet) ):
    status += chars[ tweet[i] ]

#print tweet
print status
#api.update_status(status)


#update for next tweet
tweet[0] = (tweet[0] + 1) % len(chars)

if tweet[0] == 0:
    right(1)


#write out where we are
toWrite = ""

for i in range( len(tweet) ):
    toWrite += str(tweet[i]) + "\n"

fileOut = open( "currentTweet.txt", "w" )
fileOut.write( toWrite )
fileOut.close()