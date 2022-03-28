from Modules.Util.DataClass.Cache import Cache


def switch_file_data():
    with open(Cache.json_path + "target.json", 'r', encoding="utf-8") as f:
        target_data = f.read()
        if target_data:
            with open(Cache.json_path + "comp_target.json", 'r', encoding="utf-8") as f:
                comp_target_data = f.read()
                open(Cache.json_path + "target.json", 'w', encoding="utf-8").write(comp_target_data)
                open(Cache.json_path + "comp_target.json", 'w', encoding="utf-8").write(target_data)
