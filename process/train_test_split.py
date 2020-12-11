import pandas as pd
import numpy as np

def trainTestSplit(data, ratio = 0.8):
    if isinstance(data, pd.DataFrame):
        train_pct_index =  int(ratio * len(data))
        train = data.iloc[:train_pct_index,:]
        test = data.iloc[train_pct_index:,:]
        return train, test
    elif isinstance(data,np.array):
        X_train, X_test = data[:train_pct_index,0], data[train_pct_index:,0]
        Y_train, Y_test = data[:train_pct_index,1:], data[train_pct_index:,1:]
        return X_train, X_test, Y_train, Y_test
