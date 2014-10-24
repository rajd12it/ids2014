# Step 2: Split the data into test and training sets

# Install library caret in R (setup.r) installs it elsewhere and so you have to install it once in R (>) prompt
library(caret)

# results for above
## Loading required package: lattice
## Loading required package: ggplot2

# set.seed - not sure what this does??
#set.seed(3456)

# Divide the data into two equal subsets, one for training and one for testing. Make sure to divide the data in an unbiased manner.
partition <- createDataPartition(MyData$pop,p = 0.5,list=FALSE)
training <- MyData[partition,]
testing <- MyData[-partition,]

# summary for mean of the variable “time” for your training set
summary(training)

