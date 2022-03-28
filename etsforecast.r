
library(forecast)

library(readxl)
data<- read.csv('1980 gen.csv')
spy<- ts(data[,2],frequency=1)
holt<-holt(spy,h=12)
plot(holt,main='forecasted',ylab='consumption',xlab='time in years')

library(Mcomp)
library('smooth')
library('greybox')
x<-ts(data[,4],frequency=1)
y<-ts(data[,3],frequency=1)
resu<-es(spy, model="AAN", h=10, holdout=FALSE)
plot(results,main='forecasted',ylab='consumption',xlab='time in years')
plot
exog2
exog1<-holt[['fitted']]
write.csv(exog2,'1980fit.csv')