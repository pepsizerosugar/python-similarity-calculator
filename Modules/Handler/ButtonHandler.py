from Modules.Interface.DataClass.UIElement import UIElements
from Modules.Interface.Dialog import Dialogs
from Modules.Util.Convert import convert_progress
from Modules.Util.Similarity.Runner import run


class ButtonHandler:
    def __init__(self):
        super().__init__()

    @staticmethod
    def target_load_button_clicked():
        if convert_progress("target") is False:
            clear_labels(["target"])

    @staticmethod
    def comp_target_load_button_clicked():
        if convert_progress("comp_target") is False:
            clear_labels(["comp_target"])

    @staticmethod
    def calculate_button_clicked():
        if check_data():
            run(UIElements.data["target"]["target_code_label"].toPlainText(),
                UIElements.data["comp_target"]["comp_target_code_label"].toPlainText())
        else:
            Dialogs.when_not_enough_data()

    @staticmethod
    def clear_button_clicked():
        clear_labels(["target", "comp_target"])


def check_data():
    if UIElements.data["target"]["target_code_label"].toPlainText() and \
            UIElements.data["comp_target"]["comp_target_code_label"].toPlainText():
        return True
    return False


def clear_labels(args):
    for arg in args:
        UIElements.data[arg][arg + "_label"].setText("Waiting for load xml file")
        UIElements.data[arg][arg + "_code_label"].clear()
