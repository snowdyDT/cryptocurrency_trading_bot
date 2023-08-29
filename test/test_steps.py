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


def test_calculate_ema():
    trades = bot_util.read_trades(file_path=bot_config.prices_file_path)
    candlesticks = bot_util.create_candlesticks(trades=trades, time_interval=bot_config.Ema.time_interval.value)
    result = bot_util.calculate_ema(data=candlesticks['PRICE']['close'], length=bot_config.Ema.ema_length.value)
    result_ = list(result)
    assert result_
    assert isinstance(result_, list)
    for ema in result_:
        assert ema
        assert isinstance(ema, float)


def test_plt_show():
    trades = bot_util.read_trades(file_path=bot_config.prices_file_path)
    trades_ = dict(trades)
    assert trades_
    assert isinstance(trades_, dict)
    assert 'TS' in trades_
    assert 'PRICE' in trades_
    assert isinstance(trades_.get('TS'), pd.Series)
    assert isinstance(trades_.get('PRICE'), pd.Series)

    candlesticks = bot_util.create_candlesticks(trades=trades, time_interval=bot_config.Ema.time_interval.value)
    candlesticks_ = dict(candlesticks)
    assert candlesticks_
    assert isinstance(candlesticks_, dict)
    assert ('PRICE', 'open') in candlesticks_
    assert ('PRICE', 'high') in candlesticks_
    assert ('PRICE', 'low') in candlesticks_
    assert ('PRICE', 'close') in candlesticks_
    assert isinstance(candlesticks_.get(('PRICE', 'open')), pd.Series)
    assert isinstance(candlesticks_.get(('PRICE', 'high')), pd.Series)
    assert isinstance(candlesticks_.get(('PRICE', 'low')), pd.Series)
    assert isinstance(candlesticks_.get(('PRICE', 'close')), pd.Series)

    ema = bot_util.calculate_ema(data=candlesticks['PRICE']['close'], length=bot_config.Ema.ema_length.value)
    ema_ = list(ema)
    assert ema_
    assert isinstance(ema_, list)
    for ema_value in ema_:
        assert ema_value
        assert isinstance(ema_value, float)

    bot_util.plt_(ema=ema, candlesticks=candlesticks, ema_length=bot_config.Ema.ema_length.value)
