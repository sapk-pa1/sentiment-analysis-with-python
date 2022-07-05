from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy.streaming import Stream

import twitter_credential

class StdOutListener(StreamListener): 
    '''
    Class to stream the live tweets 


    '''
    def __init__(self): 
        pass
    
    def on_data(self, data ): 
        print(data) 
    def on_error(self, status): 
        print(status)

if __name__ == '__main__':
    listener = StdOutListener()
    auth = OAuthHandler(twitter_credential.CONSUMER_KEY,twitter_credential.CONSUMER_SECRET,)
    auth.set_access_token(twitter_credential.ACCESS_TOKEN, twitter_credential.ACCESS_TOKEN_SECRET)
    stream = Stream(auth, listener)
    stream.filter(track= ['donald trump', 'hilary clinton', 'barack obama'])
