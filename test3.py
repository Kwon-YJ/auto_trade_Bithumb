import pybithumb


a = pybithumb.get_ohlcv("BTC")

print(a.tail(10))