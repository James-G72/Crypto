import pandas as pd
from bs4 import BeautifulSoup
import requests

class CryptoStorage():
    """
    CryptoStorage handles the .csv files and all data
    """
    def __init__(self, first_coin, website):
        """
        Initialises the object with a first
        :param first_coin: The storage object is initialised with the current price of a single coin
        :param webiste: The home page of the website that the object is to use to fetch data
        """
        self.data_origin = website
        self.latest_prices = {}
        self.Current_price(first_coin)

        # self.historic_data = pd.dataframe(columns=[first_coin])

    def Current_price(self, *coins):
        """
        Gets the current price of the requested coin. Uses self.data_origin to know where to look
        :param coins: Could be any number of coins in a list
        :return: time_stamp - The exact time the data was true, prices - Dictionary of coins and prices
        """

        def Single_value_scrape(url):
            r = requests.get(url)
            html = r.content
            page = BeautifulSoup(html, "html.parser")
            return page.find(id="initial_price")["value"]

        latest = self.latest_prices
        for coin in coins:
            url = self.data_origin+'/coins/'+coin+'/gbp'
            price = Single_value_scrape(url)
            latest[coin] = price
        self.latest_prices = latest

    def Full_price_loader(self, coin):
        """
        Used to load the full history of specified coins from the website
        :param coins: A dictionary or array of coins to be processed
        :param website: The front of a website. Coingecko is the only one which currently works
        :return: None
        """
        url = self.data_origin+'/coins/'+coin+'/historical_data/gbp#panel'
        r = requests.get(url)
        html = r.content
        page = BeautifulSoup(html,"html.parser")
        table_string = page.table.tbody.text
        stuff = list(filter(None, table_string.splitlines()))

        print(stuff)

