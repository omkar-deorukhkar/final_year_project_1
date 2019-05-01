import senti
import lstm_nn
import arima_tsm
import ffnn
import os
import matplotlib.pyplot as plt
from math import floor,ceil
from matplotlib.pyplot import figure
from matplotlib.font_manager import FontProperties
plt.style.use('ggplot')
from tkinter import *
from datetime import datetime


def master_process(tick):
	pred,nif,orig,corr, main_op, main_corr, hist_plot,y_traina, five_day_md = lstm_nn.lstmnn(tick,50)
	forcst, tenyears,diff, ind,acf_1,jnd,pacf_1, ind2,acf_2,jnd2,pacf_2,pred_adj,testval = arima_tsm.arima_tsm()
	score_senti = senti.sentiment_analysis(tick)

	final_pred, prices_a, rsq = ffnn.ffnn(400,pred,nif,orig,corr,main_op,forcst)

	next_day_pred = five_day_md*score_senti + final_pred[-1][0]

	time_curr = (str(datetime.now()))
	time_stamp = time_curr[-6:]

	figure(figsize=(16,7))

	plt.tight_layout()
	plt.subplots_adjust(left=0.1, bottom=0.1, right=0.92, top=0.95, wspace=0.2, hspace=0.25)

	plt.subplot(2,4,1)
	plt.title('LSTM Loss MSE',fontsize=6)
	plt.plot(hist_plot,color='red',label='loss MSE')
	plt.xlabel('Epoch Number',fontsize=6)
	plt.ylabel('Loss',fontsize=6)
	plt.legend(prop={'size': 6})
	plt.xticks(fontsize=6)
	plt.yticks(fontsize=6)


	plt.subplot(2,4,2)
	plt.title('NIFTY 100 6 years',fontsize=6)
	ty = tenyears.values
	plt.plot(ty,color='blue',label='NIFTY-100 shows upward trend and seasonality')
	plt.xlabel('Observation Points (DAYS)',fontsize=6)
	plt.ylabel('NIFTY-100',fontsize=6)
	plt.legend(prop={'size': 6})
	plt.xticks(fontsize=6)
	plt.yticks(fontsize=6)


	plt.subplot(2,4,3)

	plt.bar(ind,acf_1,color='blue', label='We can observe steady decrease in AC')
	plt.title('ACF of Undifferenced Series',fontsize=6)
	plt.xlabel('Observation point',fontsize=6)
	plt.ylabel('Auto Covariance',fontsize=6)
	plt.legend(prop={'size': 6})
	plt.xticks(fontsize=6)
	plt.yticks(fontsize=6)


	plt.subplot(2,4,4)
	plt.bar(jnd,pacf_1,color='blue', label='We can Observe Sudden drop in PAC')
	plt.title('PACF of Undifferenced Series',fontsize=6)
	plt.xlabel('Observation point',fontsize=6)
	plt.ylabel('Partial Auto Covariance',fontsize=6)
	plt.legend(prop={'size': 6})
	plt.xticks(fontsize=6)
	plt.yticks(fontsize=6)

	plt.subplot(2,4,5)

	plt.bar(ind2,acf_2,color='green',label = 'AC values for d=1, p=2')
	plt.title('ACF plot for First Differencing',fontsize=6)
	plt.xlabel('Observation Points',fontsize=6)
	plt.ylabel('Auto Covariance Values',fontsize=6)
	plt.legend(prop={'size': 6})
	plt.xticks(fontsize=6)
	plt.yticks(fontsize=6)



	plt.subplot(2,4,6)


	plt.bar(jnd2,pacf_2,color='green',label = 'PAC values for d=1, q=2')
	plt.title('PACF plot for First Differencing',fontsize=6)
	plt.xlabel('Observation Points',fontsize=6)
	plt.ylabel('Partial Auto Covariance Values',fontsize=6)
	plt.legend(prop={'size': 6})
	plt.xticks(fontsize=6)
	plt.yticks(fontsize=6)

	plt.subplot(2,4,7)

	plt.plot(pred_adj, color='green', label='ARIMA(2,1,2) Forecast')
	plt.plot(testval,color='grey', label='NIFTY-100')
	plt.title('ARIMA(2,1,2) Forecast',fontsize=6)
	plt.xlabel('Observation points(Days)',fontsize=6)
	plt.ylabel('NIFTY-60',fontsize=6)
	plt.legend(prop={'size': 6})
	plt.xticks(fontsize=6)
	plt.yticks(fontsize=6)

	plt.subplot(2,4,8)
	plt.plot(final_pred, color='green',label='predicted')
	plt.plot(prices_a, color='black',label='actual')
	plt.xlabel('Observation Points (DAYS)',fontsize=6)
	plt.ylabel('Value',fontsize=6)
	plt.legend(prop={'size': 6})
	plt.xticks(fontsize=6)
	plt.yticks(fontsize=6)

	plt.suptitle('Graphs ' + tick, fontsize=12)

	dir_path = os.path.dirname(os.path.realpath(__file__))
	save_path = dir_path + '\static\output' + time_stamp + '.png'
	img_name = 'output' + time_stamp + '.png'

	plt.savefig(save_path)
	plt.close()

	return next_day_pred, rsq, img_name