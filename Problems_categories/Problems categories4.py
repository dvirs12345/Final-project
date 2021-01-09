# Author - Dvir Sadon
import matplotlib.pyplot as plt
import pandas as pd


def fill2(row):
    string2 = ''
    if isinstance(row['MEDICAL 2'], str):
        string2 += 'M'
    if isinstance(row['SURGICAL 2'], str):
        string2 += 'S'
    if isinstance(row['TRAUMA 2'], str):
        string2 += 'TA'
    if isinstance(row['TRANSPLANTATION 2'], str):
        string2 += 'TN'
    if isinstance(row['OBSTETRICS 2'], str):
        string2 += 'O'
    return string2


def fill1(row):
    """Gets row and makes the String to put in the 1 column cell in the respective row"""
    string1 = ''
    if isinstance(row['MEDICAL 1'], str):
        string1 += 'M'
    if isinstance(row['SURGICAL 1'], str):
        string1 += 'S'
    if isinstance(row['TRAUMA 1'], str):
        string1 += 'TA'
    if isinstance(row['TRANSPLANTATION 1'], str):
        string1 += 'TN'
    if isinstance(row['OBSTETRICS 1'], str):
        string1 += 'O'

    return string1


def make_df(prev_df):
    df = pd.DataFrame(None, columns=['Id', '1', '2'])

    df['Id'] = prev_df['Id']

    for index, row in prev_df.iterrows():
        string1 = fill1(row)
        string2 = fill2(row)
        df.loc[df['Id'] == row['Id'], '1'] = string1
        df.loc[df['Id'] == row['Id'], '2'] = string2

    return df


def main():
    excel = pd.read_excel('Classified 2.xlsx', sheet_name='Sheet1')
    df = make_df(excel)
    df.to_excel(r'Classified 3.xlsx', index=False)


main()
