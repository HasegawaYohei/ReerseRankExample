from file_manager import import_json, export_json

my_list = []
name_list = ["shitara", "himura", "yahagi", "ogi"]
age_list = [45, 46, 45, 45]
for i, name in enumerate(name_list):
    my_list.append({"id": i, "name": name, "age": age_list[i]})

export_json("./result/data.json", my_list)

import_json_data = import_json("./result/data.json")
print(import_json_data)
