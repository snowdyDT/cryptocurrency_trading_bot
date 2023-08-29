import pathlib
from enum import Enum

assets_dir = pathlib.Path(__file__).parent / 'assets'
prices_file_path = assets_dir / 'prices.csv'  # path to CSV file


class Ema(Enum):
    time_interval = '1H'  # 1 hour interval for candlesticks
    ema_length = 14
