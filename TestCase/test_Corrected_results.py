# -*- coding:utf-8 -*-

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