import csv
from APIgetData import getData
import collections


def CSV_file_getData(webURL, token):
    """

    :param webURL:
    :param token:
    :return:
    """
    # webAPI_data = dict()
    webAPI_data = getData(webURL, token)
    heading_1 = ['Dept', 'Category', 'QuestionID', 'ParentQuestionID',  # the category ID, I think????
                 'Question', 'Answer', 'ScoreActual', 'ScorePossible',
                 'Comment']

    key_list = list(webAPI_data.keys())
    all_list = list()
    for i in range(0, len(key_list)):
        all_list.append(webAPI_data[key_list[i]])

    newData_dict = dict()
    for dictionary in all_list:
        for key in dictionary:
            if not key in newData_dict:
                newData_dict.setdefault(key, list())
            newData_dict[key].append(dictionary[key])

    result = False
    # sort_data = collections.OrderedDict(sorted(newData_dict.items()))
    with open('Report_Output_Template.csv', 'w', newline='') as report_file:
        #for key in sort_data.items():
        for key in newData_dict:
            #for i in range(0, len(newData_dict[key])):
            for i in range(0, len(newData_dict[key])):
                cat_que_list = (newData_dict[key][i][2])
                for cat in cat_que_list:
                    dept = key
                    category = cat_que_list[cat][0]
                    questionID = cat_que_list[cat][2]
                    parentQuestionID = cat_que_list[cat][4]
                    questions = cat_que_list[cat][3]
                    ans_list = cat_que_list[cat][5]
                    makeCSV(dept, category, questionID, parentQuestionID, questions,
                            ans_list, heading_1, result, report_file)
                    result = True

    report_file.close()


def makeCSV(dept, category, questionID, parentQuestionID, questions, ans_list, heading_1, result, report_file):
    """

    :param dept:
    :param category:
    :param questionID:
    :param parentQuestionID:
    :param questions:
    :param ans_list:
    :param heading_1:
    :param result:
    :param report_file:
    :return:
    """
    csvwriter = csv.writer(report_file)
    if not result:
        csvwriter.writerow(heading_1)

    # parentQuestionID, questionID, ans_list and questions
    # have the same number of elements in them

    for i in range(0, len(parentQuestionID)):
        write = list()
        ans_dict = ans_list[i]
        answer = ans_dict['answer']
        scoreActual = ans_dict['value']
        scorePossible = ans_dict['max_value']
        comment = ans_dict['details']
        write.append(dept)                  # A
        write.append(category)              # B
        write.append(questionID[i])         # C
        write.append(parentQuestionID[i])   # D
        write.append(questions[i])          # E
        write.append(answer)                # G
        write.append(scoreActual)           # G
        write.append(scorePossible)         # H
        write.append(comment)               # I

        csvwriter.writerow(write)

    var = 1


CSV_file_getData("https://demo.isora.saltycloud.com/", "c548a5524615454ac53281ac01efd56bbf69f4d9")

#
# def file1(report_file):
#     csvwriter = csv.writer(report_file)
#     heading_1 = ['Question', 'Answer', 'ScoreActual', 'ScorePossible','Comment']
#     csvwriter.writerow(heading_1)
#
#
# def file2(report_file):
#     csvwriter = csv.writer(report_file)
#     heading_1 = ['Dept', 'Category', 'QuestionID', 'ParentQuestionID',  # the category ID, I think????
#                  'Question', 'Answer', 'ScoreActual', 'ScorePossible',
#                  'Comment']
#     csvwriter.writerow(heading_1)
#
#
# with open('Report_Output_Template.csv', 'w', newline='') as report_file:
#     file1(report_file)
#     file2(report_file)
#     report_file.close()
