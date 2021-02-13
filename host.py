from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
import time


def get_price(*coins):
    def scrape(url):
        r = requests.get(url)
        html = r.content
        page = BeautifulSoup(html, "html.parser")
        print(page)
        return page.find(id="initial_price")["value"]

    output = {}
    for coin in coins:
        url = 'https://www.coingecko.com/en/coins/'+coin+'/gbp'
        price = scrape(url)
        output[coin] = price

    return output

results = get_price(
    'bitcoin',
    'ethereum',
    'ripple',
    'golem')

for coin,price in results.items():
    print(" - ",coin + ":", price)




# cmc = requests.get("https://www.coingecko.com/en")
# soup = BeautifulSoup(cmc.content, "html.parser")
# data = soup.find("script", id="__NEXT_DATA__", type="application/json")
# coins = {}
# coin_data = json.loads(data.contents[0])
# listings = coin_data["props"]["initialState"]["cryptocurrency"]["listingLatest"]["data"]
# for i in listings:
#     coins[str(i["id"])] = i["slug"]
#
# market_cap = []
# volume = []
# timestamp = []
# name = []
# symbol = []
# slug = []
#
# for i in coins:
#     page = requests.get(f"https://www.coingecko.com/en/coins/bitcoin/historical_data/gbp")
#     soup = BeautifulSoup(page.content, "html.parser")
#     data = soup.find("script", id="__NEXT_DATA__", type="application/json")
#
# for i in coins:
#     historical_data = json.loads(data.contents[0])
#     quotes = historical_data["props"]["initialState"]["cryptocurrency"]["ohlcvHistorical"][i]["quotes"]
#     info = historical_data['props']['initialState']['cryptocurrency']['ohlcvHistorical'][i]
#     for j in quotes:
#         market_cap.append(j["quote"]["USD"]["market_cap"])
#         volume.append(j["quote"]["USD"]["volume"])
#         timestamp.append(j["quote"]["USD"]["timestamp"])
#         name.append(info["name"])
#         symbol.append(info["symbol"])
#         slug.append(coins[i])
