import json
from json import JSONDecodeError

from defusedxml import ElementTree
from defusedxml.ElementTree import fromstring


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

    from deepdiff import DeepDiff
    if DeepDiff(list_1, list_2, ignore_order=True, report_repetition=True, verbose_level=2):
        for item_1 in list_1:
            if item_1 not in list_2:
                score += check_dict_in_list(list_2, item_1, weight)

    return score


def check_dict_in_list(dict_list, dict_to_check, weight):
    score = 0
    check_similar_dict_exist = False

    for dict_item in dict_list:
        intersection = get_intersection(dict_to_check, dict_item)
        if len(intersection) == len(dict_to_check) or len(intersection) == len(dict_item):
            from Modules.Util.Similarity.Modules.Progress import calculate_progress
            score += calculate_progress(dict_to_check, dict_item, weight)
            check_similar_dict_exist = True
            break
    if not check_similar_dict_exist:
        score += weight * (len(dict_list) - 1)

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
        fromstring(xml_str)
    except ElementTree.ParseError:
        return False
    return True
