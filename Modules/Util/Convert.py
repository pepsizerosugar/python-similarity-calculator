import json
import os
import pyexpat

import xmltodict

import PrintHandler
from Modules.Interface.DataClass.UIElement import UIElements
from Modules.Interface.Dialog import Dialogs
from Modules.Util.DataClass.Targets import Targets

Targets.data = {}


def convert_progress(args):
    Targets.data[args + "_path"] = Dialogs.when_try_to_load_file()
    if Targets.data[args + "_path"]:
        Targets.data[args + "_file_name"] = os.path.basename(Targets.data[args + "_path"])
        if load_xml(args, Targets.data[args + "_path"]):
            UIElements.data[args][args + "_label"].setText(Targets.data[args + "_file_name"])
            UIElements.data[args][args + "_code_label"].setText(Targets.data[args + "_xml"])

            convert_xml_to_json(Targets.data[args + "_file_name"], Targets.data[args + "_xml"])
            load_json(args, Targets.data[args + "_file_name"])
            return True
        else:
            return False
    else:
        Dialogs.when_no_file_selected()
        return False


def convert_xml_to_json(file_name, xml):
    try:
        json_data = xmltodict.parse(xml)
        json_file_name = file_name.replace(".xml", ".json")

        os.makedirs(Targets.json_path, exist_ok=True)

        with open(Targets.json_path + json_file_name, 'w', encoding="utf-8") as f:
            json.dump(json_data, f, indent=2, sort_keys=True, ensure_ascii=False)

    except pyexpat.ExpatError as e:
        PrintHandler.error(e)
        Dialogs.when_xml_file_is_not_valid()

    except Exception as e:
        PrintHandler.error(e)
        Dialogs.when_get_error_at_convert_to_json()


def load_xml(args, file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            Targets.data[args + "_xml"] = f.read()
        return True

    except FileNotFoundError as e:
        PrintHandler.error(e)
        Dialogs.when_xml_file_not_found()
        return False

    except Exception as e:
        PrintHandler.error(e)
        Dialogs.when_get_error_at_load_xml()
        return False


def load_json(args, file_name):
    try:
        with open(os.path.join(Targets.json_path + file_name.replace(".xml", ".json")),
                  "r", encoding="utf-8") as f:
            Targets.data[args + "_json"] = json.load(f)
        Dialogs.when_load_success()
        return True

    except FileNotFoundError as e:
        PrintHandler.error(e)
        Dialogs.when_json_file_not_found()
        return False

    except Exception as e:
        PrintHandler.error(e)
        Dialogs.when_get_error_at_load_json()
        return False
