import json
import os

import pyexpat
import xmltodict

from Modules.Handler import PrintHandler
from Modules.Interface.Dialog import Dialogs
from Modules.Util.DataClass.Cache import Cache

Cache.data = {}


def convert_xml_to_json(arg, xml):
    try:
        json_data = xmltodict.parse(xml)

        os.makedirs(Cache.json_path, exist_ok=True)
        with open(Cache.json_path + arg + ".json", 'w', encoding="utf-8") as f:
            json.dump(json_data, f, indent=2, sort_keys=True, ensure_ascii=False)

        return json_data
    except pyexpat.ExpatError as e:
        PrintHandler.error(e)
        Dialogs.when_xml_file_is_not_valid()
        return False

    except Exception as e:
        PrintHandler.error(e)
        Dialogs.when_get_error_at_convert_to_json()
        return False
