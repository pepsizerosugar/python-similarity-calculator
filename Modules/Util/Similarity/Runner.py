from Modules.Interface.Dialog import Dialogs
from Modules.Util.DataClass.Cache import Cache
from Modules.Util.Similarity.Modules.Modules.Util.Util import calculate_final_score, is_json, is_xml
from Modules.Util.Similarity.Modules.Progress import calculate_progress

Cache.difference_element_list = []


def run(target, comp_target, trigger=0):
    if trigger != 1:
        if not is_json(target) and not is_json(comp_target):
            if not is_xml(target) and not is_xml(comp_target):
                Dialogs.when_data_is_not_valid()
                return

    Cache.score = calculate_final_score(calculate_progress(target, comp_target))
    Dialogs.when_calculate_complete(Cache.score)
