import plotly.express as px


def ironbutterfly(options_chart, sT):

    figib = px.line(x = sT, y = options_chart)
    figib.add_hline(y=0)

    return(figib)