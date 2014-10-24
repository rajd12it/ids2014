# Step 6: Build and evaluate a random forest

#Load the randomForest library outside R
#install.packages("randomForest")

# load library random forest
library(randomForest)

# create a new model with random forest
modelB <- randomForest(fol, data=training)

# predict same as step5.r
# Use predict function
predictB=predict(modelB,newdata=testing)
# print/parse as string
str(predictB)

# Test pop for all pop values and load to resultA - Below for loop throws an error 'Error in 1:nrow(predictB) : argument of length 0'
#pop_testB=c()
#pop_names=c("crypto","nano","pico","synecho","ultra")
#for (i in 1:nrow(predictB)){
#        pop_testB=c(pop_testB,pop_names[which.max(predictB[i,])])
#        } 
#resultB=as.vector(testing$pop)==pop_testB
# print as a table
#table(resultB)

#results from above fail - table of extent 0 >

# simple/aternative way - Works!
accuracyB=sum(resultB)/length(pop_testB)
# predictB2
predictB2=predict(modelB,newdata=testing,type= "class")
table(predictB2, testing$pop)

# results from above simple/alternative method
#predictB2 crypto  nano  pico synecho ultra
  #crypto      50     1     0       0     0
  #nano         0  5559     0       2   357
  #pico         0     0 10047       2  1357
  #synecho      1     3    12    9068     4
  #ultra        0   786   371       1  8550

# Predict B2 via. a confusion matrix - method gives summarized accuracy for each pop value
confusionMatrix(predictB2, testing$pop)

# results from confusion matrix
#Confusion Matrix and Statistics

#          Reference
#Prediction crypto  nano  pico synecho ultra
#   crypto      50     1     0       0     0
#   nano         0  5559     0       2   357
#   pico         0     0 10047       2  1357
#   synecho      1     3    12    9068     4
#   ultra        0   786   371       1  8550

#Overall Statistics
                                          
#               Accuracy : 0.9199          
#                 95% CI : (0.9171, 0.9227)
#    No Information Rate : 0.2884          
#    P-Value [Acc > NIR] : < 2.2e-16       
                                          
#                  Kappa : 0.8919          
# Mcnemar's Test P-Value : NA              

#Statistics by Class:

#                     Class: crypto Class: nano Class: pico Class: synecho
#Sensitivity               0.980392      0.8756      0.9633         0.9994
#Specificity               0.999972      0.9880      0.9472         0.9993
#Pos Pred Value            0.980392      0.9393      0.8809         0.9978
#Neg Pred Value            0.999972      0.9739      0.9845         0.9998
#Prevalence                0.001410      0.1755      0.2884         0.2508
#Detection Rate            0.001382      0.1537      0.2778         0.2507
#Detection Prevalence      0.001410      0.1636      0.3153         0.2513
#Balanced Accuracy         0.990182      0.9318      0.9552         0.9994
#                     Class: ultra
#Sensitivity                0.8327
#Specificity                0.9553
#Pos Pred Value             0.8807
#Neg Pred Value             0.9351
#Prevalence                 0.2839
#Detection Rate             0.2364
#Detection Prevalence       0.2684
#Balanced Accuracy          0.8940

# A random forest can obtain another estimate of variable importance based on the Gini impurity that we discussed in the lecture.
# The function importance(model) prints the mean decrease in gini importance for each variable. 
# The higher the number, the more the gini impurity score decreases by branching on this variable, indicating that the variable is more important.
importance(modelB)

# results
#          MeanDecreaseGini
#fsc_small        2712.1304
#fsc_perp         2016.7490
#fsc_big           204.9428
#pe               8968.2031
#chl_big          4797.9997
#chl_small        8154.8962



