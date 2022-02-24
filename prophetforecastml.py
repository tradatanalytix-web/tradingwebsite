# #from fastquant import *
# from fbprophet import Prophet
# import pandas as pd
# import yfinance as yf
# # from matplotlib import pyplot as plt


# def prophet_forecast_graph(sym):

#     # Pull crypto data
#     df = yf.download(sym, interval="1d", start =  "2020-01-01", end = "2022-01-01")
#     #df = get_yahoo_data(sym, "2020-01-01", "2022-01-01")

#     # Fit model on closing prices
#     ts = df.reset_index()[["Date", "Close"]]
#     ts.columns = ['ds', 'y']
#     m = Prophet(daily_seasonality=True, yearly_seasonality=True).fit(ts)
#     forecast = m.make_future_dataframe(periods=180, freq='D')

#     # Predict and plot
#     pred = m.predict(forecast)
#     fig1 = m.plot(pred)
#     #plt.title('Forecasted Daily Closing Price', fontsize=25)

#     return(fig1)