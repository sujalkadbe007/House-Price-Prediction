import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sk.learn.mrtrics import mean_squared_error

df = pd.read_csv("house_prices.csv")
