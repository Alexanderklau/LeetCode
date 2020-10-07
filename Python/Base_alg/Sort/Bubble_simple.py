# coding: utf-8

__author__ = "lau.wenbo"

# 冒泡排序的基础写法 Python
# Bubble sort base work Python

Wait_Sort_list = [4, 3, 2, 1]

def Bubble_Sort(sort_lists):

    SortNum = len(sort_lists)


    for x in range(SortNum):
        for y in range(SortNum - x - 1):
            print(y, y + 1)
            if sort_lists[y] > sort_lists[y + 1]:
                sort_lists[y], sort_lists[y + 1] = sort_lists[y + 1], sort_lists[y]


if __name__ == '__main__':
    Bubble_Sort(Wait_Sort_list)

    print(Wait_Sort_list)