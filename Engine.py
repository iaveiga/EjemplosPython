import tweepy

def getApi():
	ck = 'cAYogkcO8qrg8uarYXw'
	cks = '7fRJ6sZY4nJP8IMTdSTOcbDtTuOuF5UX22OjcND2LE'
	at = '103998535-saAt56xCjXpnFnI2ZVEuoEsHWatPrWW1qvkZnx7S'
	ats = 'enpuB0wNpnM5181u9k8d6r3fMzxfy4GnVh10ZnoL20'
	auth = tweepy.OAuthHandler(ck,cks)
	auth.set_access_token(at,ats)
	api = tweepy.API(auth)
	return api
	
def getTweets (user_, num, includeRT):
	user = api.get_user(user_)
	pages = []      
	tweets = []
	for page in tweepy.Cursor(api.user_timeline, id = user_, count = num).pages(1):
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
