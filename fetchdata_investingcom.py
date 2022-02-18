import investpy


def fetch_investingcom(sym, country):

        data = investpy.get_index_recent_data(index=sym, 
                                                country=country)
        
        return(data)