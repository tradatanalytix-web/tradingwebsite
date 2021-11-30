def pcr_cal (df, option, option_exp, option_inst):
    
    filterdata_pcr_ce = df[(df['SYMBOL'] == option) &
            (df['EXPIRY_DT'] == option_exp) &
            (df['INSTRUMENT'] == option_inst) &
            (df['OPTION_TYP'] == "CE")] 

    filterdata_pcr_pe = df[(df['SYMBOL'] == option) &
            (df['EXPIRY_DT'] == option_exp) &
            (df['INSTRUMENT'] == option_inst) &
            (df['OPTION_TYP'] == "PE")] 

    pcr_value = filterdata_pcr_pe['OPEN_INT'].sum() /  filterdata_pcr_ce['OPEN_INT'].sum()

    return(pcr_value)
