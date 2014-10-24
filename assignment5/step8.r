# Step 8: Construct confusion matrices

table(pred = predictions, true = testingdata$pop)

# Step 8: Sanity check the data

# Question 13 The variables in the dataset were assumed to be continuous, but one of them takes on only a few discrete values, suggesting a problem. Which variable exhibits this problem?
library(ggplot2)
p13 <- ggplot(MyData, aes(x = time , y = fsc_big ) )
p13 + geom_jitter(aes(color=pop))

ggplot(aes(x=time,y=pe,color=pop),data=MyData)+geom_jitter()

library(e1071)

MyDataFilted<- subset(MyData,file_id != 208)
set.seed(3456)
inTrainingSet <- createDataPartition(MyDataFilted$pop,p = 0.5,list=FALSE)
training <- MyDataFilted[inTrainingSet,]
testing <- MyDataFilted[-inTrainingSet,]
summary(training)

model_svm <- svm(fol, data=training)

predict_11c=predict(model_svm,newdata=testing,type= "class")
table(predict_11c, testing$pop)

confusionMatrix(predict_11c, testing$pop)





