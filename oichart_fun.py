import plotly.express as px


def oi_chart_graph(filterdata):
        oi_chart = px.bar(
            filterdata,
            x = 'STRIKE_PR',
            y = 'OPEN_INT', barmode='group', color='OPTION_TYP',
            color_discrete_map={
            'CE': 'red',
            'PE': 'green'},
            height=600,
            width=850,

            labels={
                     'STRIKE_PR': "Strike Price",
                     'OPEN_INT': "Open Interest"
                 },

            title="Open Interest"
            )

        fig = oi_chart.update_layout(legend=dict( orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1,
                ))

        
    
        return(fig)
