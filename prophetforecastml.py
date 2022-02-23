from fastquant import *
from fbprophet import Prophet
import pandas as pd
from matplotlib import pyplot as plt


def prophet_forecast_graph(sym):

    # Pull crypto data
    df = get_yahoo_data(sym, "2020-01-01", "2022-01-01")

    # Fit model on closing prices
    ts = df.reset_index()[["dt", "close"]]
    ts.columns = ['ds', 'y']
    m = Prophet(daily_seasonality=True, yearly_seasonality=True).fit(ts)
    forecast = m.make_future_dataframe(periods=180, freq='D')

    # Predict and plot
    pred = m.predict(forecast)
    fig1 = m.plot(pred)
    #plt.title('Forecasted Daily Closing Price', fontsize=25)

    return(fig1)