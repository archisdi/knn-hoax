import xlrd as xr
from libs import utils as u
from operator import itemgetter
from xlutils.copy import copy

file = "archive/dataset.xlsx"

workbook = xr.open_workbook(file)
sheet_train = workbook.sheet_by_index(0)
sheet_test  = workbook.sheet_by_index(1)

# load data train
train_data = u.load_data(sheet_train)

# load data test
test_data = u.load_data(sheet_test)

# initiate k, make it even
k = 11

# main iteration
result = []
for test in test_data:
    res_temp = []
    for train in train_data:
        res_temp.append([train['hoax'],u.euclidean_distance(test['like'],train['like'],test['provokasi'],train['provokasi'],test['komentar'],train['komentar'],test['emosi'],train['emosi']) ])

    sort_res = sorted(res_temp, key=itemgetter(1))
    k_res = sort_res[:k]
    test['hoax'] = u.determine_class(k_res)
    result.append(test)
    print(test)


# save result back to xlsx
result_workbook = copy(workbook)
result_sheet = result_workbook.get_sheet(1)

i = 1
for item in result:
    result_sheet.write(i, 5, item['hoax'])
    i += 1
result_workbook.save('archive/result.xls')