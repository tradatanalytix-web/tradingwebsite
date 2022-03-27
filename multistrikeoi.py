from streamlit_echarts import st_echarts


def multistrikeoi_graph (datelist, atmce, atmpe, itmce, itmpe, otmce, otmpe):
    option = {
                "title": {
                    "text": 'OI'
                },
                "tooltip": {
                    "trigger": 'axis'
                },
                "legend": {
                    "data": ['17200 CE', '17200 PE', '17100 CE', '17300 PE', '17300 CE', '17100 PE']
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
                    "name": '17200 CE',
                    "type": 'line',
                    "data": atmce
                    },
                    {
                    "name": '17200 PE',
                    "type": 'line',
                    "data": atmpe
                    },
                    {
                    "name": '17100 CE',
                    "type": 'line',
                    "data": itmce
                    },
                    {
                    "name": '17300 PE',
                    "type": 'line',
                    "data": itmpe
                    },
                    {
                    "name": '17300 CE',
                    "type": 'line',
                    "data": otmce
                    },
                    {
                    "name": '17100 PE',
                    "type": 'line',
                    "data": otmpe
                    }
                ]
                }
    return(option)