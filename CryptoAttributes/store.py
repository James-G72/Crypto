import pandas as pd

class CryptoStorage():
    """
    CryptoStorage handles the .csv files and all data
    """
    def __init__(self, first_coin, webiste):
        """
        Initialises the object with a first
        :param first_coin:
        :param webiste:
        """
        self.latest_prices = {}
        self.Current_price(first_coin, self.latest_prices)

        self.historic_data = pd.dataframe(columns=[first_coin])

    def Current_price(self):


    def Full_data_loader(self, coins, website):
        """
        Used to load the full history of specified coins from the website
        :param coins: A dictionary or array of coins to be processed
        :param website: The front of a website. Coingecko is the only one which curretly works
        :return: None
        """

