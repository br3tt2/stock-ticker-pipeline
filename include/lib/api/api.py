import requests
import os
from typing import Dict 


class AlphaVantageClient:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv('api_key')
        self.base_url = 'https://www.alphavantage.co/query'
    

    def get_intraday_data(self, symbol: str, interval: str = "15min", output_size: str = "full") -> Dict:
        """
        Fetch intraday stock data for a given symbol.
        
        Args:
            symbol (str): stock ticker symbol
            interval (str): The time interval between data points, defalt is set to "15minutes"
            output_size (str): The size of the output data is set to "full" by default
        Returns:
            Dict: A dictionary containing the intraday stock data

        """
        params = {
            'function': 'TIME_SERIES_INTRADAY',
            'symbol': symbol,
            'interval': interval,
            'apikey': self.api_key,
            'outputsize': output_size
        }
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        
        return response.json()