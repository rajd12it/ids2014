# Step 5: Evaluate the decision tree on the test data

# Use predict function
predictA=predict(modelA,newdata=testing)
# print/parse as string
str(predictA)

# Test pop for all pop values and load to resultA
pop_testA=c()
pop_names=c("crypto","nano","pico","synecho","ultra")
for (i in 1:nrow(predictA)){
        pop_testA=c(pop_testA,pop_names[which.max(predictA[i,])])
        } 
resultA=as.vector(testing$pop)==pop_testA
# print as a table
table(resultA)

#results are below
#resultA
#FALSE  TRUE 
#5187 30984 

# simple/aternative way
accuracyA=sum(resultA)/length(pop_testA)
# predictA2
predictA2=predict(modelA,newdata=testing,type= "class")
table(predictA2, testing$pop)

#predictA2 crypto nano pico synecho ultra
  #crypto       0    0    0       0     0
  #nano        51 4977    0      16   637
  #pico         0    3 9391      16  1936
  #synecho      0   34   38    9041   120
  #ultra        0 1335 1001       0  7575


# Predict A2 via. a confusion matrix
confusionMatrix(predictA2, testing$pop)

#Confusion Matrix and Statistics

#          Reference
#Prediction crypto nano pico synecho ultra
   #crypto       0    0    0       0     0
   #nano        51 4977    0      16   637
   #pico         0    3 9391      16  1936
   #synecho      0   34   38    9041   120
   #ultra        0 1335 1001       0  7575

#Overall Statistics
                                          
#               Accuracy : 0.8566          
#                 95% CI : (0.8529, 0.8602)
#    No Information Rate : 0.2884          
#    P-Value [Acc > NIR] : < 2.2e-16       
                                          
#                  Kappa : 0.8063          
# Mcnemar's Test P-Value : NA              

#Statistics by Class:

#                     Class: crypto Class: nano Class: pico Class: synecho
#Sensitivity                0.00000      0.7839      0.9004         0.9965
#Specificity                1.00000      0.9764      0.9241         0.9929
#Pos Pred Value                 NaN      0.8761      0.8277         0.9792
#Neg Pred Value             0.99859      0.9550      0.9581         0.9988
#Prevalence                 0.00141      0.1755      0.2884         0.2508
#Detection Rate             0.00000      0.1376      0.2596         0.2500
#Detection Prevalence       0.00000      0.1571      0.3137         0.2553
#Balanced Accuracy          0.50000      0.8801      0.9122         0.9947
#                     Class: ultra
#Sensitivity                0.7377
#Specificity                0.9098
#Pos Pred Value             0.7643
#Neg Pred Value             0.8974
#Prevalence                 0.2839
#Detection Rate             0.2094
#Detection Prevalence       0.2740
#Balanced Accuracy          0.8238





