from fetchdata_investingcom import fetch_investingcom



def globaldashboard_metric(sym, country):
    dftrynifty = fetch_investingcom(sym, country)
    #dftrynifty = fetch_investingcom('Hang Seng', 'Hong Kong')
    hancmp = dftrynifty.iloc[len(dftrynifty)-1]['Close']
    hanchangepc = (dftrynifty.iloc[len(dftrynifty)-1]['Close'] - dftrynifty.iloc[len(dftrynifty)-2]['Close'])/dftrynifty.iloc[len(dftrynifty)-2]['Close']
    hanchangepc = "{:.2%}".format(hanchangepc)



    return(hancmp, hanchangepc)