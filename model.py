import pandas as pd
from sklearn import tree
from encode import Encode

df = pd.read_excel("dataset.xlsx")

# delete number rows column:
columns_names = df.keys()[:-1]  # the unwanted column is not included in the list.
df = df[columns_names]

encode = Encode()
df = df.apply(encode.translate_list)  # translate to english.
df = df.apply(encode.encode_words)  # encoded to numbers.

df = df.dropna()

# split data: # todo: train and test set.
x = df.iloc[:, 1:].values
y = df.iloc[:, 0].values


# todo: run model in a loop for optimization.
clf = tree.DecisionTreeClassifier()
fitted_model = clf.fit(x, y)
y_hat = fitted_model.predict(x)
