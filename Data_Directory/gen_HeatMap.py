import matplotlib.pyplot as plt
from pandas import DataFrame
import seaborn as sns
from Data_Directory.APIgetData import *


def category_HeatMap(names, avg):
    """
    Function is responsible for creating Category wise Heat Maps, with respect to the Org Unit Questions.
    :param names: A list of Names of Org Unit Questions
    :param avg: A list of Averages of each Org Unit Question
    :return: None
    """

    heatDict = dict()
    index = list()
    for i in range(0, len(names)):
        heatDict[names[i]] = avg[i]
        index.append(i)

    plt.title("Categorical Heat Map")
    sns.set(font_scale=0.7)
    h_map = DataFrame(data=avg, index=names)
    sns.heatmap(
        h_map,
        cbar_kws={"orientation": "vertical"},
        annot=True,
        annot_kws={"size": 10},  # font size in each cell
        linewidths=1,
        square=True,
        vmax=1,
        vmin=0,
        yticklabels=True,
        xticklabels=False,
        cmap='YlGnBu',
        linecolor='white',
        cbar=True,
        fmt='g',
    )
    plt.xlabel('Average')
    plt.ylabel('Categories')
    print(h_map)
    plt.show()


def subCategory_HeatMap(name, questions, answers):
    """
    Function is responsible for creating Sub Category wise Heat Maps, with respect to the Org Unit Question's category.
    :param name: The title of the Heat Map
    :param questions: A list of Questions regarding the specific categorical name
    :param answers: A list of dictionaries with Answers regarding the specific categorical name
    :return: None
    """

    plt.title(name)
    maximum = 0
    data = list()
    for each in answers:
        data.append(each['answer'])
        if maximum < each['max_value']:
            maximum = each['max_value']

    h_map = DataFrame(data=data, index=questions)
    sns.set(font_scale=0.6)
    sns.heatmap(
        h_map,
        cbar_kws={"orientation": "vertical"},
        annot=True,
        annot_kws={"size": 10},  # font size in each cell
        linewidths=1,
        square=True,
        vmax=maximum,
        vmin=0,
        yticklabels=True,
        xticklabels=False,
        cmap='YlGnBu',
        linecolor='white',
        cbar=True,
        fmt='g',
    )
    plt.xlabel('Value')
    plt.ylabel('Questions')
    print(h_map)
    plt.show()


def common_report_HeatMap(main_dict, assessment_name):
    """
    Function that creates the common Report Heat Map
    :param assessment_name: The title of the Heat Map
    :param main_dict: Dictionary
            :key: org_unit_name
            :value: Nested list
                    Each cell holds a list that contains individual specific data to create a category based Heat Map
    :return: None
    """
    columns = list(main_dict.keys())
    index = main_dict[columns[0]][0]
    # index = ['1','2','3','4','5','6']
    data = list()
    maximum = 0
    for i in range(0, len(columns)):
        to_check = main_dict[columns[i]][1]
        inner_data = list()
        for j in range(0, len(to_check)):
            inner_data.append(to_check[j])
            if maximum < to_check[j]:
                maximum = to_check[j]
        data.append(inner_data)
    plt.title(assessment_name)
    h_map = DataFrame(data=data, index=columns, columns=index)
    sns.set(font_scale=0.6)

    sns.heatmap(
        h_map,
        cbar_kws={"orientation": "vertical"},
        annot=True,
        annot_kws={"size": 10},  # font size in each cell
        linewidths=1,
        square=True,
        vmax=maximum,
        vmin=0,
        yticklabels=True,
        xticklabels=True,
        cmap='YlGnBu',
        linecolor='white',
        cbar=True,
        fmt='g',
    )
    plt.xlabel("Questions")
    plt.ylabel("Org_unit_Questions")
    print(h_map)

    plt.show()


if __name__ == '__main__':
    survey_id = getSurvey_ID("GLBA", "SaltyU SFA FY'18 - spring", "Infrastructure & Students",
                             "c548a5524615454ac53281ac01efd56bbf69f4d9")
    heatMap_data = heat_map_data("https://demo.isora.saltycloud.com/", survey_id,
                                 "c548a5524615454ac53281ac01efd56bbf69f4d9")

    t_names = heatMap_data[0]
    names = list()
    category_id = list()
    for i in t_names:
        names.append(i[0])
        category_id.append((i[1]))
    avg = heatMap_data[1]
    questions = heatMap_data[2]
    answers = heatMap_data[3]

    dictionary = commonReport_data("SaltyU SFA FY'18 - spring",
                                   common_heat_map_data(getData("https://demo.isora.saltycloud.com/",
                                                                "c548a5524615454ac53281ac01efd56bbf69f4d9")),
                                   "c548a5524615454ac53281ac01efd56bbf69f4d9", "https://demo.isora.saltycloud.com/")
    common_report_HeatMap(dictionary, "SaltyU SFA FY'18 - spring")
    common_report_HeatMap("CIS Controls - BASIC", getData("https://demo.isora.saltycloud.com/",
                                                          "c548a5524615454ac53281ac01efd56bbf69f4d9"))
    subCategory_HeatMap('GLBA-1: Develop, implement, and maintain a written information security program; ',
                        ['Does the written information security program include requirements for creating and '
                         'retaining system audit logs and records?',
                    'Has a written information security program been developed and implemented?'],
                        [{'answer': -2.0, 'details': '', 'value': 0.0, 'max_value': 7.5, 'favorability': 'unfavorable'},
                          {'answer': 0.5, 'details': 'in final draft', 'value': 3.75, 'max_value': 7.5,
                           'favorability': 'partial-50'}])
    # subCategory_HeatMap(names[val], questions[category_id[val]], answers[category_id[val]])
    category_HeatMap(names, avg)

    # plt.show()
