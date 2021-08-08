import plotly.express as px


def coi_chart_graph(filterdata):
        coi_chart = px.bar(
            filterdata,
            x = 'STRIKE_PR',
            y = 'CHG_IN_OI', barmode='group', color='OPTION_TYP',
            color_discrete_map={
            'CE': 'red',
            'PE': 'green'},
            height=600,
            width=850,

            labels={
                     'STRIKE_PR': "Strike Price",
                     'CHG_IN_OI': "Change in Open Interest"
                 },

            title="Change in Open Interest"
            )

        fig = coi_chart.update_layout(legend=dict( orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1,
                ))

        return(fig)