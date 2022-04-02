from streamlit_echarts import st_echarts


def sector_graph (datelist, banklist, itlist, autolist, medialist, realtylist, consumptionlist, infrastructurallist, pharmalist):
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
                    "data": ["Bank", "IT", "Auto", "Media", "Realty", "Consumption", "Infra", "Pharma"]
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
                    "name": "Bank",
                    "type": 'line',
                    "data": banklist
                    },
                    {
                    "name": "IT",
                    "type": 'line',
                    "data": itlist
                    },
                    {
                    "name": "Auto",
                    "type": 'line',
                    "data": autolist
                    },
                    {
                    "name": "Media",
                    "type": 'line',
                    "data":  medialist
                    },
                    {
                    "name": "Realty",
                    "type": 'line',
                    "data": realtylist
                    },
                    {
                    "name": "Consumption",
                    "type": 'line',
                    "data": consumptionlist
                    },
                    {
                    "name": "Infra",
                    "type": 'line',
                    "data": infrastructurallist
                    },
                    {
                    "name": "Pharma",
                    "type": 'line',
                    "data": pharmalist
                    }
                ]
                }
    return(option)