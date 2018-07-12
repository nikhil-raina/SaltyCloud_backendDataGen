import requests as r
import json


def getData(webPage, token):

    response = r.get(webPage+"api/reports", headers={"Authorization": "Token "+token,
                                                     "Content-Type": "application/json"})
    data = json.loads(response.text)
    all_data = dict

    if data['count'] > 0:
        results = data['results']       # results = list
        assessment_type_list = dict()
        org_unit_code = list()


        for key in results:
            if not assessment_type_list.__contains__(key['assessment_type']):
                assessment_type_list.setdefault(key['assessment_type'], dict())

            if not org_unit_code.__contains__(key['org_unit_code']):
                org_unit_code.append(key['org_unit_code'])

            val = assessment_type_list.get(key['assessment_type'])
            if not val.get(key['org_unit_name']) is None:
                ans = val.get(key['org_unit_name'])
                code = ans.pop(len(ans)-1)
                if code == key['org_unit_code']:
                    val[key['org_unit_name']].append(key['assessment_name'])
                val[key['org_unit_name']].append(code)

            else:
                val[key['org_unit_name']] = list()
                assessment_type_list[key['assessment_type']][key['org_unit_name']].append(key['assessment_name'])
                assessment_type_list[key['assessment_type']][key['org_unit_name']].append(key['org_unit_code'])

    # ===============================================================

            links = key['links']
            unit_questions = links["unit-questions"]

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
    category_name = list()
    category_id = dict()
    category_avg = list()
    questions = dict()
    for categories in data['categories']:
        category_id[categories['id']] = list()
        category_id[categories['id']].append(categories['name'])
        category_id[categories['id']].append(categories['average'])
        for que in data['questions']:
            q1 = que.get('question')
            if q1['category'] == categories['id']:
                questions[categories['id']] = que





getData("https://demo.isora.saltycloud.com/", "c548a5524615454ac53281ac01efd56bbf69f4d9")
