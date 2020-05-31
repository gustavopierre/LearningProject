import requests
import json

url = 'https://api.worldtradingdata.com/api/v1/stock'
params = {
  'symbol': 'ITSA4.sa',
  'api_token': 'hhhunwQURBPnrvAWJkN18z321NXCqxqTsn1arlyXH9uk52iRCZIfgqeXU2qX'
}
response = requests.request('GET', url, params=params)
response.json()
print(response.text)
