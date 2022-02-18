from streamlit_echarts import st_echarts


def oi_premium_bar_js(strikelist, celist, pelist, gcmp, titlegraph):

        option = {



                                "title": {
                                    "text": titlegraph,
                                    "subtext": 'Source: NSE Website'
                                },
                                "tooltip": {
                                    "trigger": 'axis'
                                },
                                "legend": {
                                    "data": ['Rainfall', 'Evaporation']
                                },
                                "toolbox": {
                                    "show": "true",
                                    "feature": {
                                    "dataView": { "show": "true", "readOnly": "false" },
                                    "magicType": { "show": "true", "type": ['line', 'bar'] },
                                    "restore": { "show": "true" },
                                    "saveAsImage": { "show": "true" }
                                    }
                                },
                                "calculable": "true",
                                "xAxis": [
                                {
                                    "type": 'category',
                                    
                                    "data": strikelist
                                },

                                ],
                                "yAxis": [
                                {
                                    "type": 'value'
                                }
                                ],
                                "series": [
                                {
                                    "name": 'CE',
                                    "type": 'bar',
                                    "itemStyle": {"color": '#C70039'},
                                    "data": celist,

                                "markPoint": {
                                            "data": [
                                                { "type": 'max', "name": 'Max' }
                                            ]
                                            },
                                "markLine": {
                                            "data": [{ 
                                                "name": 'CMP',
                                                "xAxis": gcmp
                                                }]
                                        }            
                            
                                    
                                },
                                {
                                    "name": 'PE',
                                    "type": 'bar',
                                    "itemStyle": {"color": '#2AF244'},
                                    "data": pelist,

                                    
                                "markPoint": {
                                            "data": [
                                                { "type": 'max', "name": 'Max' }
                                            ]
                                            },
                                
                                }
                                ]
                            }
    
        return(option)
              