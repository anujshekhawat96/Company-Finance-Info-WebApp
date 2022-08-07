import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import array
from sklearn.preprocessing import StandardScaler
import pandas_datareader as data 



import streamlit as st

import yfinance as yf

from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly

#import Prophet as ph
#from fbprophet.plot import plot_plotly
from datetime import date 

from plotly import graph_objs as go


START = '2017-01-01'

TODAY= date.today().strftime("%Y-%m-%d")


st.title('Company Financial Info')

stocks = st.text_input('Enter Company Stock Ticker', 'AAPL')

#stocks = ('AAPL','GOOG','MSFT')
selected_stocks = stocks 


@st.cache
def load_data(ticker):
    data = yf.download(ticker)
    data.reset_index(inplace=True)
    return data


#data_load_state = st.text("Load data...")

data = load_data(selected_stocks)
#data_load_state.text("Data Loading is Done...Thanks of your patience!")


# Plot raw data
def plot_raw_data():
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
	fig.layout.update(title_text='Stock Price Open and Close Information', xaxis_rangeslider_visible=True)
	st.plotly_chart(fig)
	
plot_raw_data()

csv0 = data.to_csv(index=False)

st.download_button('Download Stock Data', csv0, file_name='StockData.csv')

##TICKER VALUE
ticker_pass = yf.Ticker(selected_stocks)





##SHOW MAJOR HOLDERS

major_hold = ticker_pass.major_holders
st.subheader('Stakeholders Distribution')
st.write(major_hold)

csv = major_hold.to_csv(index=False)

st.download_button('Download Stakeholders Data', csv, file_name='StakeholderDistributionData.csv')


#major_hold.to_excel('major_holdings.xlsx', sheet_name='majorholdings', index=False)

# show institutional holders
inst_hold = ticker_pass.institutional_holders
st.subheader('Institutional Stakeholders')
st.write(inst_hold)

csv1 = inst_hold.to_csv(index=False)

st.download_button('Download Institutional Stakeholders Data', csv1, file_name='InstitutionalStakeholderData.csv')

##SHow financials 
quaterly_fin = ticker_pass.quarterly_financials
st.subheader('Quaterly Financials')
st.write(quaterly_fin)

csv2 = quaterly_fin.to_csv(index=False)

st.download_button('Download Quaterly Financials Data', csv2, file_name='QuaterlyFinancialData.csv')



# show balance sheet

st.subheader('Quaterly Balance Sheet')
balancesheet_quater = ticker_pass.quarterly_balance_sheet

st.write(balancesheet_quater)

csv3 = balancesheet_quater.to_csv(index=False)

st.download_button('Download Quaterly Balance Sheet Data', csv3, file_name='QuaterlyBalanceSheetData.csv')

# show cashflow

st.subheader('Quaterly CashFlow')
quatercash = ticker_pass.quarterly_cashflow
st.write(quatercash)

csv4 = quatercash.to_csv(index=False)

st.download_button('Download Quaterly Cashflow', csv4, file_name='QuaterlyCashFlow.csv')



# show earnings
st.subheader('Quaterly Earnings')
earn = ticker_pass.quarterly_earnings
st.write(earn)

csv5 = earn.to_csv(index=False)

st.download_button('Download Quaterly Earning Data', csv5, file_name='QuaterlyEarning.csv')


# show analysts recommendations
st.subheader('Analyst Recommendations')
recom = ticker_pass.recommendations
st.write(recom)

csv6 = recom.to_csv(index=False)

st.download_button('Download Analyst Recommendation Data', csv6, file_name='AnalystRecommendation.csv')


# show dividend nd stock split
st.subheader('Dividends and Stock Splits')
divi = ticker_pass.actions
st.write(divi)

csv7 = divi.to_csv(index=False)

st.download_button('Download Dividend and Stock Splits Data', csv7, file_name='StockSplit.csv')

# show earning dates
st.subheader('Earning Dates')
earning_dates = ticker_pass.earnings_dates
st.write(earning_dates)

csv8 = earning_dates.to_csv(index=False)

st.download_button('Download Earning Dates', csv8, file_name='Earning_dates.csv')


# show options expirations

st.subheader('Options')
options_tick = ticker_pass.options
st.write(options_tick)

csv9 = options_tick.to_csv(index=False)

st.download_button('Download Options', csv9, file_name='options.csv')


##Non Fin Info

emp = ticker_pass.info['fullTimeEmployees']
st.subheader('Company Non Financial Info')


sector = ticker_pass.info['sector']
addrs = ticker_pass.info['address1']
hqcity = ticker_pass.info['city']
hqcountry = ticker_pass.info['country']


web = ticker_pass.info['website']



st.write('Full Time Employees: ', emp)
st.write('Sector: ', sector)
st.write('Address: ', addrs)
st.write('City: ', hqcity)
st.write('Country: ', hqcountry)

st.write('Website: ', web)
