import random

import Time_count

# 无标记冒泡
@ Time_count.timecount
def bubble_sort1(l):
    i = 0
    while i < len(l) - 1:
        j = len(l) - 1
        while j > i:
            if l[j - 1] > l[j]:
                l[j], l[j - 1] = l[j - 1], l[j]
            j = j - 1
        i = i + 1

# 有标记冒泡
@ Time_count.timecount
def bubble_sort2(l):
    i = 0
    while i < len(l) - 1:
        j = len(l) - 1
        tag = True
        while j > i:
            if l[j - 1] > l[j]:
                tag = False
                l[j], l[j - 1] = l[j - 1], l[j]
            j = j - 1
        if tag:
            break
        i = i + 1

# 双端冒泡
@ Time_count.timecount
def double_bubble_sort(l):
    i = 0
    j = len(l) - 1
    while i<j:
        tag = True
        temp = j
        while temp > i:
            if l[temp - 1] > l[temp]:
                tag = False
                l[temp], l[temp - 1] = l[temp - 1], l[temp]
            temp = temp - 1
        i += 1
        if tag:
            break
        temp = i
        while temp < j:
            if l[temp + 1] < l[temp]:
                tag = False
                l[temp], l[temp + 1] = l[temp + 1], l[temp]
            temp = temp + 1
        j -= 1
        if tag:
            break

# 插入排序
@ Time_count.timecount
def insert_sort1(l):
    i1 = 1
    n = len(l)
    while i1 < n:
        i2 = 0
        temp = l[i1]
        while i1 > i2:
            if temp < l[i2]:
                l.insert(i2, temp)
                l.pop(i1 + 1)
                break
            i2 = i2 + 1
        i1 = i1 + 1

# 插入排序（折半）
@ Time_count.timecount
def insert_sort2(l):
    i = 1
    n = len(l)
    while i < n:
        j = 0
        k = i - 1
        temp = l[i]
        while j <= k:
            mid = int((j + k) / 2)
            if temp < l[mid]:
                k = mid - 1
            else:
                j = mid + 1
        if l[j] < temp:
            l.insert(j + 1, temp)
        else:
            l.insert(j, temp)
        i = i + 1
        l.pop(i)

# 希尔排序
@ Time_count.timecount
def shell_sort(l):
    i = 1
    n = len(l)
    while i < n / 3:
        i = i * 3 + 1  # 1,4,13......

    while i >= 1:
        i1 = i
        while i1 < n:
            i2 = 0
            temp = l[i1]
            while i1 > i2:
                if temp < l[i2]:
                    l.insert(i2, temp)
                    l.pop(i1 + 1)
                    break
                i2 = i2 + i
            i1 = i1 + i
        i = int(i / 3)

# 快速排序
@ Time_count.timecount
def quick_sort(l):
    qsort(l, 0, len(l) - 1)

def qsort(l, lift, right):
    if right < lift:
        return
    m = partition(l, lift, right)
    qsort(l, lift, m - 1)
    qsort(l, m + 1, right)

def partition(l, lift, right):
    key = l[lift]
    while lift < right:
        while lift < right and l[right] >= key:
            right = right - 1
        l[lift] = l[right]
        while lift < right and l[lift] <= key:
            lift = lift + 1
        l[right] = l[lift]
    l[right] = key
    return lift

# 划分奇偶
def select(l):
    i = 0
    n = len(l) - 1
    while i < n:
        while l[i] % 2 == 1 and i < n:
            i += 1
        while l[n] % 2 == 0 and i < n:
            n -= 1
        l[i], l[n] = l[n], l[i]


if __name__ == '__main__':
    l = []
    for i in range(0,10):
        l.append(random.randint(0,10))
    print(l)
    # bubble_sort1(l)
    # bubble_sort2(l)
    # double_bubble_sort(l)
    # insert_sort1(l)
    # insert_sort2(l)
    # shell_sort(l)
    # quick_sort(l)
    select(l)
    print(l)