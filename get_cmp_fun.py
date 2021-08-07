import pandas as pd
import numpy as np


def get_cmp (df, option):

    filterdata = df[(df['SYMBOL'] == option)]


    gcmp = filterdata.loc[filterdata.INSTRUMENT == "FUTIDX", "CLOSE"].mean()
    return(gcmp)