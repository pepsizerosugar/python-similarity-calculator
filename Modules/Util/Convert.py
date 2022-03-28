import json
import os
import pyexpat

import xmltodict

from Modules.Handler import PrintHandler
from Modules.Interface.DataClass.UIElement import UIElements
from Modules.Interface.Dialog import Dialogs
from Modules.Util.DataClass.Targets import Targets

Targets.data = {}


def convert_progress(args):
    Targets.data[args + "_path"] = Dialogs.when_try_to_load_file()
    file_ext = os.path.splitext(Targets.data[args + "_path"])[1]
    file_name = os.path.basename(Targets.data[args + "_path"])
    if file_ext == ".xml":
        if Targets.data[args + "_path"]:
            Targets.data[args + "_file_name"] = file_name
            if load_xml(args, Targets.data[args + "_path"]):
                UIElements.data[args][args + "_label"].setText(Targets.data[args + "_file_name"])
                UIElements.data[args][args + "_code_label"].setText(Targets.data[args + "_xml"])

                if convert_xml_to_json(Targets.data[args + "_path"], Targets.data[args + "_xml"]):
                    load_json(args, Targets.data[args + "_path"], 1)
                return True
        return False
    if file_ext == ".json":
        if Targets.data[args + "_path"]:
            Targets.data[args + "_file_name"] = file_name
            if load_json(args, Targets.data[args + "_path"]):
                UIElements.data[args][args + "_label"].setText(Targets.data[args + "_file_name"])
                UIElements.data[args][args + "_code_label"].setText(
                    json.dumps(Targets.data[args + "_json"], indent=2, sort_keys=True, ensure_ascii=False))
                return True
        return False
    Dialogs.when_no_file_selected()
    return False


def convert_xml_to_json(xml_path, xml):
    try:
        json_data = xmltodict.parse(xml)
        json_file_name = os.path.basename(xml_path).replace(".xml", ".json")

        os.makedirs(Targets.json_path, exist_ok=True)

        with open(Targets.json_path + json_file_name, 'w', encoding="utf-8") as f:
            json.dump(json_data, f, indent=2, sort_keys=True, ensure_ascii=False)

        return True

    except pyexpat.ExpatError as e:
        PrintHandler.error(e)
        Dialogs.when_xml_file_is_not_valid()
        return False

    except Exception as e:
        PrintHandler.error(e)
        Dialogs.when_get_error_at_convert_to_json()
        return False


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


def load_json(args, file_path, trigger=0):
    if trigger == 1:
        file_name = os.path.basename(file_path).replace(".xml", ".json")
        file_path = Targets.json_path + file_name
    try:
        with open(file_path, "r", encoding="utf-8") as f:
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
