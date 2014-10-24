from __future__ import division #from future division library to display sentiment:float
import sys
import json
from collections import defaultdict #no keyerror when key not found in dict

def hw():
    print 'Hello, Twitter!'

def lines(fp):
    print str(len(fp.readlines()))

#sent_file
def sent_scores(sent_file):
    with open(sent_file) as f:
        return {line.split('\t')[0]: int(line.split('\t')[1]) for line in f} #the file is tab-delimited. "\t" means "tab character
        scores[term]=int(score) #convert the score to an integer
        #print sent_scores.items() #print every (term, score) pair in the dictionary
        #print type(term)
        #print type(score)

#tweet_file, sum of tweet score
def tweet_score(tweet, scores):
    return sum(scores.get(word, 0) for word in tweet.split()) #sum of tweet score based on sent_file, default is 0

#location details in tweet
def loc_details(tweet):
    try:
        country = tweet['place']['country_code'] #look for country
        state = tweet['place']['full_name'].split(", ")[1] #look for state
        text = tweet['text'] #tweet text
        return country, state, text
    except (KeyError, TypeError, IndexError): #expection handling for output errors
        return None

#happiest state
def happiest_state(tweet_file, sent_scores):
    count_tweets, scores, happiest = [defaultdict(float) for _ in range(3)] #use defaultdict to store count of tweets, scores and happiest
    with open(tweet_file) as f:
        js = (json.loads(line) for line in f) #load to json, text type and split the tweet
        tweet_location = (loc_details(tweet) for tweet in js if loc_details(tweet))
        state_scores = ((state, tweet_score(text, sent_scores)) #load state scores to match location details
                         for country, state, text in tweet_location
                         if len(state) == 2 and country == 'US')
       
        for state, score in state_scores:
            count_tweets[state] += 1 
            scores[state] += score
            happiest[state] = scores[state] / count_tweets[state]
    return max(happiest, key=happiest.get)


def main():
    #hw()
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    scores = sent_scores(sent_file=sys.argv[1])
    print (happiest_state(tweet_file=sys.argv[2], sent_scores=scores))
