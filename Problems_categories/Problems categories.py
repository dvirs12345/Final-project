# Author - Dvir Sadon
import pandas as pd
import xlrd
from colormap import rgb2hex

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""CLASSSIFY"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def classify(problems_categories, list_10000):
    for index, row in list_10000.iterrows():
        color = find_color(problems_categories, list_10000['ProblemText'][index])

        try:
            list_10000['Problem category (MEDICAL / SURGICAL / TRAUMA / TRANSPLANTATION / OBSTETRICS)'][index] = color[
                color.keys()[0]]
        except IndexError:  # Did not find in
            if row['ProblemText'] == 'fracture of':
                list_10000['Problem category (MEDICAL / SURGICAL / TRAUMA / TRANSPLANTATION / OBSTETRICS)'][
                    index] = "#FF0000"
            else:
                list_10000['Problem category (MEDICAL / SURGICAL / TRAUMA / TRANSPLANTATION / OBSTETRICS)'][
                    index] = "#FFFFFF"

    list_10000 = list_10000[list_10000['Problem category (MEDICAL / SURGICAL / TRAUMA / TRANSPLANTATION / OBSTETRICS)']
                            != "#FFFFFF"]

    return list_10000


def find_color(problems_categories, ProblemText):
    return problems_categories.loc[problems_categories['ProblemText'].str.lower() == ProblemText.lower(), 'Color']


def replace_with_category(list_10000):
    list_10000['Problem category (MEDICAL / SURGICAL / TRAUMA / TRANSPLANTATION / OBSTETRICS)'].replace(
        ['#FFFF00'], 'MEDICAL', inplace=True)

    list_10000['Problem category (MEDICAL / SURGICAL / TRAUMA / TRANSPLANTATION / OBSTETRICS)'].replace(
        ['#99CC00'], 'SURGICAL', inplace=True)

    list_10000['Problem category (MEDICAL / SURGICAL / TRAUMA / TRANSPLANTATION / OBSTETRICS)'].replace(
        ['#00CCFF'], 'OBSTETRICS', inplace=True)

    list_10000['Problem category (MEDICAL / SURGICAL / TRAUMA / TRANSPLANTATION / OBSTETRICS)'].replace(
        ['#FFCC00'], 'TRANSPLANTATION', inplace=True)

    list_10000['Problem category (MEDICAL / SURGICAL / TRAUMA / TRANSPLANTATION / OBSTETRICS)'].replace(
        ['#FF0000'], 'TRAUMA', inplace=True)

    list_10000['Problem category (MEDICAL / SURGICAL / TRAUMA / TRANSPLANTATION / OBSTETRICS)'].replace(
        ['#FFFFFF'], 'NOT FOUND', inplace=True)


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""MAKE DATA FUNCTIONS"""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def make_data(book, sheet):
    problems_categories = handle_colors(book, sheet)
    list_10000 = clean_list_10000()
    return problems_categories, list_10000


def handle_colors(book, sheet):
    problems_categories = pd.read_excel('problems categories.xlsx', sheet_name='problem categories')
    problems_categories.drop(problems_categories.columns[[2, 3, 4]], axis=1, inplace=True)
    problems_categories.columns = ['ProblemText', 'Color']

    surg = ['s/p THR', 's/p TKR', 's/p mitral valve repair', 'peripheral vascular disease']
    med = ['pulmonary hypertension - severe', 'multibrain infarction', 'gastropathy', 'hypertensive emergency']
    for i in range(0, sheet.nrows - 1):
        color = getBGColor(book, sheet, i + 1, 0)
        if color is None:
            if problems_categories.loc[i, 'ProblemText'] in surg:
                problems_categories.loc[i, 'Color'] = '#99CC00'
            elif problems_categories.loc[i, 'ProblemText'] in med:
                problems_categories.loc[i, 'Color'] = '#FFFF00'

            problems_categories.loc[i, 'Color'] = "#FFFFFF"  # White
        else:
            problems_categories.loc[i, 'Color'] = rgb2hex(color[0], color[1], color[2])

    problems_categories = problems_categories[problems_categories['ProblemText'].notna()]

    return problems_categories


def clean_list_10000():
    list_10000 = pd.read_excel('problems categories_new_09.1.xlsx', sheet_name='Sheet1')
    list_10000 = list_10000[list_10000['ProblemText'].notna()]
    list_10000 = list_10000[list_10000['ProblemText'] != "ד"]

    return list_10000


def getBGColor(book, sheet, row, col):
    xfx = sheet.cell_xf_index(row, col)
    xf = book.xf_list[xfx]
    bgx = xf.background.pattern_colour_index
    pattern_colour = book.colour_map[bgx]
    return pattern_colour


def main():
    """ Code for xls """
    excel = xlrd.open_workbook('problems categories.xls', formatting_info=True)
    problems_categories = excel.sheet_by_name("problem categories")
    problems_categories, list_10000 = make_data(excel, problems_categories)
    classified = classify(problems_categories, list_10000)
    replace_with_category(classified)
    print(classified.head())
    print(classified['Problem category (MEDICAL / SURGICAL / TRAUMA / TRANSPLANTATION / OBSTETRICS)'].unique())
    classified.to_excel(r'Problems Categories Classified.xlsx', index=False)

    """ Code for xlsx """
    # excel = openpyxl.load_workbook('problems categories.xlsx', data_only=True)
    # list_10000 = excel["list_10000"]
    # problems_categories = excel["problem categories"]
    # color_in_hex = problems_categories['A35'].fill.start_color.index
    # print(color_in_hex)
    # rgb = tuple(int(color_in_hex[i:i + 2], 16) for i in (0, 2, 4))
    # print(rgb)

    """"""


main()
