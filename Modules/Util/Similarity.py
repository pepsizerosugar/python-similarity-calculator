from PyQt5.QtWidgets import QMessageBox

from Modules.Interface.Dialog import Dialogs
from Modules.Util.DataClass.Target import Targets


def calculate_similarity(param1, param2):
    Targets.score = 0

    # calculate similarity score
    if Targets.target == Targets.comp_target:
        reply = Dialogs.when_both_target_and_comparison_target_are_the_same()
        if reply == QMessageBox.Yes:
            Targets.score = calculate_final_score(get_similarity_score(param1, param2))
            Dialogs.when_calculate_complete(Targets.score)
        else:
            Dialogs.when_cancel_same_target()
    else:
        Targets.score = calculate_final_score(get_similarity_score(param1, param2))
        Dialogs.when_calculate_complete(Targets.score)


def get_similarity_score(target, comp_target, weight=None):
    score = 0
    weight = get_key_weight(target.keys()) if weight is None else weight / len(target.keys())
    then_weight = 0  # for print each depth

    for key in target:
        # for print each depth weight
        if weight == then_weight:
            print(f"[INFO] key: {key} weight: {weight}")
        else:
            print(f"\n[INFO] key: {key} weight: {weight}")
            then_weight = weight

        if key in comp_target:
            if isinstance(target[key], dict):
                if isinstance(comp_target[key], dict):
                    score += get_similarity_score(target[key], comp_target[key], weight)
                elif isinstance(comp_target[key], list):
                    for item in comp_target[key]:
                        score += get_similarity_score(item, target[key], weight)
                else:
                    score += weight
            elif isinstance(target[key], list):
                if isinstance(comp_target[key], list):
                    if len(target[key]) > len(comp_target[key]):
                        for i in range(len(comp_target[key])):
                            score += get_similarity_score(target[key][i], comp_target[key][i], weight)
                    else:
                        for i in range(len(target[key])):
                            score += get_similarity_score(target[key][i], comp_target[key][i], weight)
                elif isinstance(comp_target[key], dict):
                    for item in target[key]:
                        score += get_similarity_score(item, comp_target[key], weight)
                else:
                    score += weight
            else:
                if target[key] != comp_target[key]:
                    print(
                        f"[WARN] key: {key} value: {target[key]} is not equal to {comp_target[key]} with weight: {weight}")
                    score += weight
        else:
            print(f"[WARN] {key} is not in comparison target with weight: {weight}")
            score += weight
    return score


def get_key_weight(keys):
    return 1 / len(keys)


def calculate_final_score(num):
    print(f"\n[INFO] final score: {1 - num}")
    return round((1 - num) * 100, 6)
