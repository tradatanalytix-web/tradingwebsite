from Myround import *


def filtered_data_future (df, option, option_inst):


    filterdata = df[(df['SYMBOL'] == option) &
            (df['INSTRUMENT'] == option_inst)] 

    return(filterdata)