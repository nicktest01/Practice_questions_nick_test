# -*- coding:utf-8 -*-
"""
列印出 1 ~ n 的每一個整數，但是
當該整數可以被3整除時，印出 Q 來代替原本要印出的數;
當該整數可以被5整除時，印出 A 來代替原本要印出的數;
當該整數可以被 5 及 3 整除時，印出 QA 來代替原本  
"""

def print_QA(n):
    for i in range(1, n + 1):
        # 先假設這次不用輸出字母
        nicktest_by_3 = (i % 3 == 0)
        nicktest_by_5 = (i % 5 == 0)
        
        # 判斷整除情況
        if nicktest_by_3 and nicktest_by_5:
            print("QA")  # 同時被3和5整除
        elif nicktest_by_3:
            print("Q")   # 只被3整除
        elif nicktest_by_5:
            print("A")   # 只被5整除
        else:
            print(i)     # 兩者都不整除，印數字本身
