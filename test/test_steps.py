import pandas as pd

from cryptocurrency_trading_bot import config as bot_config
from cryptocurrency_trading_bot import util as bot_util


def test_read_trades():
    result = bot_util.read_trades(file_path=bot_config.prices_file_path)
    result_ = dict(result)
    assert result_
    assert isinstance(result_, dict)
    assert 'TS' in result_
    assert 'PRICE' in result_
    assert isinstance(result_.get('TS'), pd.Series)
    assert isinstance(result_.get('PRICE'), pd.Series)


def test_create_candlesticks():
    trades = bot_util.read_trades(file_path=bot_config.prices_file_path)
    result = bot_util.create_candlesticks(trades=trades, time_interval=bot_config.Ema.time_interval.value)
    result_ = dict(result)
    assert result_
    assert isinstance(result_, dict)
    assert ('PRICE', 'open') in result_
    assert ('PRICE', 'high') in result_
    assert ('PRICE', 'low') in result_
    assert ('PRICE', 'close') in result_
    assert isinstance(result_.get(('PRICE', 'open')), pd.Series)
    assert isinstance(result_.get(('PRICE', 'high')), pd.Series)
    assert isinstance(result_.get(('PRICE', 'low')), pd.Series)
    assert isinstance(result_.get(('PRICE', 'close')), pd.Series)
