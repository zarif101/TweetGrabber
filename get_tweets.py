import requests
import pandas as pd
from auth_info import *

def get_tweets(username):
    bearer_token = get_bearer_token()
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    url = 'https://api.twitter.com/2/tweets/search/recent?max_results=100&query=from:'+username
    response = requests.get(url, headers=headers)
    return response

def main():
    username = input('Account username: ')
    save_filename = input('File to save to: ')
    response = get_tweets(username)
    response = response.json()

    tweets = []
    tweet_ids = []
    for tweet in response['data']:
        tweets.append(tweet['text'])
        tweet_ids.append(tweet['id'])

    ret = pd.DataFrame({'tweet_text':tweets,'tweet_ids':tweet_ids})
    ret.to_csv(save_filename,index=False)
if __name__=='__main__':
    main()
