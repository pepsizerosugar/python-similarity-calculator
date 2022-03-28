from Modules.Handler.ButtonHandler import ButtonHandler
from Modules.Interface.DataClass.UIElement import UIElements


def switch_label():
    t_label = UIElements.data["target"]["target_label"].text()
    ct_label = UIElements.data["comp_target"]["comp_target_label"].text()
    UIElements.data["target"]["target_label"].setText(ct_label)
    UIElements.data["comp_target"]["comp_target_label"].setText(t_label)

    t_code_label = UIElements.data["target"]["target_code_label"].toPlainText()
    ct_code_label = UIElements.data["comp_target"]["comp_target_code_label"].toPlainText()
    UIElements.data["target"]["target_code_label"].setText(ct_code_label)
    UIElements.data["comp_target"]["comp_target_code_label"].setText(t_code_label)

    if ButtonHandler.t_loaded and ButtonHandler.ct_loaded:
        from Modules.Util.DataClass.Cache import Cache
        Cache.data["target_json"], Cache.data["comp_target_json"] = \
            Cache.data["comp_target_json"], Cache.data["target_json"]
