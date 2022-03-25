import PrintHandler
from Modules.Interface.Dialog import Dialogs
from Modules.Util.DataClass.Targets import Targets

Targets.difference_element_list = []


def run(target, comp_target):
    Targets.score = calculate_final_score(calculate_similarity(target, comp_target))
    Dialogs.when_calculate_complete(Targets.score)


def calculate_similarity(target, comp_target, weight=None):
    score = 0
    weight = get_key_weight(target.keys(), weight)

    for key in target:
        PrintHandler.info(key, weight)

        if key not in comp_target:
            Targets.difference_element_list.append([key, weight])
            PrintHandler.when_key_is_not_in_comparison_target(key, weight)
            score += weight
        else:
            t_value = target[key]
            ct_value = comp_target[key]

            if isinstance(t_value, dict):
                score += if_target_type_is_dict(t_value, ct_value, weight)
                continue

            if isinstance(t_value, list):
                score += if_target_type_is_list(t_value, ct_value, weight)
                continue

            if t_value != ct_value:
                Targets.difference_element_list.append([key, weight, t_value, ct_value])
                PrintHandler.when_key_is_not_equal_to_comparison_target(key, weight, t_value, ct_value)
                score += weight
    return score


def get_key_weight(keys, weight):
    return 1 / len(keys) if weight is None else weight / len(keys)


def if_target_type_is_dict(t_value, ct_value, weight):
    score = 0
    if isinstance(ct_value, dict):
        score += calculate_similarity(t_value, ct_value, weight)

    if isinstance(ct_value, list):
        for c_item in ct_value:
            score += calculate_similarity(c_item, t_value, weight)

    return score


def if_target_type_is_list(t_value, ct_value, weight):
    score = 0
    if isinstance(ct_value, list):
        if len(t_value) > len(ct_value):
            for i, ct_item in enumerate(ct_value):
                score += calculate_similarity(t_value[i], ct_item, weight)
        else:
            for i, v_item in enumerate(t_value):
                score += calculate_similarity(v_item, ct_value[i], weight)

    if isinstance(ct_value, dict):
        for v_item in t_value:
            score += calculate_similarity(v_item, ct_value, weight)

    return score


def calculate_final_score(num):
    PrintHandler.final_score(num)
    return round((1 - num) * 100, 6)
