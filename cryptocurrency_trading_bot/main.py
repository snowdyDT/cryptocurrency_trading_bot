from cryptocurrency_trading_bot import config as bot_config
from cryptocurrency_trading_bot import util as bot_util


def main():
    # Read trades
    trades = bot_util.read_trades(file_path=bot_config.prices_file_path)

    # Create candlesticks
    candlesticks = bot_util.create_candlesticks(trades=trades, time_interval=bot_config.Ema.time_interval.value)

    # Calculate EMA
    ema = bot_util.calculate_ema(data=candlesticks['PRICE']['close'], length=bot_config.Ema.ema_length.value)

    # plt.show()
    bot_util.plt_(ema=ema, candlesticks=candlesticks, ema_length=bot_config.Ema.ema_length.value)


if __name__ == '__main__':
    main()
