import requests
import json
import pandas as pd


def fetch_optionschain(symbol, exp_date): 
    url = 'https://trendlyne.com/futures-options/api/options/'+exp_date+'-next/1887/'+symbol
    
    headers = {"accept-encoding": "gzip, deflate, br",
               "accept-language": "en-US,en;q=0.9",
               "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}
    
    response = requests.get(url, headers=headers).text
    
    data = json.loads(response)
    
    new_dict = {}
    if data['tableData'] == []:
        raise Exception("Data table empty")
    else: 
        for i in data['tableData']: 
            new_dict[i['strike_price']] = {"strike_price": i['strike_price'],"ce_ltp": i['Call'][0], "ce_ltp_ch": i['Call'][1], "ce_volume": i['Call'][2], "ce_volume_ch":  i['Call'][3], "ce_OI":  i['Call'][5], "ce_OI_ch":  i['Call'][6] ,
                         "pe_ltp": i['Put'][0], "pe_ltp_ch": i['Put'][1], "pe_volume": i['Put'][2], "pe_volume_ch":  i['Put'][3], "pe_OI":  i['Put'][5], "pe_OI_ch":  i['Put'][6]}
        
        df = pd.DataFrame.from_dict(new_dict).transpose()
        
        return df
