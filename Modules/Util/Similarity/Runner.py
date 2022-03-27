import json

from Modules.Interface.Dialog import Dialogs
from Modules.Util.DataClass.Targets import Targets
from Modules.Util.Similarity.Modules.Progress import calculate_progress
from Modules.Util.Similarity.Modules.Util import is_json, is_xml, calculate_final_score

Targets.difference_element_list = []


def run(target, comp_target):
    if is_json(target):
        target = json.loads(target)
    else:
        target = Targets.data["target_json"] if is_xml(target) else False

    if is_json(comp_target):
        comp_target = json.loads(comp_target)
    else:
        comp_target = Targets.data["comp_target_json"] if is_xml(comp_target) else False

    if not target or not comp_target:
        Dialogs.when_data_is_not_valid()
        return

    Targets.score = calculate_final_score(calculate_progress(target, comp_target))
    Dialogs.when_calculate_complete(Targets.score)
