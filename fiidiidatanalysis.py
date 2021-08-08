from os import name
import pandas as pd
from datetime import date, datetime

isVolDataLoad = False

def fiidiidata(tday):

    
    dayformat = datetime.strftime(tday, '%d%m%Y')
    url = 'https://archives.nseindia.com/content/nsccl/fao_participant_oi_'+ dayformat + '.csv'
    tablename = 'open_interest'
    if isVolDataLoad:
        url = 'https://archives.nseindia.com/content/nsccl/fao_participant_vol_'+ dayformat + '.csv'
        tablename = 'volume'
        
    data = pd.read_csv(url, skiprows=1)
    data = data.drop(data.index[4])
    data.insert(0, 'Date', tday)
    data.columns = [c.strip() for c in data.columns.values.tolist()]

    return(data)


 

