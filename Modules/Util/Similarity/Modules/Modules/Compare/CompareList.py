from Modules.Util.Similarity.Modules.Modules.Util import Util


def if_target_is_list(target_list, comp_target, weight):
    score = 0

    if isinstance(comp_target, list):
        score += if_list_and_list(target_list, comp_target, weight)
    if isinstance(comp_target, dict):
        score += if_list_and_dict(target_list, comp_target, weight)

    return score


def if_list_and_list(target_list, comp_target_list, weight):
    score = 0
    t_len = len(target_list)
    ct_len = len(comp_target_list)

    longer_target = target_list if t_len > ct_len else comp_target_list
    diff_in_len = abs(t_len - ct_len)
    weight = Util.get_key_weight(longer_target, weight * t_len)

    if t_len > ct_len:
        score += Util.iteration_list(target_list, comp_target_list, weight)
    else:
        score += Util.iteration_list(comp_target_list, target_list, weight)
    score += diff_in_len * weight

    return score


def if_list_and_dict(target_list, comp_target_dict, weight):
    score = 0

    if comp_target_dict not in target_list:
        from Modules.Util.Similarity.Modules.Modules.Util.Util import check_dict_in_list
        score += check_dict_in_list(target_list, comp_target_dict, weight)

    return score
