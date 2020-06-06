import pandas as pd
import os.path
import os
from encode import Encode
import re
import numpy as np
from collections import Counter

root = "pollsdata"
final_df = None


def integrate_columns(data_frame):
    columns_dict = {
        "پدافند|ضد.*انفجار": 'ضد انفجار',
        "سرعت.*اجرا": 'سرعت اجرا',
        "دید": 'دید دیوار',
        "نیرو.*اجرایی": 'تعداد نیروی اجرایی',
        # "پدافند|ضد انفجار": 'one',
        # "سرعت اجرا": 'two',
        # "داشتن دید": 'three',
        # "نیرو[.]*اجرایی": 'four',
    }

    new_columns_name = list(data_frame.columns).copy()
    columns_name = list(data_frame.columns)

    for i, names in enumerate(new_columns_name):
        for pattern in columns_dict.keys():
            if re.search(pattern, names):
                new_columns_name[i] = columns_dict[pattern]

    data_frame = data_frame.rename(columns=dict(zip(columns_name, new_columns_name)))

    return data_frame


# import all surveys:
print(" \t importing data...")

for dir_name in os.listdir(root):

    polls = list()
    file_num = 0
    prime_idx = None

    address = root + '//' + dir_name
    for file_name in os.listdir(address):
        full_address = address + '\\' + file_name
        print(file_num, '\t', full_address)
        df = integrate_columns(pd.read_excel(full_address))
        polls.append(df)
        try:
            assert (polls[-1].shape == polls[0].shape)
        except AssertionError:
            raise ImportError(file_name + " doesn't fit")

        # find the index of the weighted poll:
        if re.search('parsa', file_name) is not None:
            prime_idx = file_num
        file_num += 1

    # make a new data frame:
    columns_name = polls[0].columns[1:]
    x_df = polls[0][columns_name]
    y = []  # store the final result. (type of the wall)

    # pick up surveys answers, split the columns y of the all polls to a new variable called ys:
    y_s = np.array([])
    for poll in polls:
        y_s = np.append(y_s, poll['نوع دیوار'].values.copy())

    n_rows = len(polls[0]['نوع دیوار'])
    y_s = np.reshape(y_s, newshape=[-1, n_rows]).T

    encode = Encode()
    encode.encode_walls_name(y_s)

    # # take the weighted poll out from y_s:
    # y_prime = y_s[:, 9]
    # y_s = np.hstack((y_s[:, :9], y_s[:, 10:]))

    # voting walls for the y columns:
    weight = 1  # [0, 1]

    # todo: outer loop:
    disagreements = 0

    for i in range(y_s.shape[0]):
        counted = dict(Counter(y_s[i, :]))
        top_vote = max(counted.items(), key=lambda x: x[1])
        prime_vote = y_s[i][prime_idx]  # careful: with changing this.

        if prime_vote != top_vote[0]:
            disagreements += 1
            # print(f'Prime vote is \033[1m{prime_vote}\033[0m, top answers is \033[1m{top_vote[0]}\033[0m'
            #       f' with \033[1m{top_vote[1]}\033[0m vote')

        threshold = len(y_s) - (weight * len(y_s))  # 0 means No One and 1 means anyone.
        if top_vote[1] > threshold:  # if the number of votes for a particular wall is more than a threshold:
            y.append(top_vote[0])
        else:
            y.append(prime_vote)

    print("\033[94m" + f"number of disagreements: {disagreements}" + "\033[0m")

    # import math
    df = pd.DataFrame(y, columns=['wall']).join(x_df)
    # df['wall'] = df['wall'].apply(lambda x: x if math.isnan(x) else int(x))

    if final_df is None:
        final_df = df.copy()
    else:
        final_df = pd.concat([final_df, df], ignore_index=True)

final_df.to_excel('new.xlsx')