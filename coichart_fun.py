import plotly.express as px


def coi_chart_graph(filterdata):
    coi_chart = px.bar(
            filterdata,
            x = 'STRIKE_PR',
            y = 'CHG_IN_OI', barmode='group', color='OPTION_TYP',
            color_discrete_map={
            'CE': 'red',
            'PE': 'green'},
            #height=500,width=1000,
            title="Change in Open Interest"
            )
    return(coi_chart)