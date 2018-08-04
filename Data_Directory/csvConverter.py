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
    heading_1 = ['Assessment','Dept', 'Category', 'QuestionID', 'ParentQuestionID',
                 'Question', 'Answer', 'ScoreActual', 'ScorePossible',
                 'Comment']

    # ========================================================== #
    # ========================================================== #
    # Creates a CSV File. Calls the makeCSV function each departmental value
    with open('Report_Output.csv', 'w', newline='') as report_file:
        csvWriter = csv.writer(report_file)
        csvWriter.writerow(heading_1)
        for outer_key in webAPI_data:
            for inner_key in webAPI_data[outer_key]:
                for i in range(0, len(webAPI_data[outer_key][inner_key])):
                    val_dict = webAPI_data[outer_key][inner_key][2]
                    for cat in val_dict:
                        assessment = outer_key
                        dept = inner_key
                        category = val_dict[cat][0]
                        questionID = val_dict[cat][2]
                        parentQuestionID = val_dict[cat][4]
                        questions = val_dict[cat][3]
                        ans_list = val_dict[cat][5]

                        # Function call
                        makeCSV(assessment, dept, category, questionID, parentQuestionID, questions, ans_list, csvWriter)
    report_file.close()


def makeCSV(assessment, dept, category, questionID, parentQuestionID, questions, ans_list, csvWriter):
    """
    Takes in multiple parameters and writes a set number of rows, in the
    CSV File, depending on the number of elements present in parentQuestionID.
    :param assessment: The assessment category
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
        write.append(assessment)            # A
        write.append(dept)                  # B
        write.append(category)              # C
        write.append(questionID[i])         # D
        write.append(parentQuestionID[i])   # E
        write.append(questions[i])          # F
        write.append(answer)                # G
        write.append(scoreActual)           # H
        write.append(scorePossible)         # I
        write.append(comment)               # J

        csvWriter.writerow(write)


CSV_file_getData("https://demo.isora.saltycloud.com/", "c548a5524615454ac53281ac01efd56bbf69f4d9")
