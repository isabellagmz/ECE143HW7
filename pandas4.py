# Isabella Gomez A15305555
# ECE143 HW7

import pandas as pd
from datetime import datetime
def fix_categorical(x):
    '''
    This function takes in a pd.dataframe from count_month and counts the unique values

    :param x: pd.dataframe of survey info
    :return: pd.dataframe with unique values and their corresponding repetition counts
    '''

    # check if x is a pd.dataframe
    assert isinstance(x, pd.DataFrame)

    # put index values into a list
    index_values = list(x.index.values)
    content = x["Timestamp"].to_list()

    # make dictionary with dates and values
    data_dict = {}
    for date in range(len(index_values)):
        data_dict[index_values[date]] = content[date]
    # convert to datetime object and store in dict
    index_values.sort(key=lambda date: datetime.strptime(date, "%b-%Y"))

    # make it categorical
    cat = pd.Series(index_values, dtype="category")

    # make a content list
    content = [] # empty content
    for oredered_key in range(len(index_values)):
        for key in data_dict.keys():
            if(key == index_values[oredered_key]):
                content.append(data_dict[key])

    # add cat back to dataframe
    final_df = pd.DataFrame({'month-yr':cat, 'Timestamp':content})

    # delete index
    final_df.set_index('month-yr', inplace=True)  # temp is index

    #print(final_df.groupby('month-yr')['Timestamp'].count().to_frame().sort_index())

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
