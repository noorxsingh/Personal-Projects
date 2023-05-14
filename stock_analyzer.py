import requests
from time import sleep 

BASE_URL = "https://polygon.io/"
API_KEY = "yro_LLgVHShua3tJU6ATzzFSXbrwlBBJ"
def get_stock_data(symbol):
    endpoint = f"https://api.polygon.io/v1/open-close/{symbol}/2023-01-09?adjusted=true&apiKey=yro_LLgVHShua3tJU6ATzzFSXbrwlBBJ"
    response = requests.get(endpoint)

    data = response.json()

    if response.status_code == 200:
        data = response.json()
    else:
        print("Error occurred:", response.status_code)
    

    open = data['open']
    high = data['high']
    low = data['low']
    close = data['close']
    volume = data['volume']
    after_hours = data['afterHours']
    pre_market = data['preMarket']

    return open, high, low, close, volume, after_hours, pre_market

def get_answer():
    symbol = input("Please give the ticker symbol of the stock you would like to look at: ").upper()
    answer = input("Would you like to look at the stocks (open, high, low, close, volume, after hours, or premarker): ")


    if answer == 'open':
        open = get_stock_data(symbol)[0]
        return open
    elif answer == 'high':
        high = get_stock_data(symbol)[1]
        return high
    elif answer == 'low':
        low = get_stock_data(symbol)[2]
        return low
    elif answer == 'close':
        close = get_stock_data(symbol)[3]
        return close
    elif answer == 'volume':
       volume = get_stock_data(symbol)[4]
       return volume
    elif answer == 'after hours':
        after_hours = get_stock_data(symbol)[5]
        return after_hours
    elif answer == 'premarket':
        pre_market = get_stock_data(symbol)[6]
        return pre_market
    else:
        print("invalid answer")
        return get_answer()


result = get_answer()
print(f"The stocks is: ${result}")
