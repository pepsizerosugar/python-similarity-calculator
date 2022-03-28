import json
import os

from Modules.Handler import PrintHandler
from Modules.Interface.DataClass.UIElement import UIElements
from Modules.Interface.Dialog import Dialogs
from Modules.Util.Convert.Convert import convert_xml_to_json
from Modules.Util.DataClass.Cache import Cache


def load_progress(arg):
    file_path = Dialogs.when_try_to_load_file()
    file_ext = os.path.splitext(file_path)[1]
    file_name = os.path.basename(file_path)

    if file_ext == ".xml":
        if file_path:
            file_xml_data = load_xml(arg, file_path)
            UIElements.data[arg][arg + "_label"].setText(file_name)
            UIElements.data[arg][arg + "_code_label"].setText(file_xml_data)

            Cache.data[arg + "_json"] = convert_xml_to_json(arg, file_xml_data)
            return True
        return False

    if file_ext == ".json":
        if file_path:
            file_json_data = load_json(arg, file_path)
            UIElements.data[arg][arg + "_label"].setText(file_name)
            UIElements.data[arg][arg + "_code_label"] \
                .setText(json.dumps(file_json_data, indent=2, sort_keys=True, ensure_ascii=False))
            return True
        return False

    Dialogs.when_no_file_selected()
    return False


def load_xml(arg, file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            Cache.data[arg + "_xml"] = f.read()
            Dialogs.when_load_success()
            return Cache.data[arg + "_xml"]

    except FileNotFoundError as e:
        PrintHandler.error(e)
        Dialogs.when_xml_file_not_found()
        return False

    except Exception as e:
        PrintHandler.error(e)
        Dialogs.when_get_error_at_load_xml()
        return False


def load_json(arg, file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            Cache.data[arg + "_json"] = json.load(f)
            Dialogs.when_load_success()
            return Cache.data[arg + "_json"]

    except FileNotFoundError as e:
        PrintHandler.error(e)
        Dialogs.when_json_file_not_found()
        return False

    except Exception as e:
        PrintHandler.error(e)
        Dialogs.when_get_error_at_load_json()
        return False
