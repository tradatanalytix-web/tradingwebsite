from os import name
import pandas as pd
from datetime import date, datetime

#data

def fnodata(tday):


        dd = datetime.strftime(tday,'%d')
        MM = datetime.strftime(tday, '%b').upper()
        YYYY = datetime.strftime(tday, '%Y')
        fnoBhavcopyUrl = 'https://archives.nseindia.com/content/historical/DERIVATIVES/' +YYYY+ '/' +MM +'/fo'+dd+ MM + YYYY+'bhav.csv.zip'

        datafno = pd.read_csv(fnoBhavcopyUrl, parse_dates=['EXPIRY_DT', 'TIMESTAMP'])
        datafno = datafno.drop(datafno.columns[15:], axis=1)

        datafno.columns = [c.strip() for c in datafno.columns.values.tolist()]
        
        return(datafno)

    


