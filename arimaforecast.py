# -*- coding: utf-8 -*-
"""Ghana Data visualization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HqPCXmSlvbdi9zGaF1i_L5M6eyKdFiRp
"""

from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline
import pandas as pd
import numpy as np
import tensorflow as tf
import os

path='/content/drive/MyDrive/final_data.xlsx'

import datetime
file_con=pd.read_excel(path,sheet_name='Electricity_consumption bilKWh')
file_con.head()
# file_dem=pd.read_excel(path,sheet_name='monthly demand')
# file_gen=pd.read_excel(path,sheet_name='monthly generation')
# file_pop=pd.read_excel(path,sheet_name='Population')
# file_gdp=pd.read_excel(path,sheet_name='GDP')
# file_con
# file_dem
# #file_gen
# file_pop
file_con

Year=file_con['Year']
GDP=file_con['GDP']
plt.plot(Year, GDP)
plt.title('GDP Vs Year')
plt.xlabel('Year')
plt.ylabel('GDP')
plt.show()

Year=file_con['Year']
consumption=file_con['consumption']
plt.plot(Year, consumption)
plt.title('Consumption Vs Year')
plt.xlabel('Year')
plt.ylabel('Energy consumption in Billion KWhr')
plt.show()

file_con["consumption"]

file_con.index=file_con.Year

file_con

file_con.plot()

Consumption=file_con['consumption']
year=file_con['Year']
plt.plot(year, Consumption)
plt.title('Electricity Consumption Vs Year')
plt.xlabel('Year')
plt.ylabel('Electricity Consumption in Billion KWhr')
plt.show()

file_con['consumption'].plot(figsize=(12,5))

from statsmodels.tsa.statespace.sarimax import SARIMAX
from random import random

file_con

exo.head()

exo=pd.DataFrame()
exo['GDP']=file_con['GDP']
exo['Population']=file_con['Population']
#

model = SARIMAX(file_con['consumption'], exog=exo, order=(0, 1, 0))
model_fit = model.fit(disp=0)
# make prediction
model_fit.summary()

year_test=pd.DataFrame()
year1_test=pd.DataFrame()
year2_test=pd.DataFrame()
year1_test['Year']=[2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030]
year1_test['population']=[31073288,31733971.14,32401361.46,33077321.32,33763515.8,34460942.18,35169753.19,35889398.16,36618983.73,37357690.11,38105083.99]
year1_test['GDP']=[7241275,7435832,7862798,8161794,8517739,8856511,9194350,9538885,9876703,10219340,10559160]
year1_test['GDP']=year1_test['GDP']*10000
year_test['Year']=year1_test['Year']
year2_test['GDP']=year1_test['GDP']
year2_test['Population']=year1_test['population']

year2_test.index=year1_test.Year

year2_test

year1_test.index=year1_test.Year

year1_test

file_con

file_con['Population'].append(year1_test['population'])

"""final touch"""

final=pd.DataFrame()
finlist=[final,file_con['Year'],forecast['Year']]

finresult['Year']=pd.concat(finlist)

finresult

year2_test

finresult.index=finresult.Year

exog2=year2_test

exogg=pd.DataFrame()
exoglist=[exogg,exo,exog2]

finalexog=pd.concat(exoglist)

finalexog

year1_test.drop('Year',axis=1,inplace=True)

year1_test
yearx=pd.DataFrame()
yearx["population"]=year1_test['population']
yearx["GDP"]=year1_test["GDP"]

year2_test.index=year1_test.index

year2_test

fen=pd.DataFrame()
fen['Year']=[1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]

year1_test.drop("Year",axis=1,inplace=True)

year2_test

import pandas as pd
#year1_test.index=year1_test.Year
forecast = model_fit.predict(start=40,end=40+len(year2_test)-1,exog=year2_test)
forecasted = pd.DataFrame(forecast,columns=['Prediction'])

forecasted.shape
#year2_test.shape

forecasted

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
# %matplotlib inline
model_fit.plot_diagnostics(figsize=(15,8))
plt.show()

forecast

finalexog

exo=pd.DataFrame()
exo['GDP']=file_con['GDP']
exo['Population']=file_con['Population']
#
#print(exog1)
model = SARIMAX(file_con['consumption'], exog=exo, order=(0, 1, 0))
model_fit2 = model.fit(disp=0)
# make prediction
model_fit2.summary()

year2_test

import pandas as pd
year1_test.index=year1_test.Year
forecast1 = model_fit2.predict(start=1,end=40)
forecasted1 = pd.DataFrame(forecast1,columns=['Prediction'])
result=pd.concat([forecasted1,forecasted])
#forecasted1.index=fen.Year
result

result.plot(label="Predicted")
file_con['consumption'].plot(ylabel='Electricity consumption in Billion KWhr',legend='Actual')

from sklearn.metrics import mean_absolute_error
expected = file_con['consumption'][1:]
print(expected.shape)
predictions = forecasted1[:]
print(predictions.shape)
mae = mean_absolute_error(expected, predictions)
print('MAE: %f' % mae)

from sklearn.metrics import mean_squared_error
expected = file_con['consumption'][:]
predictions = forecasted1[:]
mse = mean_squared_error(expected, predictions)
print('MSE: %f' % mse)

from sklearn.metrics import mean_squared_error
from math import sqrt
expected = file_con['consumption'][1:]
predictions = forecasted1[:]
mse = mean_squared_error(expected, predictions)
rmse = sqrt(mse)
print('RMSE: %f' % rmse)





import matplotlib.pyplot as plt
import statsmodels.api as sm
fig, ax = plt.subplots(2,1)
fig = sm.graphics.tsa.plot_acf(file_con['consumption'], lags=40, ax=ax[0])
fig = sm.graphics.tsa.plot_pacf(file_con['consumption'], lags=40, ax=ax[1])
plt.show()

model1 = sm.tsa.statespace.SARIMAX(file_con['consumption'], order=(0,1,0)).fit(max_iter=50, method='powell')

model1.summary()

res = model1.resid
fig, ax = plt.subplots(2,1)
fig = sm.graphics.tsa.plot_acf(res, lags=40, ax=ax[0])
fig = sm.graphics.tsa.plot_pacf(res, lags=40, ax=ax[1])
plt.show()

fitted_values = pd.Series(model_fit.fittedvalues, name="Fitted Values")

fitted_values

