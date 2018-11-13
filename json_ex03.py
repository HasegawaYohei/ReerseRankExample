import json
import collections as cl

def main():
    name_list = ["honoka", "eri", "kotori", "umi", "rin", "maki", "nozomi", "honayo", "niko"]
    height = [157,162,159,159,155,161,159,156,154]
    BWH = [[78, 58, 82],[88, 60, 84],[80, 58, 80],[76, 58, 80],
           [75, 59, 80],[78, 56, 83],[90, 60, 82],[82, 60, 83],[74, 57, 79]]


    ys = cl.OrderedDict()
    for i in range(len(name_list)):
        data = cl.OrderedDict()
        data["BWH"] = BWH[i]
        data["height"] = height[i]

        ys[name_list[i]] = data


    fw = open('myu_s.json', 'w')
    json.dump(ys, fw, indent=4)


if __name__ == '__main__':
    main()
