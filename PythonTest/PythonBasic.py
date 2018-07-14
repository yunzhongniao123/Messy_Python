# -*- coding:utf-8 -*-

# 1到4能组成多少个互不相同且不重复数字的三位数？分别是？
def NumCombination():
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if (i != j) and (i != k) and (j != k):
                    print(i, j, k)


def GetBonus():
    i = int(raw_input('净利润：'))
    arr = [1000000, 600000, 400000, 200000, 100000, 0]
    rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    r = 0
    for idx in range(0, 6):
        if i > arr[idx]:
            r += (i - arr[idx]) * rat[idx]
            print (i - arr[idx]) * rat[idx]
            i = arr[idx]
    print(r)


if __name__ == '__main__':
    GetBonus()
