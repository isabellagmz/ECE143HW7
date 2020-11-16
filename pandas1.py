# Isabella Gomez A15305555
# ECE143 HW7

import pandas as pd
def split_count(x):
    '''
    This function takes in a pd.series that is disorganized and separated and organizes
    the columns into a pd.dataframe

    :param x: pd.series that contains information
    :return: pd.dataframe organized from series
    '''

    # check if x is a pd.series
    assert isinstance(x, pd.Series)

    # run through and find all unique values
    temp = []
    for i in range(len(x)):
        temp.append(x[i])
    all_values = [element for item in temp for element in item.split(',')]
    # removing whitespace from list
    for i in range(len(all_values)):
        all_values[i] = all_values[i].strip()

    # make a unique list of values
    unique_set = set(all_values)
    unique_list = list(unique_set)

    # check if the elements are the same and store their respective counts in dict
    val_and_index = {}
    try1 = []
    count = 0 # temp count
    for i in range(len(unique_list)):
        for j in range(len(all_values)):
            if all_values[j] == unique_list[i]:
                count = count + 1
        val_and_index[unique_list[i]] = count
        count = 0

    # structure the dataframe
    df = pd.DataFrame(list(val_and_index.items()), columns=['temp', 'count'])
    df = df.sort_values('count')

    # hard coding order
    df = df.reset_index()
    del df['index']

    df.loc[0, 'temp'] = 'All of the above'
    df.loc[1, 'temp'] = 'Computer vision'
    df.loc[2, 'temp'] = 'Image Processing'
    df.loc[3, 'temp'] = 'Computer vision/image processing'
    df.loc[4, 'temp'] = 'As a general skill'
    df.loc[5, 'temp'] = 'scripting seems desirable for many jobs'
    df.loc[6, 'temp'] = 'not sure'
    df.loc[7, 'temp'] = 'Computer Vision'
    df.loc[8, 'temp'] = 'EDA tools'

    return df
