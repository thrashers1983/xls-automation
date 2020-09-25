from switches import acc_stat
from switches import core_stat
from switches import ap_stat
import csv

store_list = []
with open('apac_store_list') as f:
    for line in f:
        store_number, *_ = line.split(':')
        store_list.append(store_number.lower())

print(store_list)
print(len(store_list))

# # 以下这段代码是输出acc-sw的统计
# statistics = []
# headers = ['store', 'acc-sw QTY', 'WS-C3560CX-12TC-S', 'WS-C3560CX-12PC-S', 'WS-C3560CX-8PC-S',
#            'WS-C3560-12PC-S', 'WS-C3560-8PC-S', 'C2960', 'C2960 ratio']
#
# for store_no in store_list:
#     store = acc_stat(store_no)
#     statistics.append(store)
#
# for i in statistics:
#     if i['acc-sw QTY'] != i['WS-C3560CX-12TC-S'] + i['WS-C3560CX-12PC-S'] + i['WS-C3560CX-8PC-S'] \
#             + i['WS-C3560-12PC-S'] + i['WS-C3560-8PC-S'] + i['C2960']:
#         print(i['store'])
#
# statistics_sort = sorted(statistics, key=lambda s: s['C2960 ratio'], reverse=True)
#
# for store in statistics_sort:
#     store['C2960 ratio'] = "{:.0%}".format(store['C2960 ratio'])
#
# with open('../data/test.csv', 'w+') as f:
#     f_csv = csv.DictWriter(f, headers)
#     f_csv.writeheader()
#     f_csv.writerows(statistics_sort)

# with open('../data/result', 'a') as file:
#     for store in statistics_sort:
#         file.write("{0:<8s}total: {1:<8d}3560: {2:<8d}2960: {3:<8d}2960 ratio: {4:.0%}\n"
#                    .format(store['store'], store['acc_total'], store['c3560'], store['c2960'], store['c2960_ratio']))

# # 以下这段代码是输出core-sw/srv-sw/rsr-sw的统计
# statistics = []
# headers = ['store', 'core-sw1', 'core-sw2', 'srv-sw1', 'rsr-sw1', 'rsr-sw2', 'rsr-sw3']
#
# for store_no in store_list:
#     store = core_stat(store_no)
#     statistics.append(store)
#
# with open('../data/core_srv_rsr.csv', 'w+') as f:
#     f_csv = csv.DictWriter(f, headers)
#     f_csv.writeheader()
#     f_csv.writerows(statistics)

# 以下这段代码输出AP的统计
statistics = []
headers = ['store', 'total ap', '3602', '3702', '3802']

for store_no in store_list:
    store = ap_stat(store_no)
    statistics.append(store)

with open('../data/ap.csv', 'w+') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(statistics)


