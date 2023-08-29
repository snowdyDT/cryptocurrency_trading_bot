import os

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
from mpl_finance import candlestick_ohlc

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
        fig, ax = plt.subplots(figsize=(10, 6))
        # Convert timestamp to float format for candlestick_ohlc
        candlestick_data = [(mdates.date2num(date), open, high, low, close)
                            for date, (open, high, low, close) in self.candlesticks['PRICE'].iterrows()]

        candlestick_ohlc(ax, candlestick_data, width=0.6, colorup='g', colordown='r')
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
        ax.plot(self.ema.index, self.ema, label=f'EMA-{self.ema_length}', color='orange')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title('Candlestick Chart with EMA')
        plt.legend()
        plt.xticks(rotation=45)
        plt.show()
