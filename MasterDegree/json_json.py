import json
import csv
import os


def main():
    filename = 'info_test.json'
    input = os.path.join('info/', filename)
    with open(input) as f:
        data = json.loads(f.read())

    with open('loc_dic.json') as f:
        city_state_dict = json.loads(f.read())

    for t in data.keys():
        data[t]["city"] = city_state_dict[t]["city"]
        data[t]["state"] = city_state_dict[t]["state"]


    output = os.path.join('info', filename[2:])
    with open(output, 'w') as f:
        json.dump(data, f)


if __name__ == "__main__":
    main()
