from streamlit_echarts import st_echarts


def pcrchart_hist(datelist, pcrlist):
    option = {
                "title": {
                    "text": 'PCR Historical Data'
                },
                "tooltip": {
                    "trigger": 'axis'
                },
                "legend": {
                    "data": ['PCR']
                },
                "grid": {
                    "left": '3%',
                    "right": '4%',
                    "bottom": '3%',
                    "containLabel": "true"
                },
                "toolbox": {
                    "feature": {
                    "saveAsImage": {}
                    }
                },
                "xAxis": {
                    "type": 'category',
                    "data": datelist
                },
                "yAxis": {
                    "type": 'value'
                },
                "series": [
                    {
                    "data": pcrlist,
                    "type": 'line'
                    }
                ]
                }
    return(option)