from streamlit_echarts import st_echarts


def futureoigraph_hist (datelist, currlist, nextlist):
    option = {
                "title": {
                    "text": 'Futures OI'
                },
                "tooltip": {
                    "trigger": 'axis'
                },
                "legend": {
                    "data": ['Current Month Contracts', 'Next Month Contracts']
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
                    "name": 'Current Month Contracts',
                    "type": 'line',
                    "data": currlist
                    },
                    {
                    "name": 'Next Month Contracts',
                    "type": 'line',
                    "data": nextlist
                    }
                ]
                }
    return(option)