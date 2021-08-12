def filterclientdat (df1, client_type):


    df1['Bullish Index Option'] = df1['Option Index Call Long'] + df1['Option Index Put Short']
    df1['Bearish Index Option'] = df1['Option Index Put Long'] + df1['Option Index Call Short']

    filterdata = df1[(df1['Client Type'] == client_type)] 

    return(filterdata)