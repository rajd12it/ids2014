# Step 7: Train a support vector machine model and compare results

# Use the e1071 library and call model <- svm(fol, data=trainingdata)
library(e1071)
model_svm <- svm(fol, data=training)

# predict same as step5.r
# Use predict function
predictC=predict(model_svm,newdata=testing)
# print/parse as string
str(predictC)

# Test pop for all pop values and load to resultA - Below for loop throws an error 'Error in 1:nrow(predictB) : argument of length 0'
#pop_testC=c()
#pop_names=c("crypto","nano","pico","synecho","ultra")
#for (i in 1:nrow(predictC)){
#        pop_testC=c(pop_testC,pop_names[which.max(predictC[i,])])
#       } 
#resultC=as.vector(testing$pop)==pop_testC
# print as a table
#table(resultC)

#results from above fail - table of extent 0 >

# simple/aternative way - Works!
accuracyC=sum(resultC)/length(pop_testC)
# predictC2
predictC2=predict(model_svm,newdata=testing,type= "class")
table(predictC2, testing$pop)

# results from above simple/alternative method
#predictC2 crypto  nano  pico synecho ultra
  #crypto      45     0     0       0     0
  #nano         4  5627     0       3   389
  #pico         0     0 10016      26  1314
  #synecho      2     2    62    9037     3
  #ultra        0   720   352       7  8562

# Predict C2 via. a confusion matrix - method gives summarized accuracy for each pop value
confusionMatrix(predictC2, testing$pop)

# results from confusion matrix
#Confusion Matrix and Statistics

#          Reference
#Prediction crypto  nano  pico synecho ultra
#   crypto      45     0     0       0     0
#   nano         4  5627     0       3   389
#   pico         0     0 10016      26  1314
#   synecho      2     2    62    9037     3
#   ultra        0   720   352       7  8562

#Overall Statistics
                                         
#               Accuracy : 0.9203         
#                 95% CI : (0.9174, 0.923)
#    No Information Rate : 0.2884         
#    P-Value [Acc > NIR] : < 2.2e-16      
                                         
#                  Kappa : 0.8925         
# Mcnemar's Test P-Value : NA             

#Statistics by Class:

#                     Class: crypto Class: nano Class: pico Class: synecho
#Sensitivity               0.882353      0.8863      0.9603         0.9960
#Specificity               1.000000      0.9867      0.9479         0.9975
#Pos Pred Value            1.000000      0.9343      0.8820         0.9924
#Neg Pred Value            0.999834      0.9761      0.9833         0.9987
#Prevalence                0.001410      0.1755      0.2884         0.2508
#Detection Rate            0.001244      0.1556      0.2769         0.2498
#Detection Prevalence      0.001244      0.1665      0.3140         0.2517
#Balanced Accuracy         0.941176      0.9365      0.9541         0.9967
#                     Class: ultra
#Sensitivity                0.8339
#Specificity                0.9583
#Pos Pred Value             0.8881
#Neg Pred Value             0.9357
#Prevalence                 0.2839
#Detection Rate             0.2367
#Detection Prevalence       0.2665
#Balanced Accuracy          0.8961

# A random forest can obtain another estimate of variable importance based on the Gini impurity that we discussed in the lecture.
# The function importance(model) prints the mean decrease in gini importance for each variable. 
# The higher the number, the more the gini impurity score decreases by branching on this variable, indicating that the variable is more important.
#importance(model_svm) - does not apply to this decision tree

# results
#          MeanDecreaseGini
#fsc_small        2712.1304
#fsc_perp         2016.7490
#fsc_big           204.9428
#pe               8968.2031
#chl_big          4797.9997
#chl_small        8154.8962


