import json
import os

import xmltodict

from Modules.Interface.Dialog import Dialogs


def convert_xml_to_json(path, xml):
    try:
        json_path = 'Resources/json/'
        json_data = xmltodict.parse(xml)
        json_file_name = path.split('/')[-1].split('.')[0] + '.json'
        os.makedirs(json_path, exist_ok=True)
        with open(json_path + json_file_name, 'w', encoding="utf-8") as f:
            json.dump(json_data, f, indent=2, sort_keys=True, ensure_ascii=False)
    except Exception as e:
        print(e)
        Dialogs.when_get_error_at_convert_to_json()
