import imp
from nbformat import write
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
from fetchdata_investingcom import fetch_investingcom
from fnodataupdate import fnodata
#import SessionState
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
from realtime_optionchain import fetch_optionschain
import json
from os import name
from intradaycharts import volume_profile
#from pynse import *
import logging
import mplfinance as mpf
#from alice_blue import *
import dateutil.parser
from streamlit_option_menu import option_menu
#import streamlit_analytics
from auth0_component import login_button
import pyrebase
from PIL import Image
import hydralit_components as hc
from streamlit_echarts import st_echarts
from dispjsbar import oi_premium_bar_js
from gauge_chart import pcr_gauge_graph
from streamlit_autorefresh import st_autorefresh
import investpy
from fetchdata_investingcom import fetch_investingcom
from options_function_cal import OptionStrat
from options_function_cal import Option
from dispjsoptions import optionspayoff_diagram
from maxpaingraph import maxxpain
from filterdatafuture import filtered_data_future
from futureoigraph import futureoigraph_hist
from pcrchart_h import pcrchart_hist
from candlestick_chart import candlestick_chart_display
#from prophetforecastml import prophet_forecast_graph
from supertrend_optimal import suptrend_cal
import datetime
from multistrikeoi import multistrikeoi_graph
from fetchdata_investingcom_hist import fetch_investingcom_hist
import pytz
from sqlalchemy import create_engine
from globaldashboard import globaldashboard_metric
from globaldf import *
from globalcharts_summary import global_graph
from simplelinechart_js import linechart_js
from sectorchart import sector_graph



logo_top = Image.open("./tradatanalytix logo.png")

st.set_page_config(page_title = 'TraDatAnalytix',layout='wide', page_icon=logo_top)


# hide_menu_style = """
#   <style>
#   #MainMenu {visibility: hidden; }
#   footer {visibility: hidden;}
#   </style>
# """

# st.markdown(hide_menu_style, unsafe_allow_html=True)


# # Configuration Key
# firebaseConfig = {
#     'apiKey': "AIzaSyAMSJ5BnRt24irMVQ1OXL2C0_ZXwCKPvDY",
#     'authDomain': "tradatanalytix.firebaseapp.com",
#     'projectId': "tradatanalytix",
#     'databaseURL': "https://tradatanalytix-default-rtdb.asia-southeast1.firebasedatabase.app/",
#     'storageBucket': "tradatanalytix.appspot.com",
#     'messagingSenderId': "218878821093",
#     'appId': "1:218878821093:web:236e1e4012d87539524a0c",
#     'measurementId': "G-T31TH0KN15"
# }


# # Firebase Authentication
# firebase = pyrebase.initialize_app(firebaseConfig)
# auth = firebase.auth()

# # Database
# db = firebase.database()
# storage = firebase.storage()

# title_input = st.empty()
# title_input.title("Welcome to TraDatAnalytix")

# # Authentication
# choicebox = st.empty()
# choice = choicebox.selectbox('login/Signup', ['Login', 'Sign up'])


# text_input_container_email = st.empty()
# text_input_container_pwd = st.empty()

# # Obtain User Input for email and password
# email = text_input_container_email.text_input('Please enter your email address')
# password = text_input_container_pwd.text_input('Please enter your password',type = 'password')


# #image1 = paymentimage.image("C:\\Users\\pitan\\PycharmProjects\\tradingwebsite\\QrCode.jpeg")

# #paymentimage.image(image_open_now)


# # App 

# # Sign up Block
# if choice == 'Sign up':
#     handle = st.text_input(
#         'Please input your app handle name', value='Default')
#     submit = st.button('Create my account')

#     if submit:
#         user = auth.create_user_with_email_and_password(email, password)
#         st.success('Your account is created suceesfully!')
#         st.balloons()
#         # Sign in
#         user = auth.sign_in_with_email_and_password(email, password)
#         db.child(user['localId']).child("Handle").set(handle)
#         db.child(user['localId']).child("ID").set(user['localId'])
#         st.title('Welcome' + handle)
#         st.info('Login via login drop down selection')

# # Login Block
# if choice == 'Login':
#     logincheck = st.empty()
#     #paymentimage = st.empty()
#     login = logincheck.checkbox('Login')
#     #image_open_now = Image.open("./TraDatAnalyttics-01.png")
#     #paymentimage.image(image_open_now, width=500)
#     if login:
#           user = auth.sign_in_with_email_and_password(email,password)
#           text_input_container_email.empty()
#           text_input_container_pwd.empty()
#           title_input.empty()
#           choicebox.empty()
#           logincheck.empty()
          #paymentimage.empty()
          # email.empty()
          # password.empty()



          # # Firebase Config
          # firebaseConfig = {
          #   apiKey: "AIzaSyAMSJ5BnRt24irMVQ1OXL2C0_ZXwCKPvDY",
          #   authDomain: "tradatanalytix.firebaseapp.com",
          #   projectId: "tradatanalytix",
          #   storageBucket: "tradatanalytix.appspot.com",
          #   messagingSenderId: "218878821093",
          #   appId: "1:218878821093:web:236e1e4012d87539524a0c",
          #   measurementId: "G-T31TH0KN15"
          # }


#streamlit_analytics.start_tracking()

#st.set_page_config(page_title = 'TraDatAnalytix',layout='wide', page_icon='💹')



# clientId = "Lfd5DqF9GeqhJWeb2hq0JXedCyLyYzS2"
# domain = "https://dev-ak2hwag7.us.auth0.com"

#user_info = login_button(clientId, domain = domain)



#nse=Nse()


# with open('style.css') as f:
#  st.markdown(f'<style>{f.read()}<style>', unsafe_allow_html=True)

# st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

# st.markdown("""
# <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
#   <a class="navbar-brand" href="https://www.youtube.com/channel/UCw2H-l2iNaRjXapU-mrJZXQ" target="_blank">TraDatAnalytix</a>
#   <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
#     <span class="navbar-toggler-icon"></span>
#   </button>
#   <div class="collapse navbar-collapse" id="navbarNav">
#     <ul class="navbar-nav">
#       <li class="nav-item active">
#         <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
#       </li>
#       <li class="nav-item">
#         <a class="nav-link" href="https://www.youtube.com/channel/UCw2H-l2iNaRjXapU-mrJZXQ" target="_blank">YouTube</a>
#       </li>
#       <li class="nav-item">
#         <a class="nav-link" href="https://twitter.com/PitanjalDatta" target="_blank">Twitter</a>
#       </li>
#     </ul>
#   </div>
# </nav>
# """, unsafe_allow_html=True)



# # specify the primary menu definition
# menu_data = [
#     #{'icon': "far fa-copy", 'label':"Left End"},
#     #{'id':'Copy','icon':"🐙",'label':"Copy"},
#     {'icon': "fa-solid fa-radar",'label':"Social Media", 'submenu':[{'id':' subid11','icon': "fa fa-paperclip", 'label':"Facebook"},{'id':'subid12', 'label':"Twitter"},{'id':'subid13','icon': "fa fa-database", 'label':"Youtube"}]},
#     {'icon': "far fa-chart-bar", 'label':"Chart"},#no tooltip message
#     #{'id':' Crazy return value 💀','icon': "💀", 'label':"Calendar"},
#     {'icon': "fas fa-tachometer-alt", 'label':"Dashboard",'ttip':"I'm the Dashboard tooltip!"}, #can add a tooltip message
#     #{'icon': "far fa-copy", 'label':"Right End"},
#     #{'icon': "fa-solid fa-radar",'label':"Dropdown2", 'submenu':[{'label':"Sub-item 1", 'icon': "fa fa-meh"},{'label':"Sub-item 2"},{'icon':'🙉','label':"Sub-item 3",}]},
# ]

# over_theme = {'txc_inactive': '#FFFFFF'}
# menu_id = hc.nav_bar(
#     menu_definition=menu_data,
#     override_theme=over_theme,
#     home_name='Home',
#     login_name='Logout',
#     hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
#     sticky_nav=True, #at the top or not
#     sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
# )



# session_state = SessionState.get(
#     button1_clicked=False,
#     button2_clicked=False,
#     button3_clicked=False,
#     home_button = False
# )



USERNAME = 'pitanjal_demo_db_connection'
PG_STRING = 'postgresql://pitanjal_demo_db_connection:3GeG3_M27uKWEWjGb57svsdm35vz2@db.bit.io'
# Create SQLAlchemy engine to manage our database connections
engine = create_engine(PG_STRING)




holidays_dates = ["2022-03-18", "2022-01-26"]


current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
timetrack = current_time.hour

if timetrack <= 20:
  tday = date.today() - datetime.timedelta(days=1)
else:
  tday = date.today()

#tday = date.today()


#tday = st.sidebar.date_input('Date Input')
previous_Date = tday - timedelta(days = 180)

lc, mc, rc = st.columns(3)


with st.sidebar:
  selected_option = option_menu(
    "TraDatAnalytix",
    ['Global Markets','Derivatives Data','Open Interest Data', 'FII/DII Data','Pick Outperformers' ,'Trading Strategy'],
    icons = ['globe','body-text','bar-chart-fill', 'gear', 'currency-exchange' ,'option'],
    menu_icon = "cast",
    default_index = 0
  )


#####################################################################

if selected_option == "*BUDGET SPECIAL*":
    #st.title("Post Budget - Trading Strategy")
    # horizontal menu
    selected2 = option_menu("Post Budget Trading Strategy for:", ["Nifty", "Bank Nifty"], 
    icons=['collection', 'bank2'], 
    menu_icon="graph-up-arrow", default_index=0, orientation = "horizontal")
    #selected2

    st.set_option('deprecation.showPyplotGlobalUse', False)
    
    


    if selected2 == "Nifty":


      with hc.HyLoader('Loading',hc.Loaders.standard_loaders,index=[3,0,5]):
        with st.expander("See Trading Strategy -- Details"):
          st.write("""
              1. Check Budget Day Closing, whether Green Candle or Red Candle, at 3:15 pm on Budget Day.
              2. If its a GREEN candle at 3:15 pm of Budget day, mark the LOW of Budget day, and SELL PUT option strike price nearest to the LOW price.
              3. If its a RED candle at 3:15 pm of Budget day, mark the HIGH of Budget day, and SELL CALL option strike price nearest to the HIGH price.
              4. Apart from 2020, this strategy worked every year from 2015 to 2021.
          """)


        # Nifty 2015 Analysis


        st.subheader("Nifty in 2015")
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
        st.subheader("Nifty in 2016")
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
        st.subheader("Nifty in 2017")
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
        st.subheader("Nifty in 2018")
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
        st.subheader("Nifty in 2019")
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
        st.subheader("Nifty in 2020")
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
        st.subheader("Nifty in 2021")
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
    
    
    
    if selected2 == "Bank Nifty":
      with hc.HyLoader('Loading',hc.Loaders.standard_loaders,index=[3,0,5]):
        with st.expander("See Trading Strategy -- Details"):
          st.write("""
              1. Check Budget Day Closing, whether Green Candle or Red Candle, at 3:15 pm on Budget Day.
              2. If its a GREEN candle at 3:15 pm of Budget day, mark the LOW of Budget day, and SELL PUT option strike price nearest to the LOW price.
              3. If its a RED candle at 3:15 pm of Budget day, mark the HIGH of Budget day, and SELL CALL option strike price nearest to the HIGH price.
              4. Apart from 2020, this strategy worked every year from 2015 to 2021.
          """)


        # # Nifty 2015 Analysis


        # st.subheader("Bank Nifty in 2015")
        # df2015_nifty = yf.download('^NSEBANK', interval="1d", start="2015-01-15", end="2015-02-15")
        # df2015_nifty['Date'] = pd.to_datetime(df2015_nifty.index)
        # df2015_nifty['Date'] = df2015_nifty['Date'].apply(mpl_dates.date2num)

        # df2015_nifty = df2015_nifty.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]
        # #df2016 = nse.get_hist('NIFTY 50', from_date=dt.date(2016,1,15),to_date=dt.date(2016,2,15))
        # vls=['2015-02-12']
        # ga1 = mpf.plot(df2015_nifty, type="candle", style = "yahoo", 
        #               #alines=two_points, 
        #               vlines=dict(vlines=vls,colors='c', linewidths=255,alpha=0.4),
        #               hlines=20600)
        # #g1 = mpf.plot(df2016_nifty, type="candle", style = "yahoo")
        # st.pyplot(ga1)

        
        
        
        
        # # Nifty 2016 Analysis
        # st.subheader("Bank Nifty in 2016")
        # df2016_nifty = yf.download('^NSEBANK', interval="1d", start="2016-01-15", end="2016-02-15")
        # df2016_nifty['Date'] = pd.to_datetime(df2016_nifty.index)
        # df2016_nifty['Date'] = df2016_nifty['Date'].apply(mpl_dates.date2num)

        # df2016_nifty = df2016_nifty.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]
        # #df2016 = nse.get_hist('NIFTY 50', from_date=dt.date(2016,1,15),to_date=dt.date(2016,2,15))
        # st.write(df2016_nifty)
        # vls=['2016-02-08']
        # g1 = mpf.plot(df2016_nifty, type="candle", style = "yahoo", 
        #               #alines=two_points, 
        #               vlines=dict(vlines=vls,colors='c', linewidths=345,alpha=0.4),
        #               hlines=15565)
        # #g1 = mpf.plot(df2016_nifty, type="candle", style = "yahoo")
        # st.pyplot(g1)

        # Nifty 2017 Analysis
        st.subheader("Bank Nifty in 2017")
        df2017_nifty = yf.download('^NSEBANK', interval="1d", start="2017-01-15", end="2017-02-15")
        df2017_nifty['Date'] = pd.to_datetime(df2017_nifty.index)
        df2017_nifty['Date'] = df2017_nifty['Date'].apply(mpl_dates.date2num)

        df2017_nifty = df2017_nifty.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]
        
        #df2017 = nse.get_hist('NIFTY 50', from_date=dt.date(2017,1,15),to_date=dt.date(2017,2,15))
        #two_points = [('2017-02-01', 8537),('2017-02-14', 8537)]
        vls=['2017-02-14']
        g2 = mpf.plot(df2017_nifty, type="candle", style = "yahoo", 
                      #alines=two_points, 
                      vlines=dict(vlines=vls,colors='c', linewidths=330,alpha=0.4),
                      hlines=19470)
        st.pyplot(g2)
        #st.write(df2017_nifty)


        # Nifty 2018 Analysis
        st.subheader("Bank Nifty in 2018")
        df2018_nifty = yf.download('^NSEBANK', interval="1d", start="2018-01-15", end="2018-02-15")
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
                      hlines=27613)
        st.pyplot(g3)


        # Nifty 2019 Analysis
        st.subheader("Bank Nifty in 2019")
        df2019_nifty = yf.download('^NSEBANK', interval="1d", start="2019-01-15", end="2019-02-15")
        df2019_nifty['Date'] = pd.to_datetime(df2019_nifty.index)
        df2019_nifty['Date'] = df2019_nifty['Date'].apply(mpl_dates.date2num)

        df2019_nifty = df2019_nifty.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]
        
        #df2017 = nse.get_hist('NIFTY 50', from_date=dt.date(2017,1,15),to_date=dt.date(2017,2,15))
        #two_points = [('2017-02-01', 8537),('2017-02-14', 8537)]
        vls=['2019-02-12']
        g4 = mpf.plot(df2019_nifty, type="candle", style = "yahoo", 
                      #alines=two_points, 
                      vlines=dict(vlines=vls,colors='c', linewidths=243,alpha=0.4),
                      hlines=27533)
        st.pyplot(g4)



        # Nifty 2020 Analysis
        st.subheader("Bank Nifty in 2020")
        df2020_nifty = yf.download('^NSEBANK', interval="1d", start="2020-01-15", end="2020-02-15")
        df2020_nifty['Date'] = pd.to_datetime(df2020_nifty.index)
        df2020_nifty['Date'] = df2020_nifty['Date'].apply(mpl_dates.date2num)

        df2020_nifty = df2020_nifty.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]
        
        #df2017 = nse.get_hist('NIFTY 50', from_date=dt.date(2017,1,15),to_date=dt.date(2017,2,15))
        #two_points = [('2017-02-01', 8537),('2017-02-14', 8537)]
        vls=['2020-02-14']
        g5 = mpf.plot(df2020_nifty, type="candle", style = "yahoo", 
                      #alines=two_points, 
                      vlines=dict(vlines=vls,colors='c', linewidths=300,alpha=0.4),
                      hlines=30918)
        st.pyplot(g5)
        #st.write(df2017_nifty)


        # Nifty 2021 Analysis
        st.subheader("Bank Nifty in 2021")
        df2021_nifty = yf.download('^NSEBANK', interval="1d", start="2021-01-15", end="2021-02-15")
        df2021_nifty['Date'] = pd.to_datetime(df2021_nifty.index)
        df2021_nifty['Date'] = df2021_nifty['Date'].apply(mpl_dates.date2num)

        df2021_nifty = df2021_nifty.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]
        
        #df2017 = nse.get_hist('NIFTY 50', from_date=dt.date(2017,1,15),to_date=dt.date(2017,2,15))
        #two_points = [('2017-02-01', 8537),('2017-02-14', 8537)]
        vls=['2021-02-12']
        g6 = mpf.plot(df2021_nifty, type="candle", style = "yahoo", 
                      #alines=two_points, 
                      vlines=dict(vlines=vls,colors='c', linewidths=340,alpha=0.4),
                      hlines=30906)
        st.pyplot(g6)
        #st.write(df2017_nifty)
      


#########################################################################################################


#if selected_option == "Charts":
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


#########################################################################################################


if selected_option == "Open Interest Data":
    #left, middle, right = st.columns(3)
    symbol = 'NIFTY50'

    exp_date = '07-apr-2022'

    autorefresh_time = 3
    #rainbow = ['15050', '15550', '16050', '16550', '17050', '17550', '18050', '18550']
    
    # value1, value2 = middle.select_slider(
    #                       'Select a range of values', options = rainbow,
    #                       value = ('16550', '17550'))

    value1 = str(16700)
    value2 = str(17700)

    #st.write('Values:', values)

    selected3 = option_menu("", ["Multi Strike OI","Open Interest", "Change in OI"], 
    icons=['collection','collection', 'bank2'], 
    menu_icon="graph-up-arrow", default_index=0, orientation = "horizontal")
    #selected2
    
    dftrynifty = fetch_investingcom('Nifty 50', 'india')
    niftyspot_price = dftrynifty.iloc[len(dftrynifty)-1]['Close']

    t1 = str(int(np.round(niftyspot_price/100,0)*100)) + "CE"
    t2 = str(int(np.round(niftyspot_price/100,0)*100)) + "PE"
    t3 = str(int(np.round(niftyspot_price/100,0)*100) - 100) + "CE"
    t4 = str(int(np.round(niftyspot_price/100,0)*100) + 100) + "PE"
    t5 = str(int(np.round(niftyspot_price/100,0)*100) + 100) + "CE"
    t6 = str(int(np.round(niftyspot_price/100,0)*100) - 100) + "PE"

    if selected3 == "Multi Strike OI":
      st_autorefresh(interval=3 * 60 * 1000, key="dataframerefresh")
      with hc.HyLoader('Fetching Real time Data',hc.Loaders.standard_loaders,index=[3,0,5]):
        
        # 1. Execute a Specific Query
        sql = f'''
            SELECT *
            FROM "pitanjal/tradatanalytix"."nifty-intraday-oi";
        '''
        with engine.connect() as conn:
            df_multi = pd.read_sql(sql, conn)
        
        
        
        #conn = sqlite3.connect("C:\\Users\\pitan\\Algo Trading\\nifty-oi-intraday.db")
        #c = conn.cursor()
        #df_multi = pd.read_sql_query("SELECT * from 'oidata_240322'", conn)
        datelist2 = df_multi["datetime_day"].tolist()
        #datelist2 = [date_obj.strftime('%Y-%m-%d') for date_obj in datelist2]
        atmcelist = df_multi["atmce"].tolist()
        atmpelist = df_multi["atmpe"].tolist()
        itmcelist = df_multi["itmce"].tolist()
        itmpelist = df_multi["itmpe"].tolist()
        otmcelist = df_multi["otmce"].tolist()
        otmpelist = df_multi["otmpe"].tolist()


        multioic_chart_js = multistrikeoi_graph(datelist2, 
                                                atmcelist, 
                                                atmpelist, 
                                                itmcelist, 
                                                itmpelist,
                                                otmcelist,
                                                otmpelist,
                                                t1, t2, t3, t4, t5, t6)

        st_echarts(
                      options=multioic_chart_js, 
                      height="400px",
                    )


        
        #st.write(df_multi)

    

    
    #refresh_button = st.button("Refresh OI")

    #exp_date = '17-feb-2022'
    #symbol = "NIFTY50"
    # update every 3 mins
    if selected3 == "Open Interest":
      st_autorefresh(interval=autorefresh_time * 60 * 1000, key="dataframerefresh")
      with hc.HyLoader('Fetching Real time Data',hc.Loaders.standard_loaders,index=[3,0,5]):
      #if refresh_button:
        #gcmp = get_cmp(df, option)
        dftrynifty = fetch_investingcom('Nifty 50', 'india')
        gcmp = dftrynifty.iloc[len(dftrynifty)-1]['Close']
        
        gcmp = float(round(gcmp/50)*50)
        gcmp1 = format(gcmp,".2f")
        #st.write(gcmp1)
        df_realtimeoi = fetch_optionschain(symbol, exp_date)
        
        #st.write(df_realtimeoi)
        dfnew = df_realtimeoi[["strike_price", "ce_ltp", "ce_OI", "ce_OI_ch", "pe_ltp" ,"pe_OI" ,"pe_OI_ch"]]
        fullpelist_oi = dfnew["pe_OI"].tolist()
        fullcelist_oi = dfnew["ce_OI"].tolist()
        
        
        rslt_df = dfnew.loc[value1:value2]
        #st.write(rslt_df)
        strikelist = rslt_df["strike_price"].tolist()
        pelist_oi = rslt_df["pe_OI"].tolist()
        celist_oi = rslt_df["ce_OI"].tolist()
          
        oic_chart_js = oi_premium_bar_js(strikelist, celist_oi, pelist_oi, gcmp1, titlegraph = "Real time Open Interest")

        st_echarts(
                      options=oic_chart_js, 
                      height="400px",
                    )
        
        test_list_ce = [float(i) for i in fullcelist_oi  if i]
        test_list_pe = [float(i) for i in fullpelist_oi  if i]


        sumce = sum(test_list_ce)
        sumpe = sum(test_list_pe)          

        pcr = sumpe / sumce
        pcrgraph = pcr_gauge_graph(pcr/2*100)

        # Plotting OI Graph
        
        #st.plotly_chart(oi_chart)

        # Plotting OI Change Graph
        
        #st.plotly_chart(coi_chart)
        md_results = f"**PCR for {symbol} **{round(pcr, 2)}"
        st.markdown(md_results)

        st_echarts(
                      options=pcrgraph, 
                      height="400px",
                  )              


    if selected3 == "Change in OI":
      st_autorefresh(interval=autorefresh_time * 60 * 1000, key="dataframerefresh")
      with hc.HyLoader('Fetching Real time Data',hc.Loaders.standard_loaders,index=[3,0,5]):
      #if refresh_button:
        dftrynifty = fetch_investingcom('Nifty 50', 'india')
        gcmp = dftrynifty.iloc[len(dftrynifty)-1]['Close']
        
        gcmp = float(round(gcmp/50)*50)
        gcmp1 = format(gcmp,".2f")
    
        df_realtimeoi = fetch_optionschain(symbol, exp_date)
        #st.write(df_realtimeoi)
        dfnew = df_realtimeoi[["strike_price", "ce_ltp", "ce_OI", "ce_OI_ch", "pe_ltp" ,"pe_OI" ,"pe_OI_ch"]]
        fullpelist_oi = dfnew["pe_OI_ch"].tolist()
        fullcelist_oi = dfnew["ce_OI_ch"].tolist()
        rslt_df = dfnew.loc[value1:value2]
        #st.write(rslt_df)
        strikelist = rslt_df["strike_price"].tolist()
        pelist_oi = rslt_df["pe_OI_ch"].tolist()
        celist_oi = rslt_df["ce_OI_ch"].tolist()
          
        oic_chart_js = oi_premium_bar_js(strikelist, celist_oi, pelist_oi, gcmp1, titlegraph = "Change in Open Interest")

        st_echarts(
                      options=oic_chart_js, 
                      height="400px",
                    )
        
        test_list_ce = [float(i) for i in fullcelist_oi if i]
        test_list_pe = [float(i) for i in fullpelist_oi if i]

        sumce = sum(test_list_ce)
        sumpe = sum(test_list_pe)            

        pcr = sumpe / sumce
        pcrgraph = pcr_gauge_graph(pcr/2*100)

        # Plotting OI Graph
        
        #st.plotly_chart(oi_chart)

        # Plotting OI Change Graph
        
        #st.plotly_chart(coi_chart)
        md_results = f"**Intraday PCR for {symbol} **{round(pcr, 2)}"
        st.markdown(md_results)

        st_echarts(
                      options=pcrgraph, 
                      height="400px",
                  )              


        #df_oi = oc(sym, exp_date)
      #st.write(df_oi)


######################################################################################################

if selected_option == "Global Markets":

    # horizontal menu
    selected_globalmarkets = option_menu("", ["Dashboard", "Charts"], 
    icons=['collection', 'bank2'], 
    menu_icon="graph-up-arrow", default_index=0, orientation = "horizontal")



    # Get CMPS

    if selected_globalmarkets == "Dashboard":
      
      lc, mc, rc = st.columns(3)

      #NIFTY 50
      dftrynifty = fetch_investingcom('Nifty 50', 'india')
      niftycmp = dftrynifty.iloc[len(dftrynifty)-1]['Close']
      niftychangepc = (dftrynifty.iloc[len(dftrynifty)-1]['Close'] - dftrynifty.iloc[len(dftrynifty)-2]['Close'])/dftrynifty.iloc[len(dftrynifty)-2]['Close']
      niftychangepc = "{:.2%}".format(niftychangepc)

      # DOW 30
      dftrynifty = fetch_investingcom('Dow 30', 'united states')
      dowcmp = dftrynifty.iloc[len(dftrynifty)-1]['Close']
      dowchangepc = (dftrynifty.iloc[len(dftrynifty)-1]['Close'] - dftrynifty.iloc[len(dftrynifty)-2]['Close'])/dftrynifty.iloc[len(dftrynifty)-2]['Close']
      dowchangepc = "{:.2%}".format(dowchangepc)


      # DAX
      dftrynifty = fetch_investingcom('DAX', 'germany')
      daxcmp = dftrynifty.iloc[len(dftrynifty)-1]['Close']
      daxchangepc = (dftrynifty.iloc[len(dftrynifty)-1]['Close'] - dftrynifty.iloc[len(dftrynifty)-2]['Close'])/dftrynifty.iloc[len(dftrynifty)-2]['Close']
      daxchangepc = "{:.2%}".format(daxchangepc)


      # CAC
      dftrynifty = fetch_investingcom('CAC 40', 'france')
      caccmp = dftrynifty.iloc[len(dftrynifty)-1]['Close']
      cacchangepc = (dftrynifty.iloc[len(dftrynifty)-1]['Close'] - dftrynifty.iloc[len(dftrynifty)-2]['Close'])/dftrynifty.iloc[len(dftrynifty)-2]['Close']
      cacchangepc = "{:.2%}".format(cacchangepc)


      # Nikkei 225
      dftrynifty = fetch_investingcom('Nikkei 225', 'Japan')
      nikcmp = dftrynifty.iloc[len(dftrynifty)-1]['Close']
      nikchangepc = (dftrynifty.iloc[len(dftrynifty)-1]['Close'] - dftrynifty.iloc[len(dftrynifty)-2]['Close'])/dftrynifty.iloc[len(dftrynifty)-2]['Close']
      nikchangepc = "{:.2%}".format(nikchangepc)

      # Hang Sang
      dftrynifty = fetch_investingcom('Hang Seng', 'Hong Kong')
      hancmp = dftrynifty.iloc[len(dftrynifty)-1]['Close']
      hanchangepc = (dftrynifty.iloc[len(dftrynifty)-1]['Close'] - dftrynifty.iloc[len(dftrynifty)-2]['Close'])/dftrynifty.iloc[len(dftrynifty)-2]['Close']
      hanchangepc = "{:.2%}".format(hanchangepc)



      # FTSE

      ftse_index = globaldashboard_metric('FTSE 100', 'united kingdom')
      #strait_index = globaldashboard_metric('STI', 'singapore')
      kospi_index = globaldashboard_metric('KOSPI', 'south korea')
      nasdaq_index = globaldashboard_metric('NASDAQ', 'united states')





      # Metrics
      lc.metric(label="Nifty 50 - India", value=niftycmp, delta=niftychangepc)
      mc.metric(label="DAX - Germany", value=daxcmp, delta=daxchangepc)
      rc.metric(label="DOW 30 - USA", value=dowcmp, delta=dowchangepc)
      lc.metric(label="CAC 40 - France", value=caccmp, delta=cacchangepc)
      mc.metric(label="Nikkei 225 - Japan", value=nikcmp, delta=nikchangepc)
      rc.metric(label="Hang Sang - Hong Kong", value=hancmp, delta=hanchangepc)
      lc.metric(label="FTSE - UK", value=ftse_index[0], delta=ftse_index[1])
      mc.metric(label="NASDAQ - US", value=nasdaq_index[0], delta=nasdaq_index[1])
      rc.metric(label="KOSPI - South Korea", value=kospi_index[0], delta=kospi_index[1])


      
    
    if selected_globalmarkets == "Charts":

        # Summary Chart -- Global

        indialist = globallist_get("Nifty 50",'india')
        uklist = globallist_get("FTSE 100",'united kingdom')
        uslist = globallist_get("NASDAQ",'united states')
        japanlist = globallist_get("Nikkei 225",'Japan')
        hongkonglist = globallist_get("Hang Seng",'Hong Kong')
        francelist = globallist_get("CAC 40",'france')
        #sglist = globallist_get("STI",'singapore')
        southkorlist = globallist_get("KOSPI",'south korea')
        germanylist = globallist_get("DAX",'germany')
        datelist = datelistget("DAX",'germany')





        # linechartplot = linechart_js(datelist, indialist)


        # st_echarts(
        #     options = linechartplot, height=400,
        # )


        #st.write((indialist))
        # st.write((uslist))
        # st.write((gerlist))
        # st.write((frlist))
        # st.write((korlist))
        # st.write((hklist))
        # st.write((jplist))
        # st.write((uklist))
        #st.write((datelist))

        plot_global = global_graph(datelist, indialist, uklist, uslist, southkorlist, japanlist, hongkonglist, francelist, germanylist)


        st_echarts(
            options = plot_global, height=400,
        )





        with st.form("Candle_Index"):
          st.write("View Global Indices Candle Chart")
          df = pd.read_csv("./globalindices_sym.csv")
          #df.head()
          #st.write(df)
          select_option = st.selectbox(
                                'Choose Global Index',
                                ('Nifty 50', 'Dow 30', 'FTSE 100' , 'CAC 40', 'DAX' ,'Nikkei 225', 'Hang Seng'))
          submitted = st.form_submit_button("See Chart")

          if submitted:
            df = df.loc[(df['symbol'] == select_option)]
            country = df.iloc[0]['country']
            sym_yahoo = df.iloc[0]['yahoofin']

            dftrynifty = fetch_investingcom(select_option, country)
            #st.write(country)
            #st.write(sym_yahoo)
            #st.write(dftrynifty)
            dateobj22 = list(dftrynifty.index.values)
            #st.write(datelist)
            
            datelist = [str(x) for x in dateobj22]

            dfohlc = dftrynifty[["Close", "Open", "Low", "High"]]
            #st.write(dfohlc)
            ohlclist = dfohlc.to_numpy().tolist()
            #st.write(ohlclist)
            printcandlechart = candlestick_chart_display(datelist, ohlclist)

            st_echarts(
                          options=printcandlechart, height = "400px"
                      )

            # prof_forecast =  prophet_forecast_graph(sym_yahoo)
        # st.pyplot(prof_forecast)          


          

  ###################################################################

if selected_option == "Derivatives Data":
    
    if tday.weekday() == 5:
      tday = tday - timedelta(days=1)
    elif tday.weekday() == 6:
      tday = tday - timedelta(days=2)
    elif tday.strftime("%Y-%m-%d") in holidays_dates:
      tday = tday - timedelta(days=1)
      if tday.weekday() == 0:
        tday = tday - timedelta(days=3)  
    
    df = fnodata(tday)



    selected4 = option_menu("", ["Option OI", "Future OI", "PCR", "Max Pain"], 
    icons=['collection', 'activity', 'speedometer', 'chevron-bar-contract'], 
    menu_icon="graph-up-arrow", default_index=1, orientation = "horizontal")



    if selected4 == "Option OI":
      #df = fnodata(tday)
      st.write(tday)
      left, right = st.columns(2)
      option = left.selectbox(
              'Symbol',
              df['SYMBOL'].unique())

      option_exp = right.selectbox(
              'Expiry DATE',
              df['EXPIRY_DT'].unique())

      option_inst = "OPTIDX"

      #Getting CMP
      gcmp = get_cmp(df, option)

      # Graph data as per user choice    
      filterdata = filtered_data(df, option, option_exp, option_inst, gcmp)

          
          #md_results = f"**{option}** Futures LTP **{gcmp}**"
          #st.markdown(md_results)
          #lc.markdown(f"<h4 style='text-align: center; color: white; background-color:SlateBlue'>{md_results}</h4>", unsafe_allow_html=True)
          #st.write("Current Future Price" + gcmp)

      
      bb1 = st.button("Generate OI Graphs")

      if bb1:
          gcmp = round(gcmp/50)*50
          #st.write(gcmp)
          dfce = filterdata[filterdata['OPTION_TYP']=="CE"]
          dfpe = filterdata[filterdata['OPTION_TYP']=="PE"]
          #st.write(dfce)
          #st.write(dfpe)
          strikelist = dfpe['STRIKE_PR'].tolist()
          pelist_oi = dfpe['OPEN_INT'].tolist()
          celist_oi = dfce["OPEN_INT"].tolist()
          
          oic_chart_js = oi_premium_bar_js(strikelist, celist_oi, pelist_oi, gcmp, titlegraph = "Open Interest")

          st_echarts(
                        options=oic_chart_js, height="400px",
                    )


          pelist_coi = dfpe['CHG_IN_OI'].tolist()
          celist_coi = dfce["CHG_IN_OI"].tolist()
          oicoi_chart_js = oi_premium_bar_js(strikelist, celist_coi, pelist_coi, gcmp, titlegraph = "Change in OI")

          st_echarts(
                        options=oicoi_chart_js, height="400px",
                    )
                    
          #oi_chart = oi_chart_graph(filterdata)

          #coi_chart = coi_chart_graph(filterdata)

          pcr = pcr_cal(df, option, option_exp, option_inst)
          pcrgraph = pcr_gauge_graph(pcr/2*100)

          # Plotting OI Graph
          
          #st.plotly_chart(oi_chart)

          # Plotting OI Change Graph
          
          #st.plotly_chart(coi_chart)
          md_results = f"**PCR for {option} **{round(pcr, 2)}"
          st.markdown(md_results)

          st_echarts(
                        options=pcrgraph, height="400px",
                    )
          
          #st.markdown(f"<h4 style='text-align: center; color: white; background-color:SlateBlue'>{pcr}</h4>", unsafe_allow_html=True)
        #st.write(pcr)

    if selected4 == "Max Pain":
        max_pain_graph = maxxpain (strikelist, celist_oi, pelist_oi)


        st_echarts(
                      options=max_pain_graph, height="400px",
                  )

    if selected4 == "Future OI": 
        
                      
        data1 = fnodata(tday)
        option = st.selectbox(
              'Symbol',
              df['SYMBOL'].unique())

        st.write(tday)      

        left, right = st.columns(2)
        #dftrynifty = fetch_investingcom('Nifty 50', 'india')
        #niftycmp = dftrynifty.iloc[len(dftrynifty)-1]['Close']        

        filterdata = filtered_data_future(data1, option, "FUTIDX")

        # Hang Sang
        
        futoi_current = filterdata.iloc[len(filterdata)-3]['CHG_IN_OI']
        fut_oi_current_pc_1 = (filterdata.iloc[len(filterdata)-3]['CHG_IN_OI']) / (filterdata.iloc[len(filterdata)-3]['OPEN_INT'])
        fut_oi_current_pc = "{:.2%}".format(fut_oi_current_pc_1)


        futoi_next = filterdata.iloc[len(filterdata)-2]['CHG_IN_OI']
        fut_oi_next_pc_1 = (filterdata.iloc[len(filterdata)-2]['CHG_IN_OI']) / (filterdata.iloc[len(filterdata)-3]['OPEN_INT'])
        fut_oi_next_pc = "{:.2%}".format(fut_oi_next_pc_1)



        # Metrics
        left.metric(label="Futures (Current Month) OI Change", value=futoi_current, delta=fut_oi_current_pc)
        right.metric(label="Futures (Next Month) OI Change", value=futoi_next, delta=fut_oi_next_pc)

        if (fut_oi_current_pc_1 > 0.1):
          st.markdown(f'<h1 style="color:#04ba65;font-size:24px;">{"Market is Bullish"}</h1>', unsafe_allow_html=True)
        elif (fut_oi_current_pc_1 < -0.1):
          st.markdown(f'<h1 style="color:#ba0419;font-size:24px;">{"Market is Bearish"}</h1>', unsafe_allow_html=True)
        else:
          st.markdown(f'<h1 style="color:#d1c300;font-size:24px;">{"Market is Sideways"}</h1>', unsafe_allow_html=True)


        # start_date = date(2022, 2, 10)
        # end_date = date(2022, 2, 18)

        #holidays_dates = ["2022-03-18", "2022-01-26"]

        start_date = tday - timedelta(days=10)
        end_date = tday
        delta = timedelta(days=1)
        rowsdata = []

        while start_date <= end_date:
            if (start_date.weekday() >= 0 and start_date.weekday() <= 4) and (start_date.strftime("%Y-%m-%d") not in holidays_dates):
              data2 = fnodata(start_date)
              filterdata = filtered_data_future(data2, option, "FUTIDX")
              futoi_current = filterdata.iloc[len(filterdata)-3]['CHG_IN_OI']
              fut_oi_current_pc_1 = (filterdata.iloc[len(filterdata)-3]['CHG_IN_OI']) / (filterdata.iloc[len(filterdata)-3]['OPEN_INT'])*100
              futoi_next = filterdata.iloc[len(filterdata)-2]['CHG_IN_OI']
              fut_oi_next_pc_1 = (filterdata.iloc[len(filterdata)-2]['CHG_IN_OI']) / (filterdata.iloc[len(filterdata)-3]['OPEN_INT'])*100
              rowsdata.append([start_date, fut_oi_current_pc_1, fut_oi_next_pc_1])
            start_date += delta    
              #print(start_date)

        
        df = pd.DataFrame(rowsdata, columns=["Date", "Change in Current Month Future OI (%)", "Change in Next Month Future OI (%)"])
        # plot1 = df.plot()
        # fig = px.line(        
        #               df, #Data Frame
        #               x = "Date", #Columns from the data frame
        #               y = "Change in Current Month Future OI (%)",
        #               title = "Percentage Change in Future OI"
        #           )
        # fig.update_traces(line_color = "maroon")
        # st.plotly_chart(fig) 


        datelist1 = df["Date"].tolist()
        datelist = [date_obj.strftime('%Y%m%d') for date_obj in datelist1]
        currlist = df["Change in Current Month Future OI (%)"].tolist()
        nextlist = df["Change in Next Month Future OI (%)"].tolist()
          
        futurechart_js = futureoigraph_hist(datelist, currlist, nextlist)

        st_echarts(
                      options=futurechart_js, height="400px",
                  )
        
        #st.write(df) 
        
        #st.write(filterdata)




    if selected4 == "PCR":            
          data2 = fnodata(tday)
          left, right = st.columns(2)
          option = left.selectbox(
                  'Symbol',
                  df['SYMBOL'].unique())

          option_exp = right.selectbox(
                  'Expiry DATE',
                  df['EXPIRY_DT'].unique())

          option_inst = "OPTIDX"

          #Getting CMP
          gcmp = get_cmp(df, option)

          # Graph data as per user choice    
          filterdata = filtered_data(df, option, option_exp, option_inst, gcmp)     

          #left, right = st.columns(2)
          #dftrynifty = fetch_investingcom('Nifty 50', 'india')
          #niftycmp = dftrynifty.iloc[len(dftrynifty)-1]['Close'] 
          
          start_date = tday - timedelta(days=10)
          end_date = tday
          delta = timedelta(days=1)
          rowsdata = []

          while start_date <= end_date:
              if start_date.weekday() >= 0 and start_date.weekday() <= 4 and (start_date.strftime("%Y-%m-%d") not in holidays_dates):
                df = fnodata(start_date)
                gcmp = get_cmp(df, option)
                filterdata = filtered_data(df, option, option_exp, option_inst, gcmp)
                pcr = pcr_cal(df, option, option_exp, option_inst)
                rowsdata.append([start_date, pcr])    
                #print(start_date)
              start_date += delta
          
          df = pd.DataFrame(rowsdata, columns=["Date", "PCR"])
          #st.write(df)
          # plot1 = df.plot()
          # fig = px.line(        
          #               df, #Data Frame
          #               x = "Date", #Columns from the data frame
          #               y = "Change in Current Month Future OI (%)",
          #               title = "Percentage Change in Future OI"
          #           )
          # fig.update_traces(line_color = "maroon")
          # st.plotly_chart(fig) 


          datelist1 = df["Date"].tolist()
          datelist = [date_obj.strftime('%Y%m%d') for date_obj in datelist1]
          pcrlist = df["PCR"].tolist()
          # nextlist = df["Change in Next Month Future OI (%)"].tolist()

          pcrchartjs = pcrchart_hist(datelist, pcrlist)
            
          # futurechart_js = futureoigraph_hist(datelist, currlist, nextlist)

          st_echarts(
                        options=pcrchartjs, height="400px",
                    )
          
          if (df.iloc[len(df)-1]['PCR'] > df.iloc[len(df)-2]['PCR']):
            st.markdown(f'<h1 style="color:#04ba65;font-size:24px;">{"Market is Bullish"}</h1>', unsafe_allow_html=True)
          elif (df.iloc[len(df)-1]['PCR'] < df.iloc[len(df)-2]['PCR']):
            st.markdown(f'<h1 style="color:#ba0419;font-size:24px;">{"Market is Bearish"}</h1>', unsafe_allow_html=True)
          else:
            st.markdown(f'<h1 style="color:#d1c300;font-size:24px;">{"Market is Sideways"}</h1>', unsafe_allow_html=True)

          
      


#####################################################################################################3


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

#########################################################################################################

if selected_option == "Pick Outperformers":

    selected6 = option_menu("", ["Relative Strength", "RS Comparison"], orientation="horizontal")


    if selected6 == "Relative Strength":



      df_nifty = yf.download('^NSEI', interval="1d", start=previous_Date, end=tday)
      df_nifty['Date'] = pd.to_datetime(df_nifty.index)
      df_nifty['Date'] = df_nifty['Date'].apply(mpl_dates.date2num)

      df_nifty = df_nifty.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]


      df_banknifty = yf.download('^NSEBANK', interval="1d", start=previous_Date, end=tday)
      df_banknifty['Date'] = pd.to_datetime(df_banknifty.index)
      df_banknifty['Date'] = df_banknifty['Date'].apply(mpl_dates.date2num)

      df_banknifty = df_banknifty.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]

      rsdata_bank = pd.merge(df_nifty, df_banknifty, left_index=True, right_index=True)

      rsdata_bank['Relative Strength'] = rsdata_bank["Close_y"]/rsdata_bank["Close_x"]

      rs_df = pd.DataFrame()
      rs_df["Date"] = df_nifty['Date']
      rs_df["bank"] = rsdata_bank['Relative Strength'].pct_change()
      df_bank = rsdata_bank[['Date_x', 'Relative Strength']]
      fig_bank = px.line(df_bank, y='Relative Strength', title='Relative Strength - Bank Nifty')
      st.plotly_chart(fig_bank)


      rsbank_list = df_bank["Relative Strength"].tolist()
      datebank_list = df_bank["Date_x"].tolist()

      # option = {
      #               "xAxis": {
      #                   "type": "category",
      #                   "data": datebank_list,
      #               },
      #               "yAxis": {"type": "value"},
      #               "series": [{"data": rsbank_list, "type": "line"}],
      #           }

      # option = oi_premium_bar_js()

      # st_echarts(
      #                 options=option, height="400px",
      #             )

      

      
      df_niftyit = yf.download('^CNXIT', interval="1d", start=previous_Date, end=tday)
      df_niftyit['Date'] = pd.to_datetime(df_niftyit.index)
      df_niftyit['Date'] = df_niftyit['Date'].apply(mpl_dates.date2num)

      df_niftyit = df_niftyit.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]

      rsdata_it = pd.merge(df_nifty, df_niftyit, left_index=True, right_index=True)

      rsdata_it['Relative Strength'] = rsdata_it["Close_y"]/rsdata_it["Close_x"]


      rs_df["IT"] = rsdata_it['Relative Strength'].pct_change()

      df_it = rsdata_it[['Date_x', 'Relative Strength']]
      fig_it = px.line(df_it, y='Relative Strength', title='Relative Strength - IT')
      st.plotly_chart(fig_it)

      stringdate1 = str(tday)
      stringdate2 = str(previous_Date)

      lastconnection = datetime.datetime.strptime(stringdate1, "%Y-%m-%d").strftime("%d/%m/%Y")
      firstconnection = datetime.datetime.strptime(stringdate2, "%Y-%m-%d").strftime("%d/%m/%Y")

      #df_niftyit = yf.download('^CNXAUTO', interval="1d", start=previous_Date, end=tday)
      dfnifty_commodities = fetch_investingcom_hist(sym = "Nifty Pharma", country = "India", startdate = str(firstconnection), enddate = str(lastconnection))
      dfnifty_commodities['Date'] = pd.to_datetime(dfnifty_commodities.index)
      dfnifty_commodities['Date'] = dfnifty_commodities['Date'].apply(mpl_dates.date2num)

      dfnifty_commodities = dfnifty_commodities.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]

      rsdata_commodities = pd.merge(df_nifty, dfnifty_commodities, left_index=True, right_index=True)

      rsdata_commodities['Relative Strength'] = rsdata_commodities["Close_y"]/rsdata_commodities["Close_x"]
      rs_df["Pharma"] = rsdata_commodities['Relative Strength'].pct_change()
      df_commodities = rsdata_commodities[['Date_x', 'Relative Strength']]
      fig_commodities = px.line(df_commodities, y='Relative Strength', title='Relative Strength - Pharma')
      st.plotly_chart(fig_commodities)


      
      #df_niftyit = yf.download('^CNXAUTO', interval="1d", start=previous_Date, end=tday)
      dfnifty_commodities = fetch_investingcom_hist(sym = "Nifty Auto", country = "India", startdate = str(firstconnection), enddate = str(lastconnection))
      dfnifty_commodities['Date'] = pd.to_datetime(dfnifty_commodities.index)
      dfnifty_commodities['Date'] = dfnifty_commodities['Date'].apply(mpl_dates.date2num)

      dfnifty_commodities = dfnifty_commodities.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]

      rsdata_commodities = pd.merge(df_nifty, dfnifty_commodities, left_index=True, right_index=True)

      rsdata_commodities['Relative Strength'] = rsdata_commodities["Close_y"]/rsdata_commodities["Close_x"]
      df_commodities = rsdata_commodities[['Date_x', 'Relative Strength']]
      rs_df["Auto"] = rsdata_commodities['Relative Strength'].pct_change()
      fig_commodities = px.line(df_commodities, y='Relative Strength', title='Relative Strength - Auto')
      st.plotly_chart(fig_commodities)


      
      #df_niftyit = yf.download('^CNXAUTO', interval="1d", start=previous_Date, end=tday)
      dfnifty_commodities = fetch_investingcom_hist(sym = "Nifty Metal", country = "India", startdate = str(firstconnection), enddate = str(lastconnection))
      dfnifty_commodities['Date'] = pd.to_datetime(dfnifty_commodities.index)
      dfnifty_commodities['Date'] = dfnifty_commodities['Date'].apply(mpl_dates.date2num)

      dfnifty_commodities = dfnifty_commodities.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]

      rsdata_commodities = pd.merge(df_nifty, dfnifty_commodities, left_index=True, right_index=True)

      rsdata_commodities['Relative Strength'] = rsdata_commodities["Close_y"]/rsdata_commodities["Close_x"]
      rs_df["Metal"] = rsdata_commodities['Relative Strength'].pct_change()
      df_commodities = rsdata_commodities[['Date_x', 'Relative Strength']]
      fig_commodities = px.line(df_commodities, y='Relative Strength', title='Relative Strength - Metals')
      st.plotly_chart(fig_commodities)


      
      #df_niftyit = yf.download('^CNXAUTO', interval="1d", start=previous_Date, end=tday)
      dfnifty_commodities = fetch_investingcom_hist(sym = "Nifty Media", country = "India", startdate = str(firstconnection), enddate = str(lastconnection))
      dfnifty_commodities['Date'] = pd.to_datetime(dfnifty_commodities.index)
      dfnifty_commodities['Date'] = dfnifty_commodities['Date'].apply(mpl_dates.date2num)

      dfnifty_commodities = dfnifty_commodities.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]

      rsdata_commodities = pd.merge(df_nifty, dfnifty_commodities, left_index=True, right_index=True)

      rsdata_commodities['Relative Strength'] = rsdata_commodities["Close_y"]/rsdata_commodities["Close_x"]
      rs_df["Media"] = rsdata_commodities['Relative Strength'].pct_change()
      df_commodities = rsdata_commodities[['Date_x', 'Relative Strength']]
      fig_commodities = px.line(df_commodities, y='Relative Strength', title='Relative Strength - Media')
      st.plotly_chart(fig_commodities)


          
      #df_niftyit = yf.download('^CNXAUTO', interval="1d", start=previous_Date, end=tday)
      dfnifty_commodities = fetch_investingcom_hist(sym = "Nifty Realty", country = "India", startdate = str(firstconnection), enddate = str(lastconnection))
      dfnifty_commodities['Date'] = pd.to_datetime(dfnifty_commodities.index)
      dfnifty_commodities['Date'] = dfnifty_commodities['Date'].apply(mpl_dates.date2num)

      dfnifty_commodities = dfnifty_commodities.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]

      rsdata_commodities = pd.merge(df_nifty, dfnifty_commodities, left_index=True, right_index=True)

      rsdata_commodities['Relative Strength'] = rsdata_commodities["Close_y"]/rsdata_commodities["Close_x"]
      rs_df["Realty"] = rsdata_commodities['Relative Strength'].pct_change()
      df_commodities = rsdata_commodities[['Date_x', 'Relative Strength']]
      fig_commodities = px.line(df_commodities, y='Relative Strength', title='Relative Strength - Realty')
      st.plotly_chart(fig_commodities)


          
      #df_niftyit = yf.download('^CNXAUTO', interval="1d", start=previous_Date, end=tday)
      dfnifty_commodities = fetch_investingcom_hist(sym = "Nifty India Consumption", country = "India", startdate = str(firstconnection), enddate = str(lastconnection))
      dfnifty_commodities['Date'] = pd.to_datetime(dfnifty_commodities.index)
      dfnifty_commodities['Date'] = dfnifty_commodities['Date'].apply(mpl_dates.date2num)

      dfnifty_commodities = dfnifty_commodities.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]

      rsdata_commodities = pd.merge(df_nifty, dfnifty_commodities, left_index=True, right_index=True)

      rsdata_commodities['Relative Strength'] = rsdata_commodities["Close_y"]/rsdata_commodities["Close_x"]
      rs_df["Consumption"] = rsdata_commodities['Relative Strength'].pct_change()
      df_commodities = rsdata_commodities[['Date_x', 'Relative Strength']]
      fig_commodities = px.line(df_commodities, y='Relative Strength', title='Relative Strength - FMCG')
      st.plotly_chart(fig_commodities)


      
      #df_niftyit = yf.download('^CNXAUTO', interval="1d", start=previous_Date, end=tday)
      dfnifty_commodities = fetch_investingcom_hist(sym = "Nifty Infrastructure", country = "India", startdate = str(firstconnection), enddate = str(lastconnection))
      dfnifty_commodities['Date'] = pd.to_datetime(dfnifty_commodities.index)
      dfnifty_commodities['Date'] = dfnifty_commodities['Date'].apply(mpl_dates.date2num)

      dfnifty_commodities = dfnifty_commodities.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]

      rsdata_commodities = pd.merge(df_nifty, dfnifty_commodities, left_index=True, right_index=True)

      rsdata_commodities['Relative Strength'] = rsdata_commodities["Close_y"]/rsdata_commodities["Close_x"]
      rs_df["Infrastructure"] = rsdata_commodities['Relative Strength'].pct_change()
      df_commodities = rsdata_commodities[['Date_x', 'Relative Strength']]
      fig_commodities = px.line(df_commodities, y='Relative Strength', title='Relative Strength - Infrastructure')
      st.plotly_chart(fig_commodities)

      rs_df = rs_df.iloc[1: , :]
      #rs_df.dropna()

      datelist = rs_df['Date'].to_list()
      datelist2 = [str(x) for x in datelist]
      #datelist2 = datelist.pop(0)
      banklist = rs_df['bank'].to_list()
      #banklist = banklist.pop(0)
      itlist = rs_df['IT'].to_list()
      #itlist = itlist.pop(0)
      autolist = rs_df['Auto'].to_list()
      #autolist = autolist.pop(0)
      medialist = rs_df['Media'].to_list()
      #medialist = medialist.pop(0)
      realtylist = rs_df['Realty'].to_list()
      #realtylist = realtylist.pop(0)
      consumptionlist = rs_df['Consumption'].to_list()
      #consumptionlist = consumptionlist.pop(0)
      infrastructuallist = rs_df['Infrastructure'].to_list()
      #infrastructuallist = infrastructuallist.pop(0)
      pharmalist = rs_df['Pharma'].to_list()
      #pharmalist = pharmalist.pop(0)


      #st.write(rs_df)





      rssector_graph = sector_graph(datelist2, banklist, itlist, autolist, medialist, realtylist, consumptionlist, infrastructuallist, pharmalist)

      # st_echarts(
      #   rssector_graph, height=400
      # )
    

    if selected6 == 'RS Comparison':
        df_nifty = yf.download('^NSEI', interval="1d", start=previous_Date, end=tday)
        df_nifty['Date'] = pd.to_datetime(df_nifty.index)
        df_nifty['Date'] = df_nifty['Date'].apply(mpl_dates.date2num)

        df_nifty = df_nifty.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]


        df_banknifty = yf.download('^NSEBANK', interval="1d", start=previous_Date, end=tday)
        df_banknifty['Date'] = pd.to_datetime(df_banknifty.index)
        df_banknifty['Date'] = df_banknifty['Date'].apply(mpl_dates.date2num)

        df_banknifty = df_banknifty.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]

        rsdata_bank = pd.merge(df_nifty, df_banknifty, left_index=True, right_index=True)

        rsdata_bank['Relative Strength'] = rsdata_bank["Close_y"]/rsdata_bank["Close_x"]

        rs_df = pd.DataFrame()
        rs_df["Date"] = df_nifty['Date']
        rs_df["bank"] = (rsdata_bank['Relative Strength'].pct_change() + 1).cumprod()
        df_bank = rsdata_bank[['Date_x', 'Relative Strength']]
        fig_bank = px.line(df_bank, y='Relative Strength', title='Relative Strength - Bank Nifty')
        #st.plotly_chart(fig_bank)


        rsbank_list = df_bank["Relative Strength"].tolist()
        datebank_list = df_bank["Date_x"].tolist()

        # option = {
        #               "xAxis": {
        #                   "type": "category",
        #                   "data": datebank_list,
        #               },
        #               "yAxis": {"type": "value"},
        #               "series": [{"data": rsbank_list, "type": "line"}],
        #           }

        # option = oi_premium_bar_js()

        # st_echarts(
        #                 options=option, height="400px",
        #             )

        

        
        df_niftyit = yf.download('^CNXIT', interval="1d", start=previous_Date, end=tday)
        df_niftyit['Date'] = pd.to_datetime(df_niftyit.index)
        df_niftyit['Date'] = df_niftyit['Date'].apply(mpl_dates.date2num)

        df_niftyit = df_niftyit.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]

        rsdata_it = pd.merge(df_nifty, df_niftyit, left_index=True, right_index=True)

        rsdata_it['Relative Strength'] = rsdata_it["Close_y"]/rsdata_it["Close_x"]


        rs_df["IT"] = (rsdata_it['Relative Strength'].pct_change() + 1).cumprod()

        df_it = rsdata_it[['Date_x', 'Relative Strength']]
        fig_it = px.line(df_it, y='Relative Strength', title='Relative Strength - IT')
        #st.plotly_chart(fig_it)

        stringdate1 = str(tday)
        stringdate2 = str(previous_Date)

        lastconnection = datetime.datetime.strptime(stringdate1, "%Y-%m-%d").strftime("%d/%m/%Y")
        firstconnection = datetime.datetime.strptime(stringdate2, "%Y-%m-%d").strftime("%d/%m/%Y")

        #df_niftyit = yf.download('^CNXAUTO', interval="1d", start=previous_Date, end=tday)
        dfnifty_commodities = fetch_investingcom_hist(sym = "Nifty Pharma", country = "India", startdate = str(firstconnection), enddate = str(lastconnection))
        dfnifty_commodities['Date'] = pd.to_datetime(dfnifty_commodities.index)
        dfnifty_commodities['Date'] = dfnifty_commodities['Date'].apply(mpl_dates.date2num)

        dfnifty_commodities = dfnifty_commodities.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]

        rsdata_commodities = pd.merge(df_nifty, dfnifty_commodities, left_index=True, right_index=True)

        rsdata_commodities['Relative Strength'] = rsdata_commodities["Close_y"]/rsdata_commodities["Close_x"]
        rs_df["Pharma"] = (rsdata_commodities['Relative Strength'].pct_change() + 1).cumprod()
        df_commodities = rsdata_commodities[['Date_x', 'Relative Strength']]
        fig_commodities = px.line(df_commodities, y='Relative Strength', title='Relative Strength - Pharma')
        #st.plotly_chart(fig_commodities)


        
        #df_niftyit = yf.download('^CNXAUTO', interval="1d", start=previous_Date, end=tday)
        dfnifty_commodities = fetch_investingcom_hist(sym = "Nifty Auto", country = "India", startdate = str(firstconnection), enddate = str(lastconnection))
        dfnifty_commodities['Date'] = pd.to_datetime(dfnifty_commodities.index)
        dfnifty_commodities['Date'] = dfnifty_commodities['Date'].apply(mpl_dates.date2num)

        dfnifty_commodities = dfnifty_commodities.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]

        rsdata_commodities = pd.merge(df_nifty, dfnifty_commodities, left_index=True, right_index=True)

        rsdata_commodities['Relative Strength'] = rsdata_commodities["Close_y"]/rsdata_commodities["Close_x"]
        df_commodities = rsdata_commodities[['Date_x', 'Relative Strength']]
        rs_df["Auto"] = (rsdata_commodities['Relative Strength'].pct_change() + 1).cumprod()
        fig_commodities = px.line(df_commodities, y='Relative Strength', title='Relative Strength - Auto')
        #st.plotly_chart(fig_commodities)


        
        #df_niftyit = yf.download('^CNXAUTO', interval="1d", start=previous_Date, end=tday)
        dfnifty_commodities = fetch_investingcom_hist(sym = "Nifty Metal", country = "India", startdate = str(firstconnection), enddate = str(lastconnection))
        dfnifty_commodities['Date'] = pd.to_datetime(dfnifty_commodities.index)
        dfnifty_commodities['Date'] = dfnifty_commodities['Date'].apply(mpl_dates.date2num)

        dfnifty_commodities = dfnifty_commodities.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]

        rsdata_commodities = pd.merge(df_nifty, dfnifty_commodities, left_index=True, right_index=True)

        rsdata_commodities['Relative Strength'] = rsdata_commodities["Close_y"]/rsdata_commodities["Close_x"]
        rs_df["Metal"] = (rsdata_commodities['Relative Strength'].pct_change() + 1).cumprod()
        df_commodities = rsdata_commodities[['Date_x', 'Relative Strength']]
        fig_commodities = px.line(df_commodities, y='Relative Strength', title='Relative Strength - Metals')
        #st.plotly_chart(fig_commodities)


        
        #df_niftyit = yf.download('^CNXAUTO', interval="1d", start=previous_Date, end=tday)
        dfnifty_commodities = fetch_investingcom_hist(sym = "Nifty Media", country = "India", startdate = str(firstconnection), enddate = str(lastconnection))
        dfnifty_commodities['Date'] = pd.to_datetime(dfnifty_commodities.index)
        dfnifty_commodities['Date'] = dfnifty_commodities['Date'].apply(mpl_dates.date2num)

        dfnifty_commodities = dfnifty_commodities.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]

        rsdata_commodities = pd.merge(df_nifty, dfnifty_commodities, left_index=True, right_index=True)

        rsdata_commodities['Relative Strength'] = rsdata_commodities["Close_y"]/rsdata_commodities["Close_x"]
        rs_df["Media"] = (rsdata_commodities['Relative Strength'].pct_change() + 1).cumprod()
        df_commodities = rsdata_commodities[['Date_x', 'Relative Strength']]
        fig_commodities = px.line(df_commodities, y='Relative Strength', title='Relative Strength - Media')
        #st.plotly_chart(fig_commodities)


            
        #df_niftyit = yf.download('^CNXAUTO', interval="1d", start=previous_Date, end=tday)
        dfnifty_commodities = fetch_investingcom_hist(sym = "Nifty Realty", country = "India", startdate = str(firstconnection), enddate = str(lastconnection))
        dfnifty_commodities['Date'] = pd.to_datetime(dfnifty_commodities.index)
        dfnifty_commodities['Date'] = dfnifty_commodities['Date'].apply(mpl_dates.date2num)

        dfnifty_commodities = dfnifty_commodities.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]

        rsdata_commodities = pd.merge(df_nifty, dfnifty_commodities, left_index=True, right_index=True)

        rsdata_commodities['Relative Strength'] = rsdata_commodities["Close_y"]/rsdata_commodities["Close_x"]
        rs_df["Realty"] = (rsdata_commodities['Relative Strength'].pct_change() + 1).cumprod()
        df_commodities = rsdata_commodities[['Date_x', 'Relative Strength']]
        fig_commodities = px.line(df_commodities, y='Relative Strength', title='Relative Strength - Realty')
        #st.plotly_chart(fig_commodities)


            
        #df_niftyit = yf.download('^CNXAUTO', interval="1d", start=previous_Date, end=tday)
        dfnifty_commodities = fetch_investingcom_hist(sym = "Nifty India Consumption", country = "India", startdate = str(firstconnection), enddate = str(lastconnection))
        dfnifty_commodities['Date'] = pd.to_datetime(dfnifty_commodities.index)
        dfnifty_commodities['Date'] = dfnifty_commodities['Date'].apply(mpl_dates.date2num)

        dfnifty_commodities = dfnifty_commodities.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]

        rsdata_commodities = pd.merge(df_nifty, dfnifty_commodities, left_index=True, right_index=True)

        rsdata_commodities['Relative Strength'] = rsdata_commodities["Close_y"]/rsdata_commodities["Close_x"]
        rs_df["Consumption"] = (rsdata_commodities['Relative Strength'].pct_change() + 1).cumprod()
        df_commodities = rsdata_commodities[['Date_x', 'Relative Strength']]
        fig_commodities = px.line(df_commodities, y='Relative Strength', title='Relative Strength - FMCG')
        #st.plotly_chart(fig_commodities)


        
        #df_niftyit = yf.download('^CNXAUTO', interval="1d", start=previous_Date, end=tday)
        dfnifty_commodities = fetch_investingcom_hist(sym = "Nifty Infrastructure", country = "India", startdate = str(firstconnection), enddate = str(lastconnection))
        dfnifty_commodities['Date'] = pd.to_datetime(dfnifty_commodities.index)
        dfnifty_commodities['Date'] = dfnifty_commodities['Date'].apply(mpl_dates.date2num)

        dfnifty_commodities = dfnifty_commodities.loc[:,['Date', 'Open', 'High', 'Low', 'Close']]

        rsdata_commodities = pd.merge(df_nifty, dfnifty_commodities, left_index=True, right_index=True)

        rsdata_commodities['Relative Strength'] = rsdata_commodities["Close_y"]/rsdata_commodities["Close_x"]
        rs_df["Infrastructure"] = (rsdata_commodities['Relative Strength'].pct_change() + 1).cumprod()
        df_commodities = rsdata_commodities[['Date_x', 'Relative Strength']]
        fig_commodities = px.line(df_commodities, y='Relative Strength', title='Relative Strength - Infrastructure')
        #st.plotly_chart(fig_commodities)

        rs_df = rs_df.iloc[1: , :]
        #rs_df.dropna()

        datelist = rs_df['Date'].to_list()
        datelist2 = [str(x) for x in datelist]
        #datelist2 = datelist.pop(0)
        banklist = rs_df['bank'].to_list()
        #banklist = banklist.pop(0)
        itlist = rs_df['IT'].to_list()
        #itlist = itlist.pop(0)
        autolist = rs_df['Auto'].to_list()
        #autolist = autolist.pop(0)
        medialist = rs_df['Media'].to_list()
        #medialist = medialist.pop(0)
        realtylist = rs_df['Realty'].to_list()
        #realtylist = realtylist.pop(0)
        consumptionlist = rs_df['Consumption'].to_list()
        #consumptionlist = consumptionlist.pop(0)
        infrastructuallist = rs_df['Infrastructure'].to_list()
        #infrastructuallist = infrastructuallist.pop(0)
        pharmalist = rs_df['Pharma'].to_list()
        #pharmalist = pharmalist.pop(0)


        #st.write(rs_df)





        rssector_graph = sector_graph(datelist2, banklist, itlist, autolist, medialist, realtylist, consumptionlist, infrastructuallist, pharmalist)

        st_echarts(
          rssector_graph, height=400
        )



    






########################################################################################################3

if selected_option == "Trading Strategy":

        selected5 = option_menu("", ["Equity/Cash", "Futures" ,"Options"], 
                    icons=['cash-coin', 'bar-chart' ,'alt'], 
                    menu_icon="basket", default_index=0, orientation = "horizontal")
                    #selected2

        if selected5 == "Equity/Cash":
          options_atrpdselect = st.multiselect(
                                  'ATR period values you want to consider?',
                                  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                                  [6, 7, 8, 9, 10])

          options_atrmultselect = st.multiselect(
                                  'ATR Multiplier values you want to consider?',
                                  [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0],
                                  [1.0, 1.5, 2.0, 2.5, 3.0])
          
          option_sym_suptr = st.selectbox(
                                'Select Stock for which you want to find best Supertrend Setting',
                                ('SBIN.NS', 'HDFCBANK.NS', 'CIPLA.NS'))


          d = st.date_input(
                            "Backtest Start Date",
                            datetime.date(2019, 7, 6))


          trading_capital = st.slider('How much capital do you want to deploy to trade this strategy?', 2000, 100000, 25000, 1000)                  


          if st.button('Find Optimal Settings for trade'):                                        
              with st.spinner('Wait for it...finding the best setting'): 
                df = yf.download(option_sym_suptr, start=d, interval = "1D")
                sptrcal = suptrend_cal(df, options_atrpdselect, options_atrmultselect, trading_capital)
                st.header("")
                st.info(sptrcal)
              
        
        if selected5 == "Options":
          c1, c2, c3, c4 = st.columns(4)

          #df = fnodata(tday)
          #gcmp_2 = get_cmp(df,"NIFTY")
          #price = myround(gcmp_2)

          obj = OptionStrat('Butterfly Spread', 100, {'start': 85, 'stop':115,'by':1})
          obj.long_call(90,2, 1)
          obj.long_put(90,2,1)
          op_strikelist = obj.STs.tolist()
          op_payofflist = obj.payoffs.tolist()
          maxprofit = max(op_payofflist)
          #st.write(op_strikelist[0])
          #st.write(op_payofflist)
          fig = optionspayoff_diagram(op_strikelist, op_payofflist, maxprofit) 

          st_echarts(
                      options=fig, height="400px",
                    )
      
          

          # SYMBOL price
          #spot_price = myround(gcmp_2)

          # Long call
          strike_price_long_call = c2.number_input(value = (100 + 200),label = "OTM Strike CE - BUY")
          premium_long_call = c2.number_input(label = "Price for CE Long")

          # Short call
          strike_price_short_call = c1.number_input(value = 199, label = "ATM Strike CE - SELL")
          premium_short_call = c1.number_input(label="Price for CE Short")

          # Long put
          strike_price_long_put = c4.number_input(value = (100 + 200), label = "OTM Strike PE - BUY") 
          premium_long_put = c4.number_input(label = "Price for PE Long")

          # Short put
          strike_price_short_put = c3.number_input(value = 100, label = "ATM Strike PE - SELL") 
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

#streamlit_analytics.stop_tracking()







