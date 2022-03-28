from Modules.Interface.DataClass.UIElement import UIElements
from Modules.Interface.Dialog import Dialogs
from Modules.Util.Load.LoadFile import load_progress
from Modules.Util.Similarity.Runner import run


class ButtonHandler:
    t_loaded = False
    ct_loaded = False

    @classmethod
    def target_load_button_clicked(cls):
        if load_progress("target") is False:
            clear_labels(["target"])
        else:
            cls.t_loaded = True

    @classmethod
    def comp_target_load_button_clicked(cls):
        if load_progress("comp_target") is False:
            clear_labels(["comp_target"])
        else:
            cls.ct_loaded = True

    @staticmethod
    def calculate_button_clicked():
        if check_data():
            from Modules.Util.DataClass.Cache import Cache
            if "target_json" in Cache.data and "comp_target_json" in Cache.data:
                run(Cache.data["target_json"], Cache.data["comp_target_json"], 1)
            else:
                run(UIElements.data["target"]["target_code_label"].toPlainText(),
                    UIElements.data["comp_target"]["comp_target_code_label"].toPlainText())
        else:
            Dialogs.when_not_enough_data()

    @staticmethod
    def switch_button_clicked():
        from Modules.Util.Interface.SwitchLabel import switch_label
        from Modules.Util.Interface.SwitchFileData import switch_file_data
        switch_label()
        switch_file_data()

    @classmethod
    def clear_button_clicked(cls):
        clear_labels(["target", "comp_target"])
        clear_data()
        cls.t_loaded = False
        cls.ct_loaded = False


def check_data():
    if UIElements.data != {}:
        if UIElements.data["target"]["target_code_label"].toPlainText() and \
                UIElements.data["comp_target"]["comp_target_code_label"].toPlainText():
            return True
    return False


def clear_labels(args):
    for arg in args:
        UIElements.data[arg][arg + "_label"].setText("Waiting for load xml file")
        UIElements.data[arg][arg + "_code_label"].clear()


def clear_data():
    from Modules.Util.DataClass.Cache import Cache
    Cache.data = {}
