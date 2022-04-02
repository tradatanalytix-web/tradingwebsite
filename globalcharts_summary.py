from streamlit_echarts import st_echarts


def global_graph (datelist, indialist, uklist, uslist, southkorlist, japanlist, honkonglist, francelist, germanylist):
    option = {
                "title": {
                    #"text": 'Global Markets Tracker',
                    #"top": "bottom",
                },
                "tooltip": {
                    "trigger": 'axis'
                },
                "legend": {
                    "orient": "horizontal",
                    "top": "top",
                    "data": ["India", "United Kingdom", "United States", "South Korea", "Japan", "Hong Kong", "France", "Germany"]
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
                    "boundaryGap": "false",
                    "data": datelist
                },
                "yAxis": {
                    "type": 'value',
                    "scale": "false"
                },
                "series": [
                    {
                    "name": "India",
                    "type": 'line',
                    "data": indialist
                    },
                    {
                    "name": "United Kingdom",
                    "type": 'line',
                    "data": uklist
                    },
                    {
                    "name": "United States",
                    "type": 'line',
                    "data": uslist
                    },
                    {
                    "name": "South Korea",
                    "type": 'line',
                    "data":  southkorlist
                    },
                    {
                    "name": "Japan",
                    "type": 'line',
                    "data": japanlist
                    },
                    {
                    "name": "Hong Kong",
                    "type": 'line',
                    "data": honkonglist
                    },
                    {
                    "name": "France",
                    "type": 'line',
                    "data": francelist
                    },
                    {
                    "name": "Germany",
                    "type": 'line',
                    "data": germanylist
                    }
                ]
                }
    return(option)