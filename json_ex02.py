import json

def main():
    f = open('ex.json', 'r')
    json_data = json.load(f)

    print(f"{json.dumps(json_data, indent=4)}")


if __name__ == '__main__':
    main()
