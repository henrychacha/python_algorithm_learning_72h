# 2022-11-21 Mon 14:04
# 漢諾塔問題

def hanoi(n,a,b,c):
    # a means beginning disk
    # b means intermediate disk
    # c means the disk where all plates should end up

    if n>0:
        # step1: move (n-1) plates from a to b, which will utilize c in the procedures.
        hanoi(n-1,a,c,b)
        # step2: move the nth plate from a to c
        print("move %s to %s" % (a,c))
        # step3: move the n-1 plates from b to c, which will utilize a in the procedures.
        hanoi(n-1,b,a,c)

hanoi(3,"A","B","C")