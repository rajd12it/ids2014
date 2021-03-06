from __future__ import division #from future division library to display sentiment:float
import sys
import json

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
    return sum(scores.get(word, 0) for word in tweet) #sum of tweet score based on sent_file, default is 0

#tweet_file, non_sent_word_scores
def non_sent_word_scores(tweet_file, scores):
    with open(tweet_file) as f:
        js = (json.loads(line).get('text', '').split() for line in f) #load to json, text type and split the tweet
        #tweet=tweet.encode('utf-8') #convert to utf
        #tweet=tweet.lower() #change to lowercase
        #print tweet 
        return {word: tweet_score(tweet, scores) / len(tweet) #divide tweet_score by length of tweet
                for tweet in js if tweet
                for word in tweet if word not in scores}

def main():
    #hw()
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    scores = sent_scores(sent_file=sys.argv[1])
    sys.stdout.writelines('{0} {1}\n'.format(word.encode('utf-8'), score) #convert tweet word to utf and display score for each
                          for word, score in non_sent_word_scores(
                              tweet_file=sys.argv[2],
                              scores=scores).items())
