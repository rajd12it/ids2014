import sys
import json

def hw():
    print 'Hello, Twitter!'

def lines(fp):
    print str(len(fp.readlines()))

scores = {}  #empty dictionary to store scores for each word

#sent_file
with open(sys.argv[1]) as f:
    for line in f:
        term, score=line.split("\t") #the file is tab-delimited. "\t" means "tab character"
        scores[term]=int(score) #convert the score to an integer
        #print scores.items() #print every (term, score) pair in the dictionary
        #print type(term)
        #print type(score)

#tweet_file
with open(sys.argv[2]) as f:
    for line in f:
        js = json.loads(line) #load to json
        tweet=js.get('text',"") #find key type
        tweet=tweet.encode('utf-8') #convert to utf
        tweet=tweet.lower() #change to lowercase
        #print tweet
        if tweet:
            tweet_score = sum(scores.get(word,0) for word in tweet.split()) #sum the tweet scores
            print tweet_score

def main():
    #hw()
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
