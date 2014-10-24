# Step 4: Train a decision tree

# Install the rpart library
library(rpart)

# Use the formula function to construct the formula object for output of Pop
# Train a tree as a function of the sensor measurements: fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small
fol <- formula(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small)
# Create a model
modelA <- rpart(fol, method="class", data=training)
# Print Model - we know from the print result - which populations, if any, is your tree "incapable" of recognizing: all the pop values are there except crypto
print(modelA)

# partykit enchance the plotting functions for recursive partitioning by means of plotting a decision tree
# Need to be installed outside R 
install.packages("partykit")
# partykit is then a valid library - installs package grid to create the object called depth
library(partykit)

# We can convert the rpart object to a new class called party and plot it to see more in the terminal nodes
rpartA <- as.party(modelA)
# Plot rpartA
plot(rpartA)

# additional rpart.plot function for a different plot
# Need to be installed outside R 
install.packages("rpart.plot")
# rpart.plot is then a valid library
library(rpart.plot)
# Plot with rpart.plot - threshold value for pe that sends to the next branches based on a threshold value < 'x' and >= 'x'. What is 'x'. see result from below and compare to the result from the print(modelA) for pe brances 
rpart.plot(modelA,branch=0,branch.type=2,type=1,extra=102,shadow.col="pink",box.col="gray",split.col="magenta")
# Plot with rpart.plot - different colors
#rpart.plot(modelA,branch=0,branch.type=2,type=1,extra=102,shadow.col="pink",box.col="green",split.col="red")





