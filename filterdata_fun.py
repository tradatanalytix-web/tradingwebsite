def filtered_data (df, option, option_exp, option_inst):
    
    filterdata = df[(df['SYMBOL'] == option) &
            (df['EXPIRY_DT'] == option_exp) &
            (df['INSTRUMENT'] == option_inst)]

    return(filterdata)