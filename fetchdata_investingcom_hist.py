import investpy
import investpy



def fetch_investingcom_hist(sym, country, startdate, enddate):

        data = investpy.get_index_historical_data(index=sym, 
                                                country=country,
                                                from_date = startdate, 
                                                to_date = enddate)
        
        return(data)