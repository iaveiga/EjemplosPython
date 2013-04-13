import tweepy
import re

def getApi():
	ck = 'cAYogkcO8qrg8uarYXw'
	cks = '7fRJ6sZY4nJP8IMTdSTOcbDtTuOuF5UX22OjcND2LE'
	at = '103998535-saAt56xCjXpnFnI2ZVEuoEsHWatPrWW1qvkZnx7S'
	ats = 'enpuB0wNpnM5181u9k8d6r3fMzxfy4GnVh10ZnoL20'
	auth = tweepy.OAuthHandler(ck,cks)
	auth.set_access_token(at,ats)
	api = tweepy.API(auth)
	return api


'''
Obtiene los últmos n-tweets dado un usuario
'''
def getTweets (user_, n, includeRT):
	user = api.get_user(user_)
	pages = []      
	tweets = []
	for page in tweepy.Cursor(api.user_timeline, id = user_, count = n).pages(1):
		pages.append(page)
	
	for page in pages:
		for status in page:
			tweets.append(status)
	return tweets

def getMentions(user,num):
	pages = []
	mentions = []
	for page in tweepy.Cursor(api.mentions_timeline,id = user, count = num):
		pages.append(page)
	
	for page in pages:
		for status in page:
			mentions.apend(status)
	return mentions

'''
Devuelve una lista con la frecuenca de los tweets
	mañana
	tarde
	noche
'''
def freqHoraTweets(lsTweets):
	lsFreq = [0,0,0]
	for status in lsTweets:
		date = str(status.created_at)
		hour = int(date[11:13])
		if hour >=0 and hour < 8:
			lsFreq[0]+= 1
		if hour >=8 and hour < 16: 
			lsFreq[1]+= 1
		else:
			lsFreq[2]+= 1
	return lsFreq


#Devuelve el Corpus de una lista de tweets
def corpus(lsTweets):
        corpus = []
        for tweet in lsTweets:
                text = tweet.text
                for word in text:
                        corpus.append(word)
        return corpus

#Elimina el patrón indicado del tweet
def cleanTweet(tweet,pattern):
    tweet = re.sub(pattern,'',tweet)
    return tweet

#Elimina los RT, símbolos de puntuación, menciones, números, links de los tweets
def cleanTweets(lsTweets):

    pRT = "(RT|via)((?:\\b\\W*@\\w+)+)"
    pMentions = "@\\w+"
    pPunct = "[[:punct:]]"
    pDig = "\d+"
    pLinks = '(?:http://|www.)[^"\' ]+'
    for i in range(0,len(lsTweets)):
       lsTweets[i].text = cleanTweet(lsTweets[i].text, pRT)
       lsTweets[i].text = cleanTweet(lsTweets[i].text, pMentions)
       lsTweets[i].text = cleanTweet(lsTweets[i].text, pPunct)
       lsTweets[i].text = cleanTweet(lsTweets[i].text, pDig)
       lsTweets[i].text = cleanTweet(lsTweets[i].text, pLinks)
    return lsTweets
