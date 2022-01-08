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

st.set_page_config(page_title = 'TraDatAnalytix',layout='wide', page_icon='💹')

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
    button3_clicked=False
)

tday = st.sidebar.date_input('Date Input')

lc, mc, rc = st.columns(3)

button1 = st.sidebar.button("Open Interest")
button2 = st.sidebar.button("FII/DII Data")
button3 = st.sidebar.button("Trading Strategy")




if button1 or session_state.button1_clicked:
    session_state.button1_clicked = True
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
        session_state.button1_clicked = False
        
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


if button2 or session_state.button2_clicked:
    session_state.button2_clicked = True
    df1 = fiidiidata(tday)

    client_type = lc.selectbox('Client',
            df1['Client Type'].unique())

    
    date_fii = rc.selectbox('Contract Date',
            df1['Date'].unique())
    
    bb2 = rc.button("Generate FII Graphs")

    filterclientdata = filterclientdat(df1, client_type) 

    if bb2:
        session_state.button2_clicked = False
        fii_chart = get_fii_chart(filterclientdata)
        st.plotly_chart(fii_chart)
        st.write(df1.tail())
        #pcr2 = df1['Bullish Index Option'].sum() / df1['Bearish Index Option'].sum()
        #st.write(pcr2)



if button3 or session_state.button3_clicked:
        session_state.button3_clicked = True
        c1, c2, c3, c4 = st.columns(4)

        df = fnodata(tday)
        gcmp_2 = get_cmp(df,"NIFTY")
        price = myround(gcmp_2)    
        session_state.button3_clicked = True
    
        

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
            session_state.button3_clicked = False

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









