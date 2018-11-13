from datetime import datetime
import json


def import_json(path):
    f = open(f"{path}", 'r')
    json_data = json.load(f)

    return json_data


def export_json(path, data):
    f = open(f"{path}", 'w')
    json.dump(data, f, indent=2)


def export_json_list(export_list, name):
    export_json_list = []
    for elem in export_list:
        json_data = elem.export_json_format()
        export_json_list.append(json_data)

    export_json(f"data/{name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.json", export_json_list)


