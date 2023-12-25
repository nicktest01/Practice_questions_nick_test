# -*- coding:utf-8 -*-
"""
國泰補習班中，有五位學生期中考的成績分別為[53, 64, 75, 19, 92]，但是老師在輸入成績的時候看反了，
把五位學生的成績改成了[35, 46, 57, 91, 29]，
請用一個函數來將學生的成績修正。

輸入: [35, 46, 57, 91, 29]
輸出: [53, 64, 75, 19, 92]

"""
    #修正成績       #錯誤成績
def Correct_grades(wrong_grades):
    Correct_grades = [53, 64, 75, 19, 92]
    
    for i in range(len(Correct_grades)):
        Correct_grades[i] = wrong_grades[i]
    
    return Correct_grades

# 錯誤的學生成績
wrong_grades = [35, 46, 57, 91, 29]

# 使用函數修正成績
Corrected_results = Correct_grades(wrong_grades)

print("Correction_result:", Corrected_results )
