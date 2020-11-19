# Isabella Gomez A15305555
# ECE143 HW7

import pandas as pd
def count_month_yr(x):
    '''
    This function takes in a pd.dataframe from count_month and counts the unique values

    :param x: pd.dataframe of survey info
    :return: pd.dataframe with unique values and their corresponding repetition counts
    '''

    # check if x is a pd.dataframe
    assert isinstance(x, pd.DataFrame)

    date_df = x

    # copy dates into list
    time_list = date_df["month-yr"].tolist()
    time_set = set(time_list)
    non_rep_list = list(time_set)

    # get count of repeat words
    count = 0
    dict_repeat_times = {}
    for i in range(len(non_rep_list)):
        for k in range(len(time_list)):
            if non_rep_list[i] == time_list[k]:
                count = count + 1
        dict_repeat_times[non_rep_list[i]] = count
        count = 0

    # structure the dataframe
    final_df = pd.DataFrame(list(dict_repeat_times.items()), columns=['month-yr', 'Timestamp'])
    final_df = final_df.sort_values('month-yr')
    final_df.set_index('month-yr', inplace=True)  # temp is index

    return final_df

def add_month_yr(x):
    '''
    This function takes in a pd.series that is disorganized and separated and organizes
    the columns into a pd.dataframe

    :param x: pd.dataframe of survey info
    :return: pd. dataframe of the timestamps
    '''

    # check if x is a pd.dataframe
    assert isinstance(x, pd.DataFrame)

    # copy respective columns into dataframes
    df = x[['ID','Timestamp']]
    df.set_index('ID',inplace=True) # ID is index
    time_stamp = x[['Timestamp']]

    time_list = []
    for i in time_stamp.index:
        time_list.append(time_stamp.loc[i, 'Timestamp'])

    time_list = []
    month_abbrev = ['Jan-201','Feb-201','Mar-201','Apr-201','May-201','Jun-201','Jul-201','Aug-201','Sep-201',
                    'Oct-201','Nov-201','Dec-201']
    dates = []
    month = ''
    for i in time_stamp.index:
        time_list.append(time_stamp.loc[i,'Timestamp'])
        for j in range(len(time_list[i])):
            if time_list[i][j] == '/':
                break
            month = month + time_list[i][j]
        # find month abbreviations
        dates.append(month_abbrev[int(month)-1])
        month = ''

        # find year
        final_year = []
        for k in range(len(time_list)):
            for i in range(len(time_list[k])):
                if time_list[k][i] == ' ':
                    final_year.append(time_list[k][i-1])

    # append year to end of dates
    for y in range(len(final_year)):
        dates[y] = dates[y] + final_year[y]

    # Add new column
    df.insert(1,'new',dates, True)
    # delete old column
    del df['Timestamp']
    # rename column
    df = df.rename({'new': 'month-yr'}, axis=1)

    return df

