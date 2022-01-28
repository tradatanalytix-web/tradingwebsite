import streamlit as st
import numpy as np
import pandas as pd
import sqlite3
import time
import requests
import streamlit.components.v1 as components
import plotly.express as px
from datetime import date, datetime
from Myround import myround
from fnodataupdate import fnodata
import SessionState
from filterdata_fun import filtered_data
from oichart_fun import oi_chart_graph
from coichart_fun import coi_chart_graph
from fiidiidatanalysis import fiidiidata
from streamlit import caching
from get_cmp_fun import get_cmp
from fii_chart_fun import get_fii_chart
from filterclientdat_fun import filterclientdat
from pcr_fun import pcr_cal
from optionspayoff import ironbutterfly
from call_option import call_payoff
from put_option import put_payoff
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')
import plotly.express as px
from chart_studio import plotly as py
from streamlit_option_menu import option_menu
from plotly.offline import plot
import plotly.graph_objects as go
import yfinance as yf
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt
import cufflinks as cf
from datetime import date
from datetime import timedelta
from realtime_optionchain import oc
import json
from os import name
from intradaycharts import volume_profile
#from pynse import *
import logging
import mplfinance as mpf
#from alice_blue import *
import dateutil.parser


#nse=Nse()

st.set_page_config(page_title = 'TraDatAnalytix',layout='wide', page_icon='💹')

#with open('style.css') as f:
#  st.markdown(f'<style>{f.read()}<style>', unsafe_allow_html=True)

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
  <a class="navbar-brand" href="https://www.youtube.com/channel/UCw2H-l2iNaRjXapU-mrJZXQ" target="_blank">TraDatAnalytix</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://www.youtube.com/channel/UCw2H-l2iNaRjXapU-mrJZXQ" target="_blank">YouTube</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://twitter.com/PitanjalDatta" target="_blank">Twitter</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

session_state = SessionState.get(
    button1_clicked=False,
    button2_clicked=False,
    button3_clicked=False,
    home_button = False
)

tday = st.sidebar.date_input('Date Input')
previous_Date = tday - timedelta(days = 180)

lc, mc, rc = st.columns(3)


with st.sidebar:
  selected_option = option_menu(
    "TraDatAnalytix",
    ['*BUDGET SPECIAL*','Home','Charts','Real time OI','Open Interest', 'FII/DII Data', 'Trading Strategy'],
    icons = ['bank2','house-fill','option','bar-chart-fill','bar-chart-fill', 'gear', 'option'],
    menu_icon = "cast",
    default_index = 0
  )

if selected_option == "*BUDGET SPECIAL*":


    st.set_option('deprecation.showPyplotGlobalUse', False)
    
    st.title("Nifty Post Budget - Trading Strategy")

    with st.expander("See Trading Strategy"):
     st.write("""
         1. Check Budget Day Closing, whether Green Candle or Red Candle, at 3:15 pm on Budget Day.
         2. If its a GREEN candle at 3:15 pm of Budget day, mark the LOW of Budget day, and SELL PUT option strike price nearest to the LOW price.
         3. If its a RED candle at 3:15 pm of Budget day, mark the HIGH of Budget day, and SELL CALL option strike price nearest to the HIGH price.
         4. Apart from 2020, this strategy worked every year from 2015 to 2021.
     """)


    # Nifty 2015 Analysis

    df2015_nifty = yf.download('^NSEI', interval="1d", start="2015-01-15", end="2015-02-15")
    df2015_nifty['Date'] = pd.to_datetime(df2015_nifty.index)
    df2015_nifty['Date'] = df2015_nifty['Date'].apply(mpl_dates.date2num)

    df2015_nifty = df2015_nifty.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]
    #df2016 = nse.get_hist('NIFTY 50', from_date=dt.date(2016,1,15),to_date=dt.date(2016,2,15))
    vls=['2015-02-12']
    ga1 = mpf.plot(df2015_nifty, type="candle", style = "yahoo", 
                  #alines=two_points, 
                  vlines=dict(vlines=vls,colors='c', linewidths=255,alpha=0.4),
                  hlines=8840.80)
    #g1 = mpf.plot(df2016_nifty, type="candle", style = "yahoo")
    st.pyplot(ga1)

    
    
    
    
    # Nifty 2016 Analysis

    df2016_nifty = yf.download('^NSEI', interval="1d", start="2016-01-15", end="2016-02-15")
    df2016_nifty['Date'] = pd.to_datetime(df2016_nifty.index)
    df2016_nifty['Date'] = df2016_nifty['Date'].apply(mpl_dates.date2num)

    df2016_nifty = df2016_nifty.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]
    #df2016 = nse.get_hist('NIFTY 50', from_date=dt.date(2016,1,15),to_date=dt.date(2016,2,15))
    vls=['2016-02-12']
    g1 = mpf.plot(df2016_nifty, type="candle", style = "yahoo", 
                  #alines=two_points, 
                  vlines=dict(vlines=vls,colors='c', linewidths=345,alpha=0.4),
                  hlines=7600)
    #g1 = mpf.plot(df2016_nifty, type="candle", style = "yahoo")
    st.pyplot(g1)

    # Nifty 2017 Analysis
    df2017_nifty = yf.download('^NSEI', interval="1d", start="2017-01-15", end="2017-02-15")
    df2017_nifty['Date'] = pd.to_datetime(df2017_nifty.index)
    df2017_nifty['Date'] = df2017_nifty['Date'].apply(mpl_dates.date2num)

    df2017_nifty = df2017_nifty.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]
    
    #df2017 = nse.get_hist('NIFTY 50', from_date=dt.date(2017,1,15),to_date=dt.date(2017,2,15))
    #two_points = [('2017-02-01', 8537),('2017-02-14', 8537)]
    vls=['2017-02-14']
    g2 = mpf.plot(df2017_nifty, type="candle", style = "yahoo", 
                  #alines=two_points, 
                  vlines=dict(vlines=vls,colors='c', linewidths=330,alpha=0.4),
                  hlines=8537)
    st.pyplot(g2)
    #st.write(df2017_nifty)


    # Nifty 2018 Analysis
    df2018_nifty = yf.download('^NSEI', interval="1d", start="2018-01-15", end="2018-02-15")
    df2018_nifty['Date'] = pd.to_datetime(df2018_nifty.index)
    df2018_nifty['Date'] = df2018_nifty['Date'].apply(mpl_dates.date2num)

    df2018_nifty = df2018_nifty.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]
    
    #st.write(df2018_nifty)
    #df2018 = nse.get_hist('NIFTY 50', from_date=dt.date(2018,1,15),to_date=dt.date(2018,2,15))
    #g3 = mpf.plot(df2018_nifty, type="candle", style = "yahoo")
    vls=['2018-02-07']
    g3 = mpf.plot(df2018_nifty, type="candle", style = "yahoo", 
                  #alines=two_points, 
                  vlines=dict(vlines=vls,colors='c', linewidths=150,alpha=0.4),
                  hlines=11117.34)
    st.pyplot(g3)


    # Nifty 2019 Analysis
    df2019_nifty = yf.download('^NSEI', interval="1d", start="2019-01-15", end="2019-02-15")
    df2019_nifty['Date'] = pd.to_datetime(df2019_nifty.index)
    df2019_nifty['Date'] = df2019_nifty['Date'].apply(mpl_dates.date2num)

    df2019_nifty = df2019_nifty.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]
    
    #df2017 = nse.get_hist('NIFTY 50', from_date=dt.date(2017,1,15),to_date=dt.date(2017,2,15))
    #two_points = [('2017-02-01', 8537),('2017-02-14', 8537)]
    vls=['2019-02-12']
    g4 = mpf.plot(df2019_nifty, type="candle", style = "yahoo", 
                  #alines=two_points, 
                  vlines=dict(vlines=vls,colors='c', linewidths=243,alpha=0.4),
                  hlines=10813.45)
    st.pyplot(g4)



    # Nifty 2020 Analysis
    df2020_nifty = yf.download('^NSEI', interval="1d", start="2020-01-15", end="2020-02-15")
    df2020_nifty['Date'] = pd.to_datetime(df2020_nifty.index)
    df2020_nifty['Date'] = df2020_nifty['Date'].apply(mpl_dates.date2num)

    df2020_nifty = df2020_nifty.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]
    
    #df2017 = nse.get_hist('NIFTY 50', from_date=dt.date(2017,1,15),to_date=dt.date(2017,2,15))
    #two_points = [('2017-02-01', 8537),('2017-02-14', 8537)]
    vls=['2020-02-14']
    g5 = mpf.plot(df2020_nifty, type="candle", style = "yahoo", 
                  #alines=two_points, 
                  vlines=dict(vlines=vls,colors='c', linewidths=300,alpha=0.4),
                  hlines=12017.35)
    st.pyplot(g5)
    #st.write(df2017_nifty)


    # Nifty 2021 Analysis
    df2021_nifty = yf.download('^NSEI', interval="1d", start="2021-01-15", end="2021-02-15")
    df2021_nifty['Date'] = pd.to_datetime(df2021_nifty.index)
    df2021_nifty['Date'] = df2021_nifty['Date'].apply(mpl_dates.date2num)

    df2021_nifty = df2021_nifty.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]
    
    #df2017 = nse.get_hist('NIFTY 50', from_date=dt.date(2017,1,15),to_date=dt.date(2017,2,15))
    #two_points = [('2017-02-01', 8537),('2017-02-14', 8537)]
    vls=['2021-02-12']
    g6 = mpf.plot(df2021_nifty, type="candle", style = "yahoo", 
                  #alines=two_points, 
                  vlines=dict(vlines=vls,colors='c', linewidths=340,alpha=0.4),
                  hlines=13661.75)
    st.pyplot(g6)
    #st.write(df2017_nifty)
    






if selected_option == "Charts":
    date_select = st.date_input('Intraday Chart for:')
    sym = st.selectbox('Select Symbol', ('HDB', 'SBIN.NS'))
    b_intra = st.button("Generate")
    
    if b_intra:
      ed = date_select + timedelta(days=1)
      df = yf.download(tickers=sym, start=date_select, end=ed, interval="1m")
      df = df[['Open', 'High', 'Low', 'Close', 'Volume']]

      fig = volume_profile(df, price_pace=0.1)
      st.plotly_chart(fig)



if selected_option == "Real time OI":
    left, right = st.columns(2)
    sym = left.selectbox(
            'Index',
            ('NIFTY', 'BANKNIFTY', 'FINIFTY'))

    exp_date = right.selectbox(
            'Expiry DATE',
            ('13-Jan-2022', '20-Jan-2022', '27-Jan-2022'))


    refresh_button = st.button("Refresh OI")

    if refresh_button:
      #sym = "NIFTY"
      #exp_date = "13-Jan-2022"

      url = "https://www.nseindia.com/api/option-chain-indices?symbol="+sym
      headers = {"accept-encoding": "gzip, deflate, br",
              "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
              "referer": "https://www.nseindia.com/get-quotes/derivatives?symbol="+sym,
              "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36}"
                }
    
      response = requests.get(url, headers = headers).text
      st.write(response)
      df_oi = oc(sym, exp_date)
      st.write(df_oi)


if selected_option == "Home":
    
    # NIFTY 50 INDIAN
    df_nifty = yf.download('^NSEI', interval="1d", start=previous_Date, end=tday)
    df_nifty['Date'] = pd.to_datetime(df_nifty.index)
    df_nifty['Date'] = df_nifty['Date'].apply(mpl_dates.date2num)

    df_nifty = df_nifty.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]

    qf = cf.QuantFig(df_nifty, title="NIFTY 50 - INDIA", name='NIFTY 50 - INDIA')
    fig22 = qf.iplot(asFigure=True)
    nifty_latest_close = round(df_nifty.iloc[len(df_nifty)-1]['Close'],2)
    nifty_previous_close = round(df_nifty.iloc[len(df_nifty)-2]['Close'],2)

    # German DAX
    df_DAX = yf.download('^GDAXI', interval="1d", start=previous_Date, end=tday)
    df_DAX['Date'] = pd.to_datetime(df_DAX.index)
    df_DAX['Date'] = df_DAX['Date'].apply(mpl_dates.date2num)

    df_DAX = df_DAX.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]

    qf2 = cf.QuantFig(df_DAX, title="DAX - GERMANY", name='DAX - GERMANY')
    fig23 = qf2.iplot(asFigure=True)
    dax_latest_close = round(df_DAX.iloc[len(df_DAX)-1]['Close'],2)
    dax_previous_close = round(df_DAX.iloc[len(df_DAX)-2]['Close'],2)

    # DOW USA
    df_DOW = yf.download('^DJI', interval="1d", start=previous_Date, end=tday)
    df_DOW['Date'] = pd.to_datetime(df_DOW.index)
    df_DOW['Date'] = df_DOW['Date'].apply(mpl_dates.date2num)

    df_DOW = df_DOW.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]

    qf3 = cf.QuantFig(df_DOW, title="DOW 30 - USA", name='DOW 30 - USA')
    fig24 = qf3.iplot(asFigure=True)
    dow_latest_close = round(df_DOW.iloc[len(df_DOW)-1]['Close'],2)
    dow_previous_close = round(df_DOW.iloc[len(df_DOW)-2]['Close'],2)


    lc.metric(label="NIFTY 50", value=nifty_latest_close, delta=round((nifty_latest_close - nifty_previous_close),2))
    mc.metric(label="DAX", value=dax_latest_close, delta=round((dax_latest_close - dax_previous_close),2))
    rc.metric(label="DOW 30", value=dow_latest_close, delta=round((dow_latest_close - dow_previous_close),2))
    st.plotly_chart(fig22)
    st.plotly_chart(fig23)
    st.plotly_chart(fig24)

  #################################################################
  #st.markdown("""
  
#""", unsafe_allow_html=True)

  ###################################################################

if selected_option == "Open Interest":
    st.write(tday)
    df = fnodata(tday)
    option = lc.selectbox(
            'Symbol',
            df['SYMBOL'].unique())

    option_exp = mc.selectbox(
            'Expiry DATE',
            df['EXPIRY_DT'].unique())

    option_inst = rc.selectbox(
            'INSTRUMENT',
            df['INSTRUMENT'].unique()) 

    #Getting CMP
    gcmp = get_cmp(df, option)

    # Graph data as per user choice    
    filterdata = filtered_data(df, option, option_exp, option_inst, gcmp)

        
        #md_results = f"**{option}** Futures LTP **{gcmp}**"
        #st.markdown(md_results)
        #lc.markdown(f"<h4 style='text-align: center; color: white; background-color:SlateBlue'>{md_results}</h4>", unsafe_allow_html=True)
        #st.write("Current Future Price" + gcmp)

    
    bb1 = lc.button("Generate OI Graphs")

    if bb1:
        
        
        oi_chart = oi_chart_graph(filterdata)

        coi_chart = coi_chart_graph(filterdata)

        pcr = pcr_cal(df, option, option_exp, option_inst)

        # Plotting OI Graph
        
        st.plotly_chart(oi_chart)

        # Plotting OI Change Graph
        
        st.plotly_chart(coi_chart)
        md_results = f"**PCR for {option} **{round(pcr, 2)}"
        st.markdown(md_results)
        #st.markdown(f"<h4 style='text-align: center; color: white; background-color:SlateBlue'>{pcr}</h4>", unsafe_allow_html=True)
        #st.write(pcr)


if selected_option == "FII/DII Data":
    
    df1 = fiidiidata(tday)

    client_type = lc.selectbox('Client',
            df1['Client Type'].unique())

    
    date_fii = rc.selectbox('Contract Date',
            df1['Date'].unique())
    
    bb2 = rc.button("Generate FII Graphs")

    filterclientdata = filterclientdat(df1, client_type) 

    if bb2:
        fii_chart = get_fii_chart(filterclientdata)
        st.plotly_chart(fii_chart)
        st.write(df1.tail())
        #pcr2 = df1['Bullish Index Option'].sum() / df1['Bearish Index Option'].sum()
        #st.write(pcr2)



if selected_option == "Trading Strategy":
        c1, c2, c3, c4 = st.columns(4)

        df = fnodata(tday)
        gcmp_2 = get_cmp(df,"NIFTY")
        price = myround(gcmp_2)    
    
        

        # SYMBOL price
        spot_price = myround(gcmp_2)

        # Long call
        strike_price_long_call = c2.number_input(value = (price + 200),label = "OTM Strike CE - BUY")
        premium_long_call = c2.number_input(label = "Price for CE Long")

        # Short call
        strike_price_short_call = c1.number_input(value = price, label = "ATM Strike CE - SELL")
        premium_short_call = c1.number_input(label="Price for CE Short")

        # Long put
        strike_price_long_put = c4.number_input(value = (price - 200), label = "OTM Strike PE - BUY") 
        premium_long_put = c4.number_input(label = "Price for PE Long")

        # Short put
        strike_price_short_put = c3.number_input(value = price, label = "ATM Strike PE - SELL") 
        premium_short_put = c3.number_input(label = "Price for PE Short")


        # Stock price range at expiration of the call
        sT = np.arange(0.92*spot_price, 1.08*spot_price, 1)    

        bb3 = c1.button("Get Strategy Graph")

        if bb3:
            

            payoff_long_put = put_payoff(sT, strike_price_long_put, premium_long_put)
            payoff_short_put = put_payoff(sT, strike_price_short_put, premium_short_put) * -1.0
            payoff_long_call = call_payoff(sT, strike_price_long_call, premium_long_call)
            payoff_short_call = call_payoff(sT, strike_price_short_call, premium_short_call) * -1.0
            options_chart = payoff_long_call + payoff_long_put + payoff_short_call + payoff_short_put

            md_results_profit = f"**Max Profit **{round(max(options_chart)*50)}"
            st.markdown(md_results_profit)
            md_results_loss = f"**Max loss **{round(min(options_chart)*50)}"
            st.markdown(md_results_loss)            
            #print("Max Profit:", max(options_chart))
            #print("Max Loss:", min(options_chart))

            # Plot
            fig, ax = plt.subplots(figsize=(8, 5))
            ax.spines['bottom'].set_position('zero')
            #ax.plot(sT, payoff_long_call, '--', label='Long 920 Strike Call', color='g')
            #ax.plot(sT, payoff_short_call, '--', label='Short 940 Strike Call ', color='r')
            ax.plot(sT, options_chart, label='Iron Butterly Payoff')
            plt.xlabel('Price')
            plt.ylabel('Profit and loss')
            #plt.axhline(y = 0, color = 'r', linestyle = '-')
            plt.axhline(y = 0, color = 'r', linestyle = 'dashed')
            plt.legend()
            st.pyplot(fig)
            
            #fig.add_hline(y=0)
            st.plotly_chart(fig)

            #fig2 = py.plot_mpl(fig)
            #fig2.add_hline(y=0)
            #st.plotly_chart(fig2)


            #fig2 = ironbutterfly(options_chart, sT)
            #st.plotly_chart(fig2)









