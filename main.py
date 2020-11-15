# Isabella Gomez A15305555
# ECE143 HW7

from rational import Rational
from equal_sums import get_min_split
from pandas1 import split_count
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

    #print(get_min_split(arr))

    print(split_count(x))

    '''print(repr(r))
    print(-1/r)
    print(float(-1/r))
    print(int(r))
    print(int(Rational(10,3)))
    print(Rational(10,3) * Rational(101,8) - Rational(11,8))
    print(sorted([Rational(10,3), Rational(9,8), Rational(10,1), Rational(1,100)]))
    print(Rational(100,10))
    print(-Rational(12345,128191) + Rational(101,103) * 30/ 44)'''


