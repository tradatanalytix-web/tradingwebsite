import plotly.express as px
import plotly.graph_objects as go

def get_fii_chart(df1):
    
        bu = df1.iloc[0][16]
        be = df1.iloc[0][17]
    
        animals=['FII Call Long + FII Put Short', 'FII Put Long + FII Call Short']

        fig1 = go.Figure([go.Bar(x=animals, y=[bu, be])])
        
    
    
        return(fig1)