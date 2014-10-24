import sys
import json

def hw():
    print 'Hello, Twitter!'

def lines(fp):
    print str(len(fp.readlines()))

#AFINN
afinnfile=open("AFINN-111.txt")
scores={} # initialize an empty dictionary
for line in afinnfile:
    term, score=line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    scores[term]=int(score)  # Convert the score to an integer.
    #print scores.items() # Print every (term, score) pair in the dictionary
    #print type(term)
    #print type(score)

#Tweet
outputfile=open("output.txt")
tweet_scores={} # initialize an empty dictionary
for line in outputfile:
    js=json.loads(line)
    tweet=js.get('text',"")
    tweet=tweet.encode('utf-8')
    tweet=tweet.lower()
    #print tweet


       
  
def main():
    sent_file=open(sys.argv[1])
    tweet_file=open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
