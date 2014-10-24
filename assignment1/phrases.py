#This reports back the phrases that have a blank space in the AFINN-111.txt file
num = 0
sent_list = open("AFINN-111.txt")
for line in sent_list:
    if " " in line: #check for blank space
       print line
       num += 1
print num
