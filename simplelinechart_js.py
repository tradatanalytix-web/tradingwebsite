from streamlit_echarts import st_echarts


def linechart_js(datelist, symlist):
    option = {
        "xAxis": {
            "type": 'category',
            "data": datelist
        },
        "yAxis": {
            "type": 'value'
        },
        "series": [
            {
            "data": symlist,
            "type": 'line'
            }
        ]
        }
    
    return(option)