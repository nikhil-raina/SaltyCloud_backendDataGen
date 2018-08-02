import csv
from APIgetData import getData


def CSV_file_getData(webURL, token):
    """
    Function responsible to get the API report data and call the necessary functions
    to make the CSV File.
    :param webURL: The URL of the of the main Home Page
    :param token: The token that will be sent as a header.
            Usually indicates that permission has been given to the given party or
            individual who is using the data.
    :return: None
    """
    webAPI_data = getData(webURL, token)
    heading_1 = ['Dept', 'Category', 'QuestionID', 'ParentQuestionID',
                 'Question', 'Answer', 'ScoreActual', 'ScorePossible',
                 'Comment']
    all_list = list()
    for key in webAPI_data:
        all_list.append(webAPI_data[key])

    # ========================================================== #
    # ========================================================== #
    # Creates a dictionary where all the departments in the different
    # reports are the keys, using open addressing for each of their
    # separates reports.
    newData_dict = dict()
    for dictionary in all_list:
        for key in dictionary:
            if not key in newData_dict:
                newData_dict.setdefault(key, list())
            newData_dict[key].append(dictionary[key])

    # ========================================================== #
    # ========================================================== #
    # Creates a CSV File. Calls the makeCSV function each departmental value
    with open('Report_Output.csv', 'w', newline='') as report_file:
        csvWriter = csv.writer(report_file)
        csvWriter.writerow(heading_1)
        for key in newData_dict:
            for i in range(0, len(newData_dict[key])):
                cat_que_list = (newData_dict[key][i][2])
                for cat in cat_que_list:
                    dept = key
                    category = cat_que_list[cat][0]
                    questionID = cat_que_list[cat][2]
                    parentQuestionID = cat_que_list[cat][4]
                    questions = cat_que_list[cat][3]
                    ans_list = cat_que_list[cat][5]

                    # Function call
                    makeCSV(dept, category, questionID, parentQuestionID, questions, ans_list, csvWriter)
    report_file.close()


def makeCSV(dept, category, questionID, parentQuestionID, questions, ans_list, csvWriter):
    """
    Takes in multiple parameters and writes a set number of rows, in the
    CSV File, depending on the number of elements present in parentQuestionID.
    :param csvWriter: Object for the CSV Writer
    :param dept: Stores the Department
    :param category: Stores the Category
    :param questionID: Stores a list containing Question IDs
    :param parentQuestionID: Stores a list containing Parent Question IDs
    :param questions: Stores a list containing Questions
    :param ans_list: Stores a Dictionary from the Answer key from: (reports/ID/unit_questions)
    :return: None
    """

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

        csvWriter.writerow(write)


CSV_file_getData("https://demo.isora.saltycloud.com/", "c548a5524615454ac53281ac01efd56bbf69f4d9")
