# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 21:00:17 2020

@author: 91852
"""

# Histograms
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

n_arr=np.random.normal(100,20, 1000)
n_arr

plt.hist(n_arr, bins=[80,85,90,95,100,105,110,115,120])
plt.title("histogram")
plt.show();

l1 = list(range(50,150))
plt.hist(n_arr, bins=l1)
plt.title("histogram")
plt.show()

#Pandas Library (very very important for data analytics)
import pandas as pd

import pydataset

pydataset.data('')

from pydataset import data
mtcars = data('mtcars')
mtcars

#by default it will first 5 rows and all the columns
mtcars.head()

mtcars.head(10)

mtcars.to_csv("C:\Analytics\Projects\\mt.csv")

import pandas as pd

df = pd.read_csv("mt.csv")
df.head(2)
df.shape

s = pd.Series(range(10))
s

m= pd.Series(range(1001, 1010))
m

m1= pd.Series(range(10001,10033))
m1

m3 = df.set_index(m1)
m3

m = pd.Series(range(10001, 10001 + df.shape[0]))
m

ps2 = pd.Series([1,32,43,21,55], index=["a","b","c","d","e"])
ps2

ps2["c"]
ps2["b":"d"]

dic = {"a":1, "b":2, "c":3}
ps3 = pd.Series(dic)
ps3

ps3.iloc[1:3]
ps3.iloc[0]
ps3.iloc[1]
ps3.iloc[2]
ps3.iloc[3]
