from Myround import *


def filtered_data (df, option, option_exp, option_inst, gcmp):
    upperstrike = float(myround(1.05*gcmp))
    lowerstrike = float(myround(0.95*gcmp))


    filterdata = df[(df['SYMBOL'] == option) &
            (df['EXPIRY_DT'] == option_exp) &
            (df['INSTRUMENT'] == option_inst) &
            (df['STRIKE_PR'] > lowerstrike) &
            (df['STRIKE_PR'] < upperstrike)] 

    return(filterdata)