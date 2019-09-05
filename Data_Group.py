import pickle
import time
import datetime
import pybithumb

with open("Key_Value.pickle","rb") as fr:
    Key_Value = pickle.load(fr)
bithumb = pybithumb.Bithumb(Key_Value[0], Key_Value[1])

List_tickers = pybithumb.get_tickers()

now = datetime.datetime.now()
Q1 = datetime.datetime(now.year, now.month, now.day)
Q2 = Q1 + datetime.timedelta(hours = 6)
Q3 = Q2 + datetime.timedelta(hours = 6)
Q4 = Q3 + datetime.timedelta(hours = 6)
Q5 = Q4 + datetime.timedelta(hours = 6)


