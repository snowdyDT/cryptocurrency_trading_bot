from cryptocurrency_trading_bot import config as bot_config
from cryptocurrency_trading_bot import util as bot_util


def main():
    trades = bot_util.Trades()
    candlesticks = bot_util.Candlesticks()
    ema = bot_util.Ema()
    visualization = bot_util.Visualization()

    # Read trades
    trades_ = trades.read()

    # Create candlesticks
    candlesticks.trades = trades_
    candlesticks_ = candlesticks.create()

    # Calculate EMA
    ema.data = candlesticks_['PRICE']['close']
    ema_ = ema.calculate()

    # plt.show()
    visualization.ema = ema_
    visualization.candlesticks = candlesticks_
    visualization.show()


if __name__ == '__main__':
    main()
