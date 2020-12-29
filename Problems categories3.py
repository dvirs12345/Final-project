# Author - Dvir Sadon
import matplotlib.pyplot as plt
import pandas as pd


def display_uniques(df):
    counts1, counts2 = count_unique_categories(df)
    counts1_names = ['MEDICAL1', 'SURGICAL1', 'TRAUMA1', 'TRANSPLANTATION1', 'OBSTETRICS1']
    counts2_names = ['MEDICAL2', 'SURGICAL2', 'TRAUMA2', 'TRANSPLANTATION2', 'OBSTETRICS2']
    counts1.index = counts1_names
    counts2.index = counts2_names
    countsall = pd.concat([counts1, counts2], axis=1)
    countsall.plot(kind='pie', subplots=True, ylabel="# Of Occurrences", xlabel="Type", title="Number of Occurrences "
                                                                                              "for every category "
                                                                                              "and ProblemGroup",
                   legend=False)
    plt.show()


def count_unique_categories(df):
    dfgrouped = df.groupby(['ProblemGroup'])
    group1 = dfgrouped.get_group(1)
    counts1 = group1['Problem category (MEDICAL / SURGICAL / TRAUMA / TRANSPLANTATION / OBSTETRICS)'].value_counts()
    group2 = dfgrouped.get_group(2)
    counts2 = group2['Problem category (MEDICAL / SURGICAL / TRAUMA / TRANSPLANTATION / OBSTETRICS)'].value_counts()

    print("For ProblemGroup 1:")
    print(counts1)
    print("\nFor ProblemGroup 2:")
    print(counts2)
    return counts1, counts2


def main():
    pd.set_option('display.max_columns', 11)
    excel = pd.read_excel('Problems Categories Classified.xlsx', sheet_name='Sheet1')

    display_uniques(excel)


main()
