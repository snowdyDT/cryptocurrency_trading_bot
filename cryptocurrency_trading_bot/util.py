import os

import mplfinance as mpf
import pandas as pd

from cryptocurrency_trading_bot import config as bot_config


class Trades:
    def __init__(self,
                 file_path=bot_config.prices_file_path):
        self.file_path = file_path

    def read(self):
        """
        Read trades from CSV file
        """

        if os.path.exists(self.file_path):
            trades = pd.read_csv(self.file_path)
            trades['TS'] = pd.to_datetime(trades['TS'])
        else:
            raise FileNotFoundError(f"No such file or directory: {self.file_path}")

        return trades


class Candlesticks:
    def __init__(self,
                 time_interval=bot_config.Ema.time_interval.value):
        self.trades = None
        self.time_interval = time_interval

    def create(self):
        """
        Aggregate trades into candlesticks
        """

        candlesticks = self.trades.resample(self.time_interval, on='TS').agg({
            'PRICE': 'ohlc',
        })

        return candlesticks


class Ema:
    def __init__(self,
                 length=bot_config.Ema.ema_length.value):
        self.data = None
        self.length = length

    def calculate(self):
        """
        Calculate Exponential Moving Average (EMA)
        """

        return self.data.ewm(span=self.length, adjust=False).mean()


class Visualization:
    def __init__(self,
                 ema_length=bot_config.Ema.ema_length.value):
        self.ema = None
        self.candlesticks = None
        self.ema_length = ema_length

    def show(self):
        """
        Show graphic of result by mplfinance
        """
        mpf.plot(self.candlesticks['PRICE'])
