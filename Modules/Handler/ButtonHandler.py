import ErrorHandler
from Modules.Interface.DataClass.UIElement import UIElements
from Modules.Util import Similarity
from Modules.Util.Convert import convert_progress
from Modules.Util.DataClass.Target import Targets


class ButtonHandler:
    def __init__(self):
        super().__init__()

    @staticmethod
    def target_load_button_clicked():
        clear_labels(["target"]) if convert_progress("target") is False else None
        check_data_for_button_enable()

    @staticmethod
    def comp_target_load_button_clicked():
        clear_labels(["comp_target"]) if convert_progress("comp_target") is False else None
        check_data_for_button_enable()

    @staticmethod
    def calculate_button_clicked():
        Similarity.calculate_similarity(Targets.data["target_json"], Targets.data["comp_target_json"])

    @staticmethod
    def clear_button_clicked():
        clear_labels(["target", "comp_target"])


def check_data_for_button_enable():
    try:
        if Targets.data["target_json"] and Targets.data["comp_target_json"]:
            UIElements.calculate_button.setEnabled(True)
        else:
            UIElements.calculate_button.setEnabled(False)
    except KeyError as e:
        ErrorHandler.printing(e)
        pass


def clear_labels(args):
    for arg in args:
        UIElements.data[arg][arg + "_label"].setText("Waiting for load xml file")
        UIElements.data[arg][arg + "_code_label"].setText("")
    UIElements.calculate_button.setEnabled(False)
