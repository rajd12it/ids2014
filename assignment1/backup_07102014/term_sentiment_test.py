import sys
import json
import collections

def hw():
    print 'Hello, Twitter!'

def lines(fp):
    print str(len(fp.readlines()))

#scores_dict
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
        score_tweet(tweet, scores) = sum(scores.get(word,0) for word in tweet
        #print tweet_score    
        print score_tweet.items()        
	 #word_score = score_tweet(tweet, scores) / len(tweet)
         #print word_score
	    #ct = collections.Counter(tweet_score)
            #print ct
	    #tweet_line = tweet.split()
            #for i in range(len(tweet_line)):
            #for word in tweet_line: 
                 #if scores.get(word) == None:
                  #print word
                  #non_sent_scores[word] += int(tweet_score)
                  #print non_sent_scores.items()
                  #else:
                  #non_sent_scores[word] = int(tweet_score)
                  #print non_sent_scores[word]
                  #if i > 2 and i < len(tweet_line) - 2:
                  #print tweet_line[i], tweet_line[i+1], tweet_line[i+2]
                  #print scores.get(tweet_line[i-1],0), scores.get(tweet_line[i-2],0), scores.get(tweet_line[i+1],0), scores.get(tweet_line[i+2],0)     
                  #elif i >= len(tweet_line) - 2:
 		   #print scores.get(tweet_line[i-1],0), scores.get(tweet_line[i-2],0)
                   #elif i < 2:
                   #print scores.get(tweet_line[i+1],0), scores.get(tweet_line[i+2],0)
            
def main():
    #hw()
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
