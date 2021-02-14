import pandas as pd
from bs4 import BeautifulSoup
import requests
import datetime
import re

class CryptoStorage():
    """
    CryptoStorage handles the .csv files and all data
    """
    def __init__(self, first_coin, website):
        """
        Initialises the object with a first
        :param first_coin: The storage object is initialised with the current price of a single coin
        :param website: The home page of the website that the object is to use to fetch data
        """
        self.data_origin = website
        self.latest_prices = {}
        self.Current_price(first_coin)

        self.historic_data = pd.DataFrame(data=[str(x.date()) for x in reversed(pd.date_range("2008-01-01",datetime.datetime.today().date()).to_list())],columns=["Dates"])
        self.non_decimal = re.compile(r'[^\d.]+')

    def Current_price(self, *coins):
        """
        Gets the current price of the requested coin. Uses self.data_origin to know where to look
        :param coins: Could be any number of coins in a list. This must be input as a list and not a string
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

    def Price_loader(self, coin, start="1980-01-01", end=str(datetime.datetime.today().date())):
        """
        Loads the historical data for the specified coin across the specified timespan. Defaults to the full history of the coin.
        Note that the price scraped is the "opening" price of each day.
        :param coin: A coin to be added to the historical data page
        :param start: Historical start date
        :param end: Last date to be scrapped
        :return: None
        """
        # Assembling the string with an arbitrarily early date
        url = self.data_origin+"/coins/"+coin+"/historical_data/gbp?start_date="+start+"&end_date="+end+"#panel"
        r = requests.get(url) # Fetching the page data
        html = r.content
        page = BeautifulSoup(html, "html.parser") # Beautiful soup parses the page
        table_string = page.table.tbody.text # Extracting the table text
        stuff = list(filter(None, table_string.splitlines())) # Splitting and removing blank strings
        stuff = list(filter(lambda a: a != " ", stuff)) # Some spaces are left which can be removed
        dates = stuff[0::5] # Extracting just the dates from the text
        starter = self.historic_data["Dates"].to_list().index(dates[0])
        ender = self.historic_data["Dates"].to_list().index(dates[-1])
        if coin in self.historic_data.columns:
            self.historic_data.iloc[starter:ender,self.historic_data.columns.to_list.index(coin)] = [self.non_decimal.sub('',x) for x in stuff[3::5]] # Removing the pound sign and any spaces from the price
        else:
            self.historic_data.iloc[starter:ender,self.historic_data.shape[1]] = [self.non_decimal.sub('',x) for x in stuff[3::5]]  # Removing the pound sign and any spaces from the price

