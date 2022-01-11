import requests
import json
import pandas as pd
import time

def oc(sym, exp_date):
    url = "https://www.nseindia.com/api/option-chain-indices?symbol="+sym
    headers = {"accept-encoding": "gzip, deflate, br",
              "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
              "referer": "https://www.nseindia.com/get-quotes/derivatives?symbol="+sym,
              "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36}"
              }
    
    response = requests.get(url, headers = headers).text
    data = json.loads(response)
    exp_list = data['records']['expiryDates']
    ce = {}
    pe = {}
    n = 0
    m = 0
    for i in data['records']['data']:
        if i['expiryDate'] == exp_date:
            try:
                ce[n] = i['CE']
                n = n+1
            except:
                pass
            try:
                pe[n] = i["PE"]
                m = m+1
            except:
                pass
    ce_df = pd.DataFrame.from_dict(ce).transpose()
    pe_df = pd.DataFrame.from_dict(pe).transpose()
    ce_df.columns += "_CE"
    pe_df.columns += "_PE"
    df = pd.concat([ce_df, pe_df], axis = 1)
    return(response)