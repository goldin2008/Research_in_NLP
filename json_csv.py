import json
import csv


def main():
    with open('info/info_test.json') as f:
        data = json.loads(f.read())

    # employee_parsed = json.loads('info.json')
    # print employee_parsed.keys()
    # exit()



    # open a file for writing
    output = open('info_out.csv', 'w')

    # create the csv writer object
    csvwriter = csv.writer(output)


    # print emp_data
    # print emp_data.keys()
    csvwriter.writerow(["ID", "Journal Name", "Author 1", "Author 2", "Author 3", "Author 4",
     "Author 5", "Data/Year", "Location(city)", "Location(state)", "Abstract"])
    i = 1
    for t in data.keys():
        # string = d.encode("utf-8")
        # a0 = emp_data[emp]["author1"].encode("utf-8")
        # a1 = emp_data[emp]["author2"].encode("utf-8")
        # a2 = emp_data[emp]["author3"].encode("utf-8")
        # a3 = emp_data[emp]["author4"].encode("utf-8")
        # a4 = emp_data[emp]["author5"].encode("utf-8")
        # d = emp_data[emp]["date"].encode("utf-8")
        # lc = emp_data[emp]["city"].encode("utf-8")
        # ls = emp_data[emp]["state"].encode("utf-8")
        # abst = emp_data[emp]["abstract"].encode("utf-8")
        a0 = data[t]["author1"].encode("utf-8")
        a1 = data[t]["author2"].encode("utf-8")
        a2 = data[t]["author3"].encode("utf-8")
        a3 = data[t]["author4"].encode("utf-8")
        a4 = data[t]["author5"].encode("utf-8")
        d = data[t]["date"].encode("utf-8")
        lc = data[t]["city"].encode("utf-8")
        ls = data[t]["state"].encode("utf-8")
        abst = data[t]["abstract"].encode("utf-8")
        csvwriter.writerow([str(i), string, a0, a1, a2, a3, a4, d, lc, ls, abst])
        i = i+1

    employ_data.close()

    # objects = json.load(open('info_8.json'))
    # s = ''
    # for obj in objects:
    #     # This depends on the json file... but something like:
    #     # s += ', '.join(obj)
    #     s += ', '.join(objects[obj]["date"])
    #     s += '\n'
    # f = open('out.csv','w')
    # f.write(s)
    # f.close()

if __name__ == "__main__":
    main()