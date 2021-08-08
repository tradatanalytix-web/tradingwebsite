import plotly.express as px


def get_fii_chart(df1):
    fii_chart = px.bar(
            df1,
            x = 'Date',
            y = 'Future Index Long', 
            #barmode='group', color='OPTION_TYP',
            #color_discrete_map={
            #'CE': 'red',
            #'PE': 'green'},
            height=600,
            width=800,

            #labels={
            #         'STRIKE_PR': "Strike Price",
            #         'CHG_IN_OI': "Change in Open Interest"
            #     },

            title="FII Future Index Long"
            )

    fig = fii_chart.update_layout(legend=dict( orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1,
                ))

    return(fig)