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


# 一个整数加上100后是一个完全平方数，再加168又是一个完全平方数，请问该数是多少？
def GetAnswer():
    for i in range(1, 85):
        if 168 % i == 0:
            j = 168 / i
        if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
            m = (i + j) / 2
            n = (i - j) / 2
            x = n * n - 100
            print(x)


'''
输入*年*月*日，判断这一天是这一年的第几天？
分析：以3月5日为例，先把前两月的加起来，再加上5天就是本年的第几天，特殊情况下闰年且输入月份大于2时需考虑多加一天
'''


def CountDays():
    year = int(raw_input('year:\n'))
    month = int(raw_input('month:\n'))
    day = int(raw_input('day:\n'))
    months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
    sum = 0
    if 0 < month <= 12:
        sum = months[month - 1]
    else:
        print('data error')
    sum += day
    leap = 0
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        leap = 1
    if (leap == 1) and (month > 2):
        sum += 1
    print('it is the %dth day...' % sum)


# 斐波那契数列
def fib1(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def fib2(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fib2(n - 1) + fib2(n - 2)


if __name__ == '__main__':
    print fib2(3)
