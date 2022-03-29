from streamlit_echarts import st_echarts


def multistrikeoi_graph (datelist, atmce, atmpe, itmce, itmpe, otmce, otmpe, t1, t2, t3, t4, t5, t6):
    option = {
                "title": {
                    "text": 'OI'
                },
                "tooltip": {
                    "trigger": 'axis'
                },
                "legend": {
                    "data": [t1, t2, t3, t4, t5, t6]
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
                    "type": 'value'
                },
                "series": [
                    {
                    "name": t1,
                    "type": 'line',
                    "data": atmce
                    },
                    {
                    "name": t2,
                    "type": 'line',
                    "data": atmpe
                    },
                    {
                    "name": t3,
                    "type": 'line',
                    "data": itmce
                    },
                    {
                    "name": t4,
                    "type": 'line',
                    "data": itmpe
                    },
                    {
                    "name": t5,
                    "type": 'line',
                    "data": otmce
                    },
                    {
                    "name": t6,
                    "type": 'line',
                    "data": otmpe
                    }
                ]
                }
    return(option)