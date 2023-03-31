import random 

def Bubble_sort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]

li = [random.randint(0,10000) for i in range(1000)]
print(li)
# Bubble_sort(list(range(1000)))
Bubble_sort(li)
print(li)

# optmize 
# 如果冒泡排序中的一趟排序没有发生交换，则说明列表已经有序，可以直接结束算法。
def Bubble_sort(li):
    for i in range(len(li)-1):
        temp = False
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                temp = True
        if not temp: 
            return
