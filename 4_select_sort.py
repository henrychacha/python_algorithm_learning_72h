import random

# two parts, deprecated
# - use more than one list to store data
# - min and max functions are not recommended
def select_sort(li):
    newLi = []
    for i in range(len(li)):
        max_val = min(li)
        newLi.append(max_val)
        li.remove(max_val)
    return newLi


li1 = [1, 3, 52, 6, 3, 5, 1, 56, 7, 2]
# print(select_sort(li1))


# optimize
def select_sort2(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[i] > li[i+j+1]:
                li[i], li[i+j+1] = li[i+j+1], li[i]
    return li

# print(select_sort2(li1))

# optimize 2
def select_sort3(li):

