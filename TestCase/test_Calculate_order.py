# -*- coding:utf-8 -*-
"""
某部門今天舉辦團康活動，有n個人圍成一圈，順序排號。從第一個人開始報數（從1到3報數），凡報到3的人退出圈子。
請利用一段程式計算出，最後留下的那位同事，是所有同事裡面的第幾順位?
"""
#計算同事順位
def last_person_position(n):
    circle = list(range(1, n + 1))  # 建立圍成一圈的同事列表
    idx = 0

    while len(circle) > 1:
        idx = (idx + 2) % len(circle)  # 每次報數3的人退出，更新索引位置
        circle.pop(idx)
    return circle[0]

# 輸入n值，並計算最後留下的同事是第幾順位
n = int(input("請輸入n值（0-100）："))
result = last_person_position(n)
print(f"最後留下的同事是第 {result} 順位")
