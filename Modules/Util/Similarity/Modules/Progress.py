from Modules.Util.Similarity.Modules.Modules.Compare import CompareList, CompareDict
from Modules.Util.Similarity.Modules.Modules.Util import Util


def calculate_progress(target, comp_target, weight=None):
    score = 0
    weight = Util.get_key_weight(target, weight)

    if isinstance(target, dict):
        score += CompareDict.if_target_is_dict(target, comp_target, weight)
        return score
    if isinstance(target, list):
        score += CompareList.if_target_is_list(target, comp_target, weight)
        return score

    if target != comp_target:
        score += weight

    return score
