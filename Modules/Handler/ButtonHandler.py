import json
import os

import Modules.Interface.Dialog.Dialogs as Dialogs
from Modules.Interface.DataClass.UIElement import UIElements
from Modules.Util import Similarity
from Modules.Util.Convert import convert_xml_to_json
from Modules.Util.DataClass.Target import Targets

path = "Resources/json/"


class ButtonHandler:
    def __init__(self):
        super().__init__()

    @staticmethod
    def target_load_button_clicked():
        Targets.target = Dialogs.when_try_to_load_file()

        if Targets.target:
            Targets.target_xml = load_xml(Targets.target)

            UIElements.target_label.setText(Targets.target)
            UIElements.target_code_label.setText(Targets.target_xml)

            convert_xml_to_json(Targets.target, Targets.target_xml)
            Targets.target_json = load_json(Targets.target)
        else:
            Dialogs.when_no_file_selected()
            clear_target_labels()

        check_data_for_button_enable()

    @staticmethod
    def comp_target_load_button_clicked():
        Targets.comp_target = Dialogs.when_try_to_load_file()

        if Targets.comp_target:
            Targets.comp_target_xml = load_xml(Targets.comp_target)

            UIElements.comp_target_label.setText(Targets.comp_target)
            UIElements.comp_target_code_label.setText(Targets.comp_target_xml)

            convert_xml_to_json(Targets.comp_target, Targets.comp_target_xml)
            Targets.comp_target_json = load_json(Targets.comp_target)
        else:
            Dialogs.when_no_file_selected()
            clear_comp_target_labels()

        check_data_for_button_enable()

    @staticmethod
    def calculate_button_clicked():
        Similarity.calculate_similarity(Targets.target_json, Targets.comp_target_json)

    @staticmethod
    def clear_button_clicked():
        clear_target_labels()
        clear_comp_target_labels()


def load_xml(args):
    return open(args, "r", encoding="utf-8").read()


def load_json(args):
    for_return = json.load(open(os.path.join(path + args.split('/')[-1].split('.')[0] + '.json'),
                                "r", encoding="utf-8"))
    Dialogs.when_comparison_target_load_success()
    return for_return


def check_data_for_button_enable():
    if Targets.target and Targets.comp_target:
        UIElements.calculate_button.setEnabled(True)
    else:
        UIElements.calculate_button.setEnabled(False)


def clear_target_labels():
    UIElements.target_label.setText("")
    UIElements.target_code_label.setText("")


def clear_comp_target_labels():
    UIElements.comp_target_label.setText("")
    UIElements.comp_target_code_label.setText("")
