# Author - Dvir Sadon
import pandas as pd
import numpy as np


def conectate_problems(problems):
    """Strings all the problems divided by ',' """
    problems = problems['ProblemText']
    toreturn = ''
    for i in problems:
        toreturn += ',' + str(i)
    return toreturn


def conectate_by_group(grouped_id, id1, df):
    """Iterates over group (1 patient) and creates array to insert into df and returns it"""
    my_group = grouped_id.get_group(id1)

    Medical1 = my_group.loc[(my_group['ProblemGroup'] == 1) &
                            (my_group[
                                 'Problem category (MEDICAL / SURGICAL / TRAUMA / TRANSPLANTATION / OBSTETRICS)'] == "MEDICAL")]
    Medical2 = my_group.loc[(my_group['ProblemGroup'] == 2) &
                            (my_group[
                                 'Problem category (MEDICAL / SURGICAL / TRAUMA / TRANSPLANTATION / OBSTETRICS)'] == "MEDICAL")]
    Surgical1 = my_group.loc[(my_group['ProblemGroup'] == 1) &
                             (my_group[
                                  'Problem category (MEDICAL / SURGICAL / TRAUMA / TRANSPLANTATION / OBSTETRICS)'] == "SURGICAL")]
    Surgical2 = my_group.loc[(my_group['ProblemGroup'] == 2) &
                             (my_group[
                                  'Problem category (MEDICAL / SURGICAL / TRAUMA / TRANSPLANTATION / OBSTETRICS)'] == "SURGICAL")]
    Trauma1 = my_group.loc[(my_group['ProblemGroup'] == 1) &
                           (my_group[
                                'Problem category (MEDICAL / SURGICAL / TRAUMA / TRANSPLANTATION / OBSTETRICS)'] == "TRAUMA")]
    Trauma2 = my_group.loc[(my_group['ProblemGroup'] == 2) &
                           (my_group[
                                'Problem category (MEDICAL / SURGICAL / TRAUMA / TRANSPLANTATION / OBSTETRICS)'] == "TRAUMA")]
    Transplantation1 = my_group.loc[(my_group['ProblemGroup'] == 1) &
                                    (my_group[
                                         'Problem category (MEDICAL / SURGICAL / TRAUMA / TRANSPLANTATION / OBSTETRICS)'] == "TRANSPLANTATION")]
    Transplantation2 = my_group.loc[(my_group['ProblemGroup'] == 2) &
                                    (my_group[
                                         'Problem category (MEDICAL / SURGICAL / TRAUMA / TRANSPLANTATION / OBSTETRICS)'] == "TRANSPLANTATION")]
    Obstetrics1 = my_group.loc[(my_group['ProblemGroup'] == 1) &
                               (my_group[
                                    'Problem category (MEDICAL / SURGICAL / TRAUMA / TRANSPLANTATION / OBSTETRICS)'] == "OBSTETRICS")]
    Obstetrics2 = my_group.loc[(my_group['ProblemGroup'] == 2) &
                               (my_group[
                                    'Problem category (MEDICAL / SURGICAL / TRAUMA / TRANSPLANTATION / OBSTETRICS)'] == "OBSTETRICS")]

    return np.array([id1, conectate_problems(Medical1), conectate_problems(Surgical1), conectate_problems(Trauma1),
                     conectate_problems(Transplantation1), conectate_problems(Obstetrics1), conectate_problems(Medical2)
                     , conectate_problems(Surgical2), conectate_problems(Trauma2),
                     conectate_problems(Transplantation2), conectate_problems(Obstetrics2)])


def make_dataframe(problems_categories_classified):
    df = pd.DataFrame(None, columns=['Id', 'MEDICAL 1', 'SURGICAL 1', 'TRAUMA 1', 'TRANSPLANTATION 1', 'OBSTETRICS 1',
                                     'MEDICAL 2', 'SURGICAL 2', 'TRAUMA 2', 'TRANSPLANTATION 2', 'OBSTETRICS 2'])

    id_groups = problems_categories_classified.groupby(['id_demo'])
    df['Id'] = problems_categories_classified['id_demo'].unique()

    for i in df['Id']:
        df.iloc[(df[df['Id'] == i]).index[0]] = conectate_by_group(id_groups, i, df)

    return df


def main():
    pd.set_option('display.max_columns', 11)
    excel = pd.read_excel('Problems Categories Classified.xlsx', sheet_name='Sheet1')

    df = make_dataframe(excel)
    df.to_excel(r'Classified 2.xlsx', index=False)


main()
