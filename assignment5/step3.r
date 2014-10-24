# Step 3: Plot the data

# install library for recommneded function 'ggplot'
#library(ggplot2)

# use function 'ggplot' to plot pe against chl_small 
plot <- ggplot(MyData, aes(x = chl_small, y = pe ) )

# color by pop - Line Plot
plot + geom_line(aes(colour = pop))

# color by pop - Jitter Plot
ggplot(aes(x=chl_small,y=pe,color=pop),data=MyData)+geom_jitter()



