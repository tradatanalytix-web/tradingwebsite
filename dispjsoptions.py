from streamlit_echarts import st_echarts


def optionspayoff_diagram (op_strikelist, op_payofflist, maxprofit):
    option = {
                
                "tooltip": {
                    "trigger": 'axis',
                    "axisPointer": {
                    "type": 'cross',
                    "label": {
                        "backgroundColor": '#6a7985'
                    }
                    }
                },

                        "visualMap": {
                            "top": 10,
                            "right": 10,
                            "pieces": [{
                                "gt": 0,
                                "lte": 100,
                                "color": '#096'
                            }],
                            "outOfRange": {
                                "color": '#7e0023'
                            }
                        },
                "xAxis": {
                    "type": 'category',
                    "boundaryGap": "false",
                    "data": op_strikelist
                },
                "yAxis": {
                    "type": 'value'
                },
                "series": [
                    {
                    "data": op_payofflist,
                    "type": 'line',
                    "areaStyle": {}
                    }
                ]
                }
    return(option)
            
