import pandas as pd
from pandas_datareader import data as web
import plotly.graph_objects as go
 
# criar um DataFrame vazio
df = pd.DataFrame()

# escolher a ação desejada
acao = 'ITUB3.SA'
 
# importar dados para o DataFrame
df = web.DataReader(acao, data_source='yahoo', start='01-01-2000')
 
# ver as 5 primeiras entradas
df.head()