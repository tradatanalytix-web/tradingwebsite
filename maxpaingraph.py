from streamlit_echarts import st_echarts


def maxxpain (strikelist, celist, pelist):
    option = {
                "tooltip": {
                    "trigger": 'axis',
                    "axisPointer": {
                    "type": 'shadow' 
                    }
                },
                "legend": {},
                "grid": {
                    "left": '3%',
                    "right": '4%',
                    "bottom": '3%',
                    "containLabel": "false"
                },
                "yAxis": {
                    "type": 'value'
                },
                "xAxis": {
                    "type": 'category',
                    "data": strikelist
                },
                "series": [
                    {
                    "name": 'Direct',
                    "type": 'bar',
                    "stack": 'total',
                    "label": {
                        "show": "false"
                    },
                    "emphasis": {
                        "focus": 'series'
                    },
                    "data": celist
                    },
                    {
                    "name": 'Mail Ad',
                    "type": 'bar',
                    "stack": 'total',
                    "label": {
                        "show": "false"
                    },
                    "emphasis": {
                        "focus": 'series'
                    },
                    "data": pelist
                    }]
                }
        
    return(option)