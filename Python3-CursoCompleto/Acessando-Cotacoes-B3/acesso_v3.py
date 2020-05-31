import requests
import json

url = 'https://api.worldtradingdata.com/api/v1/forex_history'
params = {
    'base': 'USD',
    'convert_to': 'BRL',
    'api_token': 'hhhunwQURBPnrvAWJkN18z321NXCqxqTsn1arlyXH9uk52iRCZIfgqeXU2qX'
}
response = requests.request('GET', url, params=params)
response.json()
print(type(response.text))
print(type(response))
