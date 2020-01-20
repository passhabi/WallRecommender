import numpy as np
#gui import mathplotlib.pyplot as plt
import pandas as pd
from sklearn import tree
from encode import Encode
import tkinter as tk

df = pd.read_excel("dataset_50.xlsx")

encode = Encode()
df = df.apply(encode.encode_words)

# split data: # todo: train and test set.
x = df.iloc[:, :-1].values
y = df.iloc[:, -1].values


# todo: run model in a loop for optimization.
clf = tree.DecisionTreeClassifier()
model = clf.fit(x, y)
y_hat = model.predict(x)

# give me data to test:
a = x[5]

model.predict(a)