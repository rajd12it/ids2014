# The first thing to do is to import the relevant packages
# that I will need for my script, 
# these include the Numpy (for maths and arrays)
# and csv for reading and writing csv files
# If i want to use something from this I need to call 
# csv.[function] or np.[function] first

import csv as csv 
import numpy as np

# Open and read the test file in to a Python object
test_file = open('/home/user/datasci_course_materials/Kaggle_Titanic_Competition/test.csv', 'rb')
test_file_object = csv.reader(test_file) 
# The next() command just skips the first line which is a header
header = test_file_object.next()  

# Open and write the the prediction file in to a Python object
prediction_file = open("genderbasedmodel.csv", "wb")
prediction_file_object = csv.writer(prediction_file)


# Read in the test file row by row, see if male or female and write survival prediction to the prediction Python object
prediction_file_object.writerow(["PassengerId", "Survived"])
# For each row in test.csv
for row in test_file_object: 
    # is it a female, if yes then  
    if row[3] == 'female': 
        # predict 1                                       
        prediction_file_object.writerow([row[0],'1']) 
    # or else if male,  
    else:  
        # predict 0                                   
        prediction_file_object.writerow([row[0],'0'])    
test_file.close()
prediction_file.close()
                                                           
