import CryptoAttributes as CA

coin_gecko = 'https://www.coingecko.com/en'

storage = CA.CryStor("bitcoin", coin_gecko)

storage.Price_loader("bitcoin")
storage.Price_loader("ethereum")

for coin, price in storage.latest_prices.items():
    print(" - ",coin + ":", price)
