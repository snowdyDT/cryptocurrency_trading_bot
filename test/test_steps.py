import os

import pandas as pd

from cryptocurrency_trading_bot import config as bot_config
from cryptocurrency_trading_bot import util as bot_util


def test_read_trades():
    trades = bot_util.Trades()
    result = trades.read()
    result_ = dict(result)
    assert result_
    assert isinstance(result_, dict)
    assert 'TS' in result_
    assert 'PRICE' in result_
    assert isinstance(result_.get('TS'), pd.Series)
    assert isinstance(result_.get('PRICE'), pd.Series)


def test_create_candlesticks():
    trades = bot_util.Trades()
    candlesticks = bot_util.Candlesticks()

    trades_ = trades.read()
    candlesticks.trades = trades_
    result = candlesticks.create()
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


def test_calculate_ema():
    trades = bot_util.Trades()
    candlesticks = bot_util.Candlesticks()
    ema = bot_util.Ema()

    trades_ = trades.read()
    candlesticks.trades = trades_
    candlesticks_ = candlesticks.create()
    ema.data = candlesticks_['PRICE']['close']
    result = ema.calculate()
    result_ = list(result)
    assert result_
    assert isinstance(result_, list)
    for ema_value in result_:
        assert ema_value
        assert isinstance(ema_value, float)


def test_plt_show():
    trades = bot_util.Trades()
    candlesticks = bot_util.Candlesticks()
    ema = bot_util.Ema()
    visualization = bot_util.Visualization()

    trades_ = trades.read()
    trades_dict = dict(trades_)
    assert trades_dict
    assert isinstance(trades_dict, dict)
    assert 'TS' in trades_dict
    assert 'PRICE' in trades_dict
    assert isinstance(trades_dict.get('TS'), pd.Series)
    assert isinstance(trades_dict.get('PRICE'), pd.Series)

    candlesticks.trades = trades_
    candlesticks_ = candlesticks.create()
    candlesticks_dict = dict(candlesticks_)
    assert candlesticks_dict
    assert isinstance(candlesticks_dict, dict)
    assert ('PRICE', 'open') in candlesticks_dict
    assert ('PRICE', 'high') in candlesticks_dict
    assert ('PRICE', 'low') in candlesticks_dict
    assert ('PRICE', 'close') in candlesticks_dict
    assert isinstance(candlesticks_dict.get(('PRICE', 'open')), pd.Series)
    assert isinstance(candlesticks_dict.get(('PRICE', 'high')), pd.Series)
    assert isinstance(candlesticks_dict.get(('PRICE', 'low')), pd.Series)
    assert isinstance(candlesticks_dict.get(('PRICE', 'close')), pd.Series)

    ema.data = candlesticks_['PRICE']['close']
    ema_ = ema.calculate()
    ema_list = list(ema_)
    assert ema_list
    assert isinstance(ema_list, list)
    for ema_value in ema_list:
        assert ema_value
        assert isinstance(ema_value, float)

    visualization.ema = ema_
    visualization.candlesticks = candlesticks_
    visualization.show()


def test_file_path():
    file_path = bot_config.prices_file_path

    if os.path.exists(file_path):
        pd.read_csv(file_path)
    else:
        raise FileNotFoundError(f"No such file or directory: {file_path}")
