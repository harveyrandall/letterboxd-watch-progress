import numpy as np 
import pandas as pd 
import letterboxd
import datetime

def save_diary(entries, columns, path):
    df = pd.DataFrame(np.array(entries), columns=columns)
    df.sort_values(by=['date'], inplace=True)
    df.reset_index(inplace=True, drop=True)
    with open(path, 'w') as f:
        df.to_csv(f)

def load_diary(path):
    df = pd.read_csv(path, header=0)
    return df