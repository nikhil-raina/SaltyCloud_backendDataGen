import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame
import seaborn as sns
from Data_Directory.APIgetData import heat_map_data


def makeHeatMap(webPage, survey_ID, token):
    """

    :param webPage:
    :param survey_ID:
    :param token:
    :return: None
    """

    heatMap_data = heat_map_data(webPage, survey_ID, token)
    names = heatMap_data[0]
    avg = heatMap_data[1]
    questions = heatMap_data[2]
    answers = heatMap_data[3]

    heatDict = dict()
    for i in range(0,len(names)):
        heatDict[names[i]] = avg[i]

    map = DataFrame(data=avg, index=names)
    sns.heatmap(
        map,
        annot=True,
        square=True
    )
    plt.show()
    print(map)


makeHeatMap("https://demo.isora.saltycloud.com/", "04e818ce-6d54-4ea0-a7ef-1c2bb2d52936",
            "c548a5524615454ac53281ac01efd56bbf69f4d9")
