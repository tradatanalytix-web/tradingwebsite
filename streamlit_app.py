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

st.set_page_config(page_title = 'TraDatAnalytix',layout='wide', page_icon='💹')



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

    c1, c2, c3, c4 = st.columns(4)

    df = fnodata(tday)
    gcmp_2 = get_cmp(df,"NIFTY")
    price = myround(gcmp_2)    
    session_state.button3_clicked = True
    strike1 = c1.number_input(value = price, label = "ATM Strike CE - SELL")
    pr1 = c1.number_input(label="Price for CE Short")
    strike2 = c2.number_input(value = (price + 200),label = "OTM Strike CE - BUY")
    pr2 = c2.number_input(label = "Price for CE Long")
    strike3 = c3.number_input(value = price, label = "ATM Strike PE - SELL")
    pr3 = c3.number_input(label = "Price for PE Short")
    strike4 = c4.number_input(value = (price - 200), label = "OTM Strike PE - BUY")
    pr4 = c4.number_input(label = "Price for PE Long")
    bb3 = c1.button("Get Strategy Graph")

    if bb3:
            session_state.button3_clicked = False
            options_chart = ironbutterfly(strike1, pr1, strike2, pr2, strike3, pr3, strike4, pr4)
            st.set_option('deprecation.showPyplotGlobalUse', False)    
            st.pyplot(options_chart)







