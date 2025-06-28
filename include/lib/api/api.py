import requests
import os
from typing import Dict 


class AlphaVantageClient:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv('api_key')
        self.base_url = 'https://www.alphavantage.co/query'
    

    def get_intraday_data(self, symbol: str, interval: str = "15min", outputsize: str = "compact") -> Dict:
        """
        Fetch intraday stock data for a given symbol.
        
        Args:
            symbol (str): stock ticker symbol
            interval (str): The time interval between data points, defalt is set to "15minutes"
            outputsize (str): The size of the output data is set to "full" by default
        Returns:
            Dict: A dictionary containing the intraday stock data

        """
        params = {
            'function': 'TIME_SERIES_INTRADAY',
            'symbol': symbol,
            'interval': interval,
            'apikey': self.api_key,
            'outputsize': outputsize
        }
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        
        return response.json()
    

    
    def get_daily_adjusted_data(self, symbol: str, outputsize: str = "compact") -> Dict:

        """
        Fetches daily adjusted stock data for a given stock ticker 
        
        
        Args:
            symbol (str): stock ticker symbol
            outputsize (str): The size of the output data is set to "full" by default
            Returns: A json file containing the daily adjusted stock data

        """

        params = {
            'function': 'TIME_SERIES_DAILY_ADJUSTED',
            'symbol': symbol,
            'apikey': self.api_key,
            'outputsize': outputsize
        }
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        
        return response.json()
    
    def get_rsi(self, symbol: str, interval: str = "15min", time_period: int = 14, datatype = "json", series_type: str = "close") -> Dict:

        """
        Fetch the Relative Strength Index (RSI) for a given stock ticker symbol.

        Args:
            symbol (str): Stock ticker symbol (e.g., 'AAPL').
            interval (str): Time interval between data points (e.g., '15min'). 
                        Default is '15min' to align with intraday data.
            time_period (int): Number of periods to use for RSI calculation. Default is 14.
            datatype (str): Format of the returned data. Default is 'json'.
            series_type (str): Price type to use for RSI calculation (e.g., 'close'). Default is 'close'.

        Returns:
            Dict: JSON-formatted response containing RSI time series data.
        """

        params = {
            'function': 'RSI',
            'symbol': symbol,
            'interval': interval,
            'time_period': time_period,
            'series_type': series_type,
            'apikey': self.api_key,
            'datatype': datatype
        }
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        
        return response.json()
    
    def get_overview(self, symbol: str) -> Dict:
        """
        Fetch the company overview for a given stock ticker symbol.

        Args:
            symbol (str): Stock ticker symbol for the overview information 

        Returns:
            Dict: JSON-formatted response containing company overview data.
        """
        params = {
            'function': 'OVERVIEW',
            'symbol': symbol,
            'apikey': self.api_key
        }
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        
        return response.json()
    
    def get_earnings(self, symbol: str) -> Dict:
        
        """
        Fetch the earnings data for a given stock ticker symbol.

        Args:
            symbol (str): Stock ticker symbol for the earnings information 

        Returns:
            Dict: JSON-formatted response containing earnings data.
        """
        params = {
            'function': 'EARNINGS',
            'symbol': symbol,
            'apikey': self.api_key
        }
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        
        return response.json()
    
