import math

def euclidean_distance(x1, x2, y1, y2, k1, k2, c1, c2):
    temp = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (k1 - k2) ** 2 + (c1 - c2) ** 2
    return math.sqrt(temp)


def load_data(sheet):
    temp = []
    for i in range(1, sheet.nrows):
        data = {}
        data['like'] = sheet.cell_value(i, 1)
        data['provokasi'] = sheet.cell_value(i, 2)
        data['komentar'] = sheet.cell_value(i, 3)
        data['emosi'] = sheet.cell_value(i, 4)
        data['hoax'] = sheet.cell_value(i, 5)
        temp.append(data)

    return temp

def determine_class(data):
    true = 0
    false = 0

    for item in data:
        if item[0] == 1:
            true += 1
        else:
            false += 1

    return 1 if true > false else 0