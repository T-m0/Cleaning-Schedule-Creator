import numpy as np
import pandas as pd
from datetime import date, timedelta
from itertools import cycle, islice


#Change these four variables for your own cleaning schedule.
chores = ['Chore 1', 'Chore 2', 'Chore 3', 'Chore 4', 'Chore 5']
names = ['Name 1', 'Name 2', 'Name 3', 'Name 4']
max_width = 8
schedule_length = 9


def make_dates():
    """
    The next_monday line can be changed: change '0' to change the day
    (tuesday=1, wednesday=2, ...) Warning: if today is monday, then next_monday
    becomes today instead of next week. Returns index and path.
    """
    next_monday = date.today() + timedelta(days=(0 - date.today().weekday()) % 7)
    index = [(next_monday + timedelta(weeks=i)).strftime("%d/%b") for i in range(schedule_length)]
    path = f'cleaning_schedule {next_monday.strftime("%Y-%m-%d")}.xlsx'
    return index, path
            
def make_table(make_dates, chores):
    """
    This function creates a fair cleaning schedule based on the chores, names
    and maximum schedule width (max_width). Filling in the names is randomized,
    to a certain extent. If chores and names are of equal length, then randomly
    placing the names in each week can lead to one person doing a certain task
    multiple weeks in a row, which would not be fair. Therefore, this function
    seeks to cycle through the list of names instead, if possible. If not
    possible, then a (fair) random fill will be performed. Returns df. 
    """
    index=make_dates()[0]
    if len(chores) > max_width:
        pass
    elif max_width >= len(chores) == len(names):
        df = pd.DataFrame(columns=chores, index=index)
        df.iloc[0] = np.random.permutation(names)
        for i in range(1, len(index)):
            df.iloc[i] = list(islice(cycle(df.iloc[0]), i, i+len(names), 1))
            #This cycles through the list of names so that next week everyone has a different chore
        return df
    elif max_width >= len(chores) > len(names):
        df = pd.DataFrame(columns=chores, index=index)
        for i in range(len(index)):
            new_names = names.copy() * (len(chores) // len(names))
            #If there are 10 chores and 3 names, for example, this makes 3 copies of names
            for name in np.random.choice(names, size=(len(chores) % len(names))):
                #If 10 chores and 3 names, then only name is randomly picked
                new_names.append(name)
            df.iloc[i] = np.random.permutation(new_names)
        return df
    elif max_width >= len(names) > len(chores):
        chores += ['Free'] * (len(names) - len(chores)) #Now, len(names) == len(chores)
        df = pd.DataFrame(columns=chores, index=index)
        df.iloc[0] = np.random.permutation(names)
        for i in range(1, len(index)):
            df.iloc[i] = list(islice(cycle(df.iloc[0]), i, i+len(names), 1)) #same cycle
        return df
    elif len(names) >= max_width > len(chores):
        df = pd.DataFrame(columns=chores, index=index)
        for i in range(len(index)):
            df.iloc[i] = np.random.choice(names, size=len(chores), replace=False)
        return df

def write_to_excel(make_dates, make_table):
    """
    This function prints the dataframe to an Excel file. If there is no df
    (which is the case if there are more chores than max_width) then a message
    is printed instead.
    """
    path = make_dates()[1]
    try:
        df = make_table(make_dates, chores)
        writer = pd.ExcelWriter(path)
        df.to_excel(writer)
        writer.save()
        print("Your Excel File has been made.")
    except AttributeError:
        print('You have more chores than fit in the table. Either increse max_width or drop chores.')


if __name__ == '__main__':
    write_to_excel(make_dates, make_table)
