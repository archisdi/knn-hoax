import xlrd as xr
from libs import utils as u
from operator import itemgetter

file = "archive/dataset.xlsx"

workbook = xr.open_workbook(file)
sheet_train = workbook.sheet_by_index(0)

# load data train
train_data = u.load_data(sheet_train)

# load data test
start_index = 1000
test_data = train_data[start_index:4000]

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


# checking accuracy
n_data = len(test_data)
true_prediction = 0
for i in range(n_data):
    if result[i]['hoax'] == train_data[start_index + i]['hoax']:
        true_prediction += 1

acc = (100 / n_data) * true_prediction
print("Model Accuracy : " + str(acc) + '%')