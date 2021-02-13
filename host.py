import CryptoAttributes as CA

coin_gecko = 'https://www.coingecko.com/en'

storage = CA.CryStor("bitcoin", coin_gecko)

storage.Full_price_loader("bitcoin")

for coin, price in storage.latest_prices.items():
    print(" - ",coin + ":", price)
