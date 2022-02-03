def pcr_gauge_graph(pcr):
    option = {
                "series": [
                    {
                    "type" : 'gauge',
                    "axisLine" : {
                        "lineStyle": {
                        "width" : 30,
                        "color": [
                            [0.5, '#C70039'],
                            #[0.7, '#FFD700'],
                            [1, '#2AF244']
                        ]
                        }
                    },
                    "pointer": {
                        "itemStyle": {
                        "color": 'auto'
                        }
                    },
                    "axisTick": {
                        "distance": -30,
                        "length": 8,
                        "lineStyle": {
                        "color": '#fff',
                        "width": 2
                        }
                    },
                    "splitLine": {
                        "distance": -30,
                        "length": 30,
                        "lineStyle": {
                        "color": '#fff',
                        "width": 4
                        }
                    },
                    "axisLabel": {
                        "color": 'auto',
                        "distance": 40,
                        "fontSize": 20
                    },
                    "detail": {
                        "valueAnimation": "true",
                        "formatter": 'Sentiment',
                        "fontSize": 10,
                        "color": '#191970'
                    },
                    "data": [
                        {
                        "value": pcr
                        }
                    ]
                    }
                ]
                }
                
    return(option)