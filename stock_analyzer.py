import requests

BASE_URL = "https://polygon.io/"
API_KEY = "YOUR_OWN_API_KEY_YOUR_OWN_API_KEY_YOUR_OWN_API_KEY_YOUR_OWN_API_KEY"

def get_stock_data(symbol):
    
    endpoint = f"https://api.polygon.io/v1/open-close/{symbol}/2023-01-09?adjusted=true&apiKey={API_KEY}"
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
    answer = input("Would you like to look at the stocks (open, high, low, close, volume, after hours, premarker, or all data(all)): ")
     
    if answer == 'open':
        open = get_stock_data(symbol)[0]
        return answer, open
    elif answer == 'high':
        high = get_stock_data(symbol)[1]
        return answer, high
    elif answer == 'low':
        low = get_stock_data(symbol)[2]
        return answer, low
    elif answer == 'close':
        close = get_stock_data(symbol)[3]
        return answer, close
    elif answer == 'volume':
       volume = get_stock_data(symbol)[4]
       return answer, volume
    elif answer == 'after hours':
        after_hours = get_stock_data(symbol)[5]
        return answer, after_hours
    elif answer == 'premarket':
        pre_market = get_stock_data(symbol)[6]
        return answer, pre_market
    elif answer == 'all':
        return answer, get_stock_data(symbol)
    else:
        print("invalid answer")
        return get_answer()

answer, result = get_answer()

if answer == 'all':
    print("Stock data:")
    print(f"Open: ${result[0]}")
    print(f"High: ${result[1]}")
    print(f"Low: ${result[2]}")
    print(f"Close: ${result[3]}")
    print(f"Volume: {result[4]}")
    print(f"After Hours: ${result[5]}")
    print(f"Premarket: ${result[6]}")
else:
    print(f"The stock's {answer} is: ${result}")

def get_news_data(symbol):
   
    endpoint_2 = f"https://api.polygon.io/v2/reference/news?ticker={symbol}&apiKey={API_KEY}"
    response_2 = requests.get(endpoint_2)

    data_2 = response_2.json()

    if response_2.status_code == 200:
        data_2 = response_2.json()
    else:
        print("Error occurred:", response_2.status_code)
    news_articles = data_2['results']
    return news_articles

symbol_2 = input("Would you like to see the news for the ticker symbol, if so please re-enter the ticker symbol or enter a new one: ").upper()

endpoint_2 = f"https://api.polygon.io/v2/reference/news?ticker={symbol_2}&apiKey={API_KEY}"
response_2 = requests.get(endpoint_2)

data_2 = response_2.json()

news_articles = data_2['results']

if response_2.status_code == 200:
    data_2 = response_2.json()
else:
    print("Error occurred:", response_2.status_code)

author = data_2['results'][0]['author']
description = data_2['results'][0]['description']
publisher = data_2['results'][0]['publisher']
published_time = data_2['results'][0]['published_utc']
article_url = data_2['results'][0]['article_url']
involved_tickers = data_2['results'][0]['tickers']
# give a list of the articles for example where it says [0] or [1]
# give a list to the user so they can find and see which one gives them better data

print(author)
print("------------------------------------")
print(description)
print("------------------------------------")
print(publisher)
print("------------------------------------")
print(published_time)
print("------------------------------------")
print(article_url)
print("------------------------------------")
print(involved_tickers)
