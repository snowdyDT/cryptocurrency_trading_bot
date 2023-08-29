import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
from mpl_finance import candlestick_ohlc


def read_trades(file_path):
    """
    Read trades from CSV file
    :param file_path: path to CSV file
    :return: trades from CSV file
    """

    trades = pd.read_csv(file_path)
    trades['TS'] = pd.to_datetime(trades['TS'])

    return trades


def create_candlesticks(trades, time_interval):
    """
    Aggregate trades into candlesticks
    """

    candlesticks = trades.resample(time_interval, on='TS').agg({
        'PRICE': 'ohlc',
    })

    return candlesticks


def calculate_ema(data, length):
    """
    Calculate Exponential Moving Average (EMA)
    """

    return data.ewm(span=length, adjust=False).mean()


def plt_(ema, candlesticks, ema_length):
    fig, ax = plt.subplots(figsize=(10, 6))
    # Convert timestamp to float format for candlestick_ohlc
    candlestick_data = [(mdates.date2num(date), open, high, low, close)
                        for date, (open, high, low, close) in candlesticks['PRICE'].iterrows()]

    candlestick_ohlc(ax, candlestick_data, width=0.6, colorup='g', colordown='r')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
    ax.plot(ema.index, ema, label=f'EMA-{ema_length}', color='orange')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Candlestick Chart with EMA')
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()
