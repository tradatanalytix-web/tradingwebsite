import plotly.express as px


def oi_chart_graph(filterdata):
    oi_chart = px.bar(
            filterdata,
            x = 'STRIKE_PR',
            y = 'OPEN_INT', barmode='group', color='OPTION_TYP',
            color_discrete_map={
            'CE': 'red',
            'PE': 'green'},
            #height=500,width=1000,
            title="Open Interest"
            )
    return(oi_chart)
