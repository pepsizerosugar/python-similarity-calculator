from Modules.Interface.DataClass.UIElement import UIElements
from Modules.Interface.Dialog import Dialogs
from Modules.Util.Convert import convert_progress
from Modules.Util.Similarity.Runner import run


class ButtonHandler:
    t_loaded = False
    ct_loaded = False

    def __init__(self):
        super().__init__()

    @classmethod
    def target_load_button_clicked(cls):
        if convert_progress("target") is False:
            clear_labels(["target"])
        else:
            cls.t_loaded = True

    @classmethod
    def comp_target_load_button_clicked(cls):
        if convert_progress("comp_target") is False:
            clear_labels(["comp_target"])
        else:
            cls.ct_loaded = True

    @staticmethod
    def calculate_button_clicked():
        if check_data():
            run(UIElements.data["target"]["target_code_label"].toPlainText(),
                UIElements.data["comp_target"]["comp_target_code_label"].toPlainText())
        else:
            Dialogs.when_not_enough_data()

    @staticmethod
    def switch_button_clicked():
        from Modules.Util.Interface.SwitchLabel import switch_label
        switch_label()

    @classmethod
    def clear_button_clicked(cls):
        clear_labels(["target", "comp_target"])
        cls.t_loaded = False
        cls.ct_loaded = False


def check_data():
    if UIElements.data["target"]["target_code_label"].toPlainText() and \
            UIElements.data["comp_target"]["comp_target_code_label"].toPlainText():
        return True
    return False


def clear_labels(args):
    for arg in args:
        UIElements.data[arg][arg + "_label"].setText("Waiting for load xml file")
        UIElements.data[arg][arg + "_code_label"].clear()
