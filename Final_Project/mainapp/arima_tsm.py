import statsmodels.tsa.stattools as ts
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.stattools import acf,pacf
import pandas as pd
import numpy as np
from nsepy import get_history
from sklearn.metrics import r2_score
from datetime import date
import os

def arima_tsm():
  prices = get_history(symbol='NIFTY 100', start = date(2009,2,1), end = date.today(), index = True)
  #edir_path = os.path.dirname(os.path.realpath(__file__))
  #epath = edir_path + '\\edata\\arima_emer.csv'
  #prices = pd.read_csv(epath)

  prices = prices[['Close']]
  tenyears = prices

  prices = prices[len(prices)-500:len(prices)]
   
  lenprice = len(prices)
  testval = prices.values

  lnprices = np.log(prices)

  acf_1 = acf(lnprices)
  ind = []
  for i in range(0,len(acf_1)):
    ind.append(i) 

  pacf_1 = pacf(lnprices)
  jnd =[]
  for j in range(0,len(pacf_1)):
    jnd.append(j)

  ln_diff = lnprices - lnprices.shift()
  diff = ln_diff.dropna() 
  
  acf_2 = acf(diff)
  ind2 = []
  for i2 in range(0,len(acf_2)):
    ind2.append(i2)

  pacf_2 = pacf(diff)
  jnd2 = []
  for j2 in range(0,len(pacf_2)):
    jnd2.append(j2)
  
  price_matrix = lnprices.as_matrix()
  print(len(price_matrix))
  model = ARIMA(price_matrix, order = (2,1,2))
  model_fit = model.fit(disp=0)
  pred = model_fit.predict(lenprice-100,lenprice, typ='levels')
  pred_adj = np.exp(pred)
  
  rsq = r2_score(pred_adj,testval[lenprice-101:])
  print(rsq)
  err=[]
  for x1,x2 in zip(testval[lenprice-2:],pred_adj[len(pred_adj)-3:len(pred_adj)-1]):
    err.append(x1-x2)
  print(err)
  return pred_adj[len(pred_adj)-1], tenyears,diff, ind,acf_1,jnd,pacf_1, ind2,acf_2,jnd2,pacf_2,pred_adj,testval[lenprice-100:] #12
  
