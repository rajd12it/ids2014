#from __future__ import division #from future division library to display sentiment:float
import sys
import json
from collections import Counter #collections library for Counter

def hw():
    print 'Hello, Twitter!'

def lines(fp):
    print str(len(fp.readlines()))

#sent_file
#def sent_scores(sent_file):
    #with open(sent_file) as f:
        #return {line.split('\t')[0]: int(line.split('\t')[1]) for line in f} #the file is tab-delimited. "\t" means "tab character
        #scores[term]=int(score) #convert the score to an integer
        #print sent_scores.items() #print every (term, score) pair in the dictionary
        #print type(term)
        #print type(score)

#tweet_file, sum of tweet score
#def tweet_score(tweet, scores):
    #return sum(scores.get(word, 0) for word in tweet) #sum of tweet score based on sent_file, default is 0

#tweet_file, calculate frequency
def top_ten(tweet_file):
    with open(tweet_file) as f:
        js_entities = (json.loads(line).get('entities', None) for line in f) #load to json and get entities
        tweet_hashtags = (entity.get('hashtags') for entity in js_entities if entity)
        tweet_text = (tag['text'] for hashtags in tweet_hashtags for tag in hashtags)
        #tweet=tweet.encode('utf-8') #convert to utf
        #tweet=tweet.lower() #change to lowercase
        #print tweet 
        return Counter(tweet_text).most_common(10) #counter for tweet to get the most common

def main():
    #hw()
    #sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[1]) #change as argv[1]
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    top_ten_hash = top_ten(tweet_file=sys.argv[1])
    sys.stdout.writelines('{0} {1}.0\n'.format(*pair) for pair in top_ten_hash) #print to stdout each hashtag-count pair, one per line                              
