import investpy


def fetch_investingcom(sym):

        data = investpy.get_index_recent_data(index=sym, 
                                                country='india')
        
        return(data)