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


def fib3(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


# 输出 9*9 乘法口诀表,注意最后的逗号功能
def MulTable():
    for i in range(1, 10):
        print
        for j in range(1, i + 1):
            print('%d*%d=%d' % (i, j, i * j)),


import time


def TimeSleep(n):
    myDs = {1: 'a', 2: 'b'}
    for key, value in dict.items(myDs):
        print key, value
        # 格式化当前时间，注意format中大小写输出有区别
        print(time.strftime('%Y-%M-%d %H:%M:%S', time.localtime(time.time())))
        time.sleep(n)  # 暂停n秒
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


def RabbitTest():
    f1 = 1
    f2 = 1
    for i in range(1, 22):
        print('%12ld %12ld' % (f1, f2)),
        if (i % 3 == 0):
            print('')
        f1 = f1 + f2
        f2 = f1 + f2


'''
判断101-200之间有多少个素数，并输出所有素数
分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
'''

from math import sqrt
from sys import stdout


def IsPrime(m, n):
    h = 0
    leap = 1
    for num in range(m, n + 1):
        k = int(sqrt(num + 1))
        for i in range(2, k + 1):
            if num % i == 0:
                leap = 0
                break
        if leap == 1:
            print('%-4d' % num)
            h += 1
        leap = 1
    print('the total is %d' % h)


'''
打印出所有的"水仙花数"
"水仙花数"指一个三位数，其各位数字立方和等于该数本身。
'''


def GetFlowerNum():
    for i in range(100, 1000):
        b = i / 100
        s = i / 10 % 10
        g = i % 10
        if i == (b ** 3 + s ** 3 + g ** 3):
            print(i)


# 将一个正整数分解质因数
def ReduceNum(n):
    print '{} ='.format(n),
    if not isinstance(n, int) or n <= 0:
        print('请输入一个正确的数字！')
        exit(0)
    elif n in [1]:
        print('{}'.format(n))
    while n not in [1]:  # 循环保证递归
        for index in xrange(2, n + 1):
            if n % index == 0:
                n /= index  # n等于n/index
                if n == 1:
                    print index
                else:  # index 一定是素数
                    print '{} *'.format(index),
                break
