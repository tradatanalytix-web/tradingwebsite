from time import strftime
from fetchdata_investingcom import fetch_investingcom



def globallist_get (sym, country):
    
    dftrynifty = fetch_investingcom(sym, country)
    dftrynifty["returns"] = (dftrynifty["Close"].pct_change() + 1).cumprod()
    #dftrynifty["returns"] = (dftrynifty["Close"]/dftrynifty["Close"].shift(1))
    dftrynifty_list = dftrynifty["returns"].tolist()
    dftrynifty_list1 = [float(x) for x in dftrynifty_list]
    dftrynifty_list1.pop(0)



    return(dftrynifty_list1)



def datelistget (sym, country):
    
    dftrynifty = fetch_investingcom(sym, country)
    #dftrynifty_date = dftrynifty["Date"].tolist()
    dateobj22 = list(dftrynifty.index.values)
    datelist = [str(x) for x in dateobj22]
    datelist.pop(0)
    #test_list_date = [str(i) for i in dftrynifty_date if i]



    return(datelist)

