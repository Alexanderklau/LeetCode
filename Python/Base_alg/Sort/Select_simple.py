# coding: utf-8

__author__ = "lau.wenbo"

# Select Sort Work Python
# 选择排序 Python 实现
# 获取到最小值，从左边交换，不断重复

Wait_Sort = [9, 8, 7, 6, 5, 4, 3, 2, 1]


for i in range(len(Wait_Sort)):

    min_idx = i
    for j in range(i + 1, len(Wait_Sort)):
        if Wait_Sort[min_idx] > Wait_Sort[j]:
            min_idx = j

    Wait_Sort[i], Wait_Sort[min_idx] = Wait_Sort[min_idx], Wait_Sort[i]

print(Wait_Sort)


