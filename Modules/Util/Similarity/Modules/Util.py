import json
import xml.etree.ElementTree as elementTree
from json import JSONDecodeError


def get_key_weight(target, weight):
    length = 1
    if isinstance(target, (dict, list)):
        length = len(target)

    return 1 / length if weight is None else weight / length if length > 0 else weight


def get_intersection(target, comp_target):
    return set(target.keys()) & set(comp_target.keys())


def get_lowest_dict_score(dict_score, dict_1, dict_2, weight):
    from Modules.Util.Similarity.Modules.Progress import calculate_progress
    temp_score = calculate_progress(dict_1, dict_2, weight)
    dict_score = temp_score if temp_score <= dict_score else dict_score
    return dict_score


def iteration_list(list_1, list_2, weight):
    score = 0

    for item_1 in list_1:
        dict_score = weight
        for item_2 in list_2:
            dict_score = get_lowest_dict_score(dict_score, item_1, item_2, weight)
        score += dict_score

    return score


def calculate_final_score(num):
    from Modules.Handler import PrintHandler
    PrintHandler.final_score(num)
    return round((1 - num) * 100, 6)


def is_json(json_str):
    try:
        json.loads(json_str)
    except JSONDecodeError:
        return False
    return True


def is_xml(xml_str):
    try:
        elementTree.fromstring(xml_str)
    except elementTree.ParseError:
        return False
    return True
