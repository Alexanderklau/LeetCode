# coding: utf-8

__author__ = "lau.wenbo"

# insertion sort work Python
# 插入排序实现

Wait_Sort = [6, 9, 1, 3, 4, 2]


def Ins_sort(waitlists):

    for i in range(1, len(Wait_Sort)):

        # 插入值
        key = Wait_Sort[i]

        # 获取插入值前一个值
        j = i - 1

        while j >= 0 and key < Wait_Sort[j]:
            Wait_Sort[j + 1] = Wait_Sort[j]
            j -= 1

        Wait_Sort[j + 1] = key

if __name__ == '__main__':
    Ins_sort(Wait_Sort)
    print(Wait_Sort)