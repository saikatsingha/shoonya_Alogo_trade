import requests
import json
import time
import datetime
import array as arr 

api_endpoint = f"https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"

headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'DNT': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
        'Sec-Fetch-User': '?1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
    }

s = requests.Session()
response = s.get(api_endpoint, headers=headers)
# data = json.loads(response.content)
# print('Please enter any expiary from the following')
# for i in data['records']['expiryDates']:
#     print(i)
# print('Please enter any expiary from the above')
# expiary = str(input())

expiary = '11-Jul-2024'
market_end_time="23:30:00"
while True:
    current_time = datetime.datetime.now().time().strftime('%H:%M:%S')
    if current_time <= market_end_time:
        # print(f"Current Time is {current_time }")
        
        response = s.get(api_endpoint, headers=headers)
        data = json.loads(response.content)
        # print(data['records']['data'][0])
        underlyingValue = data['records']['data'][0]['PE']['underlyingValue']
        # print(f"Nifty Present Value is {underlyingValue }")
        find_put = underlyingValue - (underlyingValue%100)
        find_call = find_put + 100
        # print(find_call)
        # print(find_put)

        x = 0
        for i in data['records']['data']:
            if (data['records']['data'][x]['expiryDate'] == expiary) and (data['records']['data'][x]['strikePrice'] == find_put):
                y=0
                for y in (data['records']['data'][x]['PE']):
                    # numbers = arr.array(data['records']['data'][x]['PE'][y])
                    # index = data['records']['data'][x]['PE'].index(data['records']['data'][x]['PE'][y])
                    print(y)
                    print(data['records']['data'][x]['PE'][y])
                # print(f"Put Value of the Strike Price  {find_put} is {data['records']['data'][x]['PE']['lastPrice']}")
                # print(f"Call Value of the Strike Price {find_put} is {data['records']['data'][x]['CE']['lastPrice']}")
            if (data['records']['data'][x]['expiryDate'] == expiary) and (data['records']['data'][x]['strikePrice'] == find_call):
                    # print(f"Put Value of the Strike Price  {find_call} is {data['records']['data'][x]['PE']['lastPrice']}")
                    # print(f"Call Value of the Strike Price {find_call} is {data['records']['data'][x]['CE']['lastPrice']}")
                break
            x = x+1
    
    else:
        break

    time.sleep(60)
