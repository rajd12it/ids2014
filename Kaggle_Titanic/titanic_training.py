# The first thing to do is to import the relevant packages
# that I will need for my script, 
# these include the Numpy (for maths and arrays)
# and csv for reading and writing csv files
# If i want to use something from this I need to call 
# csv.[function] or np.[function] first

import csv as csv 
import numpy as np

# Open up the csv file in to a Python object
csv_file_object = csv.reader(open('/home/user/datasci_course_materials/Kaggle_Titanic_Competition/train.csv', 'rb')) 
# The next() command just skips the first line which is a header
header = csv_file_object.next()   
# Create a variable called 'data'                                  
data=[]             
# Run through each row in the csv file, adding each row to the data variable         
for row in csv_file_object: 
    # Then convert from a list to an array. Be aware that each item is currently a string in this format    
    data.append(row)             
data = np.array(data) 

#print data
#print data[0]
#print data[-1] 
#print data[0::,1]
#print data[0::,4]       
#print data[0::,2].astype(np.float) 

# The size() function counts how many elements are in in the array and sum() (as you would expects) sums up the elements in the array.

number_passengers = np.size(data[0::,1].astype(np.float))
#print number_passengers
number_survived = np.sum(data[0::,1].astype(np.float))
#print number_survived
proportion_survivors = number_survived / number_passengers  
#print proportion_survivors 

# This index finds and stores where all the gender column equals and does not equal female
women_only_stats = data[0::,4] == "female"
#print women_only_stats
men_only_stats = data[0::,4] != "female"
#print men_only_stats

# Using the index from above we select the females and males separately
women_onboard = data[women_only_stats,1].astype(np.float) 
#print women_onboard    
men_onboard = data[men_only_stats,1].astype(np.float)
#print men_onboard

# Then we finds the proportions of them that survived
proportion_women_survived = \
                       np.sum(women_onboard) / np.size(women_onboard)  
proportion_men_survived = \
                       np.sum(men_onboard) / np.size(men_onboard) 

# and then print it out
print 'Proportion of women who survived is %s' % proportion_women_survived
print 'Proportion of men who survived is %s' % proportion_men_survived
                                                           
