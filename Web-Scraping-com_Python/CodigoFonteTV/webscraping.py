import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

# 1. Pegar conteúdo HTML a partir da URL
url = 'https://stats.nba.com/players/traditional/?sort=PTS&dir=-1&Season=2019-20&SeasonType=Regular%20Season&PerMode=Totals'
top10ranking = {}

rankings = {
    '3points': {'field':'FG3M','label':'3PM'},
    'points': {'field':'PTS','label':'PTS'}, 
    'assistants': {'field':'AST','label':'AST'}, 
    'rebounds': {'field':'REB','label':'REB'}, 
    'steals': {'field':'STL','label':'STL'}, 
    'blocks': {'field':'BLK','label':'BLK'}, 
}


option = Options()

option.headless = True
driver = webdriver.Firefox()
driver.get(url)
time.sleep(10)

driver.find_element_by_xpath("//div[@class='nba-stat-table']//table//thead//tr//th[@dat-field='PTS']").click()

element = driver.find_element_by_xpath("//div[@class='nba-stat-table']//table")
html_content = element.get_attribute(outerhtml)

print(html_content)

# 2. parsear o conteúdo HTML - BeautifulSoup
soup = BeautifulSoup(html_content,'html.parser')
table = soup.find(name='table')

# 3. Estruturar conteúdo em um Data Frame - Pandas
df_full = pd.read_html(str(table))[0].head(10)
df = df_full[['Unnamed: 0', 'PLAYER', 'TEAM', 'PTS']]
df.columns = ['pos', 'player', 'team', 'total']

print(df)

# 4. Transformar os dados em um Dicionário de Dados próprio

top10ranking['points'] = df.to_dict('records')

print(top10ranking['points'])

driver.quit()

# 5. Converter e salvar em um arquivo JSON
js = json.dumps(top10ranking)
fp = open('ranking.json', 'w')
fp.write(js)
fp.close()