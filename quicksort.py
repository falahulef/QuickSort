import pandas as pd
from time import time

df = pd.read_csv('dataset.csv')

ourvalues = df.values.tolist()

start = time()


def qsort_index(lst, index):
    if len(lst) == 0:
        return []
    else:
        pivot = lst[0]
        lesser = qsort_index(
            [x for x in lst[1:] if x[index] < pivot[index]], index)
        greater = qsort_index(
            [x for x in lst[1:] if x[index] >= pivot[index]], index)
        return lesser + [pivot] + greater


result = qsort_index(ourvalues, 3)
index = 0
print("Hasil Sorting Kolom H-5 Median\n")
for x in result:
    index += 1
    print(x)
    if index == 10:
        break
print(f'\nWaktu Eksekusi : {time() - start} detik')
