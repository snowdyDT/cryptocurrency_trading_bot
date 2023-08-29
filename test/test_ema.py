import pandas as pd
import matplotlib.pyplot as plt


def test_ewm_method(capsys):
    stock_values = pd.DataFrame(
        {'Stock_Values': [60, 102, 103, 104, 101,
                          105, 102, 103, 103, 102]})

    ema = stock_values.ewm(com=0.4).mean()

    plt.plot(stock_values, label="Stock Values")
    plt.plot(ema, label="EMA Values")
    plt.xlabel("Days")
    plt.ylabel("Price")
    plt.legend()
    plt.show()
