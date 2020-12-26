import requests
import pandas as pd
import warnings
from auth_info import *

def get_tweets(username):
    bearer_token = get_bearer_token()
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    url = 'https://api.twitter.com/2/tweets/search/recent?max_results=100&query=from:'+username
    response = requests.get(url, headers=headers)
    return response

def main():
    username = input('Account username: ')
    accounts = username.split(',')

    save_filename = input('File to save to: ')
    filenames = save_filename.split(',')
    if len(filenames[0]) == 0:
        filenames = [name+'.csv' for name in accounts]
    elif len(filenames) != len(accounts):
        warnings.warn('Number of filenames is not same as number of usernames. Usernames will also be used as filenames')

    idx = 0
    for acct in accounts:
        response = get_tweets(acct)
        response = response.json()

        tweets = []
        tweet_ids = []
        for tweet in response['data']:
            tweets.append(tweet['text'])
            tweet_ids.append(tweet['id'])

        ret = pd.DataFrame({'tweet_text':tweets,'tweet_ids':tweet_ids})
        ret.to_csv(filenames[idx],index=False)

        idx+=1
if __name__=='__main__':
    main()
