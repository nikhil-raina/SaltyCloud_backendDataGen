import csv
from APIgetData import getData


def makeCSV_file(webURL, token):
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

    heading_2 = ['Names', 'Description', 'IPS', 'Macs', 'Aco', 'Site',
                 'Building', 'Floor', 'Room', 'Location_Notes', 'Off_Premises',
                 'Inventory_Tag', 'Serial', 'System', 'Classification', 'Categories',
                 'Priority', 'System_Type', 'Encrypted', 'Free_Fields', 'Owners',
                 'IT_Contacts', 'Users']

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


    # workbook = xlsxwriter.Workbook('csvFile.xlsx')
    # worksheet_data = workbook.add_worksheet('data')
    # worksheet_analysis = workbook.add_worksheet('analysis')

    '''
    with open('Report_Output_Template.csv', 'w', newline='') as report_file:
        csvwriter = csv.writer(report_file)
        csvwriter.writerow(heading_1)
        csvwriter.writerow(header)
        report_file.close()
    


    with open('Host_Output_Template.csv', 'w', newline='') as host_file:
        csvwriter = csv.writer(host_file)
        csvwriter.writerow(heading_2)
    '''
    var = 1


makeCSV_file("https://demo.isora.saltycloud.com/",
             "c548a5524615454ac53281ac01efd56bbf69f4d9")
