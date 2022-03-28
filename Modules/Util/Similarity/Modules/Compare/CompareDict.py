from Modules.Util.Similarity.Modules import Util, Progress


def if_target_is_dict(target_dict, comp_target, weight):
    score = 0

    if isinstance(comp_target, dict):
        score += if_dict_and_dict(target_dict, comp_target, weight)

    if isinstance(comp_target, list):
        score += if_dict_and_list(target_dict, comp_target, weight)

    return score


def if_dict_and_dict(target_dict, comp_target_dict, weight):
    score = 0
    t_len = len(target_dict)
    ct_len = len(comp_target_dict)

    intersection = Util.get_intersection(target_dict, comp_target_dict)
    longer_target = target_dict if t_len > ct_len else comp_target_dict
    weight = Util.get_key_weight(longer_target, weight * t_len)
    non_intersection_weight = weight * (len(longer_target) - len(intersection))

    if intersection:
        for key in intersection:
            score += Progress.calculate_progress(target_dict[key], comp_target_dict[key], weight)

    score += non_intersection_weight

    return score


def if_dict_and_list(target_dict, comp_target_list, weight):
    score = 0
    dict_score = weight

    for comp_target_item in comp_target_list:
        dict_score = Util.get_lowest_dict_score(dict_score, target_dict, comp_target_item, weight)
        score += dict_score

    return score
