from __future__ import division #from future division library to display sentiment:float
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
def freq(tweet_file):
    with open(tweet_file) as f:
        js = (json.loads(line).get('text', '').split() for line in f) #load to json, text type and split the tweet
        #tweet=tweet.encode('utf-8') #convert to utf
        #tweet=tweet.lower() #change to lowercase
        #print tweet 
        return Counter(word for tweet in js for word in tweet) #counter for word in tweet
        #return {word: tweet_score(tweet, scores) / len(tweet) #divide tweet_score by length of tweet
                #for tweet in js if tweet
                #for word in tweet if word not in scores}

def main():
    #hw()
    #sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[1]) #change as argv[1]
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    freq_tweet = freq(tweet_file=sys.argv[1])
    total_freq_tweet = sum(freq_tweet.values()) #no of occurances of all words in all tweets
    sys.stdout.writelines('{0} {1}\n'.format(word.encode('utf-8'), freq_tweet[word] / total_freq_tweet ) #convert tweet word to utf and calculate frequency of each word in tweet by all words in tweet
                          for word in freq_tweet)
                              
