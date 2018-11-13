import json

def main():
    f = open("ex.json", 'r')

    json_data = json.load(f)

    name_list = ["honoka", "eri", "kotori", "umi", "rin", "maki", "nozomi", "hanayo", "niko"]
    for name in name_list:
        print(f"{name} 身長:{json_data[name]['height']}")
        for i in range(len(json_data[name]["BWH"])):
            print(f"{json_data[name]['BWH'][i]}")
        print()


if __name__ == '__main__':
    main()
