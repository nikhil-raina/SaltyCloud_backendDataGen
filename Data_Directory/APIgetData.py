import requests as r
import json


def getData(webPage, token):

    response = r.get(webPage+"api/reports", headers={"Authorization": "Token "+token,
                                                     "Content-Type": "application/json"})
    data = json.loads(response.text)
    all_data = dict()

    if data['count'] > 0:
        results = data['results']       # results = list
        each_assessment_type = list()
        each_assessment_name = list()


        for each in results:
            if not each_assessment_type.__contains__(each['assessment_type']):
                each_assessment_type.append(each['assessment_type'])

            each_assessment_name.append(each['assessment_name'])

        all_data["assessment_type"] = each_assessment_type
        links = results['links']
        unit_questions = links['unit_questions']
        u_questions_data = unit_q_data(webPage, token, unit_questions)

        """
        after knowing the data that is required for the graphs... pluck out that specific data from the (text)
        and make a list or dictionary of it.... depends on how you plan on putting it.
        """

        print()
        print('response status: ' + str(response.status_code))

    else:
        return "There is NO DATA present"


def unit_q_data(webPage, token, unit_questions):

    response = r.get(webPage+unit_questions, headers={"Authorization": "Token "+token,
                                                      "Content-Type": "application/json"})
    data = json.loads(response.text)
    categories = data['categories']





getData("https://demo.isora.saltycloud.com/", "c548a5524615454ac53281ac01efd56bbf69f4d9")
