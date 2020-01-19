import np as np
# import mathplotlib.pyplot as plt
import pandas as pd
from sklearn import tree
import tkinter as tk

df = pd.read_excel("dataset_50.xlsx")

# change categorical data in dataset to numbers:
# accessibility:
df.replace(to_replace='difficult', value=1, inplace=True)
df.replace(to_replace='easy', value=0, inplace=True)

# defensive, num_forces:
df.replace(to_replace='much', value=2, inplace=True)
df.replace(to_replace='avg', value=1, inplace=True)
df.replace(to_replace='few', value=0, inplace=True)

# visibility:
df.replace(to_replace='n', value=0, inplace=True)
df.replace(to_replace='y', value=1, inplace=True)

# water_level, importance::
df.replace(to_replace='high', value=1, inplace=True)
df.replace(to_replace='low', value=0, inplace=True)

# soil_type:
df.replace(to_replace='weak', value=1, inplace=True)
df.replace(to_replace='strong', value=0, inplace=True)

# topography:
df.replace(to_replace='plain', value=0, inplace=True)
df.replace(to_replace='mountain', value=1, inplace=True)
df.replace(to_replace='hill', value=2, inplace=True)

# speed:
df.replace(to_replace='short', value=1, inplace=True)
df.replace(to_replace='long', value=0, inplace=True)


# split data: # todo: train and test set.
x = df.iloc[:, :-1].values
y = df.iloc[:, -1].values


# todo: run model in a loop for optimization.
clf = tree.DecisionTreeClassifier()
model = clf.fit(x, y)
y_hat = model.predict(x)

# give me data to test:
