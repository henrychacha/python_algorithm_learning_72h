# compare time spending of linear_search with binary_search
from util_cal_time import * 

# O(logn) 
## log2(64) = 6; O(log2(n)) or O(log(n))
n = 64
while n > 1:
    print(n)
    n = n //2


# 递归 recursion 
def func3(x):
    if x>0:
        print(x)
        func3(x-1)

def func4(x):
    if x>0:
        func4(x-1)
        print(x)
func3(3)
func4(3)


# linear search
@cal_time
def linear_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
    return None
print(linear_search([1,5,2,51,5],2))


# binary search 二分查找
@cal_time
def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right: # 候选区有值
        mid = (left + right) //2 
        if li[mid] == val:
            return mid
        elif li[mid] < val: # dai查找的值在mid右侧
            left = mid + 1
        else:
            right = mid - 1 # dai查找的值在mid左侧
    return None
print(binary_search([1,5,2,2,12,523,234,5234,12,526,7,13],12))

li = list(range(100000))
linear_search(li,3890)
binary_search(li,3890)

