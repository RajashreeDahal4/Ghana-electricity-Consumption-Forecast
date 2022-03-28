library(forecast)
library(readxl)
data<- read.csv('demandforecast.csv')
spy<- ts(data[,2],frequency=12)
library(Mcomp)
library('smooth')
library('greybox')
x<-ts(data[,3],frequency=12)
resu<-es(spy, model="AAA", h=36,holdout=FALSE, xreg=cbind(x))
plot(resu,main='forecasted',ylab='consumption',xlab='time in years')
plot
forecast<-predict(resu,newdata=spy)
forecast
fit<-resu[['fitted']]
write.csv(fit,'gdemandfit.csv')
forecas<-resu[['forecast']]
write.csv(forecas,'gdemandforecast.csv')