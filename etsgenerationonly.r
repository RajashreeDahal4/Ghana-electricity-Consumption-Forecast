
library(forecast)
library(readxl)
data<- read.csv('electricity consumption and generation.csv')
main_data<-read.csv('consumption and generation.csv')
generation<- ts(main_data[,3],frequency=1)

library(Mcomp)
library(smooth)
library(greybox)
v<-ts(data[,4],frequency=1)
w<-ts(data[,5],frequency=1)
resu<-es(generation, model="AAN", h=20,holdout=FALSE,xreg=cbind(v,w))
plot(resu,main='forecasted',ylab='consumption',xlab='time in years')
result_fit<-resu[["fitted"]]
result_predict<-resu[["forecast"]]
write.csv(result_fit,'etsgenerationfit.csv')
write.csv(result_predict,'etsgenerationforecast.csv')
result_predict
result_fit


