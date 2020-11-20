# Isabella Gomez A15305555
# ECE143 HW7

from rational import Rational
from equal_sums import get_min_split
from pandas1 import split_count
from pandas2 import add_month_yr
from pandas3 import count_month_yr
from pandas4 import fix_categorical

import numpy as np
import pandas as pd
class Homework7:
    def __init__(self):
        pass

if __name__ == '__main__':
    my_Homework7 = Homework7()
    r = Rational(3,4)

    # import data into pandas
    fname = '/Users/isabellagomez/Documents/ECE143/survey_data.csv'
    df = pd.read_csv(fname)
    x = df.iloc[:,8] # take column of 'is there anything...'

    sequence = [5, 10, 15, 20, 25]
    arr = np.array(sequence)

    #print(add_month_yr(df))
    #print(count_month_yr(df))
    #print(count_month_yr(add_month_yr(df)))
    #print(fix_categorical(count_month_yr(add_month_yr(df))))
    y = fix_categorical(add_month_yr(df))
    #y.info()
    #print(y)

    print(y.groupby('month-yr')['Timestamp'].count().to_frame().sort_index())

    #print(get_min_split(arr))

    #print(split_count(x))

