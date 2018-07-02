import requests as r


def getData(webPage, token):

    response = r.get('https://'+webPage,
                     headers={"Authorization": "Token "+token,
                              "Content-Type": "application/json"})
    print(response.text)

    """
    after knowing the data that is required for the graphs... pluck out that specific data from the (text)
    and make a list or dictionary of it.... depends on how you plan on putting it.
    """

    print()
    print('response status: ' + str(response.status_code))


getData("demo.isora.saltycloud.com/api/reports",
        "c548a5524615454ac53281ac01efd56bbf69f4d9")
