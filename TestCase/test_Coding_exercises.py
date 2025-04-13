#第一題
#( C   ) 1. 請問以下程式執行後，r = ?
#	def p(name, age):
#	    print(f’姓名: {name}, 年齡: {age}’)
#	    return
#	r = p(age = 50, name = ‘Ruby’)
#	(A)	r = Ruby, 50
#	(B)	r = 50, Ruby
#	(C)	無正確答案可選

def p(name, age):
	    print(f’姓名: {name}, 年齡: {age}’)
	    return
	r = p(age = 50, name = ‘Ruby’)
       
#這段 Python 代碼在 VS Code 上執行時可能會遇到語法錯誤，
#主要是因為使用了錯誤的單引號（’ 和 ‘），這些是全形單引號，Python 需要標準的半形單引號 (') 或雙引號 (")。修正後的代碼如下：
												  
def p(name, age):
    print(f'姓名: {name}, 年齡: {age}')
    return

r = p(age=50, name='Ruby')

Nick :程式碼不能用’執行,姓名前與age後方需改為 ‘ 符號 才能執行 

#第二題
#(  B  ) 2. lis = [1, 2, 3, 4] 如何讓 lis != [1, 2, 4]
#	(A)	lis.pop(2)
#	(B)	lis.remove(2)
#	(C)	del lis[2]
#	(D)	無正確答案可選

lis = [1, 2, 3, 4]
del lis[2]
#lis.pop(2)
print(lis)

lis = [1, 2, 3, 4]
lis.pop(2)
print(lis)

lis = [1, 2, 3, 4]
lis.remove(2)
print(lis)

Nick :
lis.pop(2)與del lis[2],根據 ()要求索引移除元素
結果會是[1, 2, 4]
若是要不等於[1, 2, 4],則選B 結果會是
[1, 3, 4]

#第三題
#(  B  ) 3. lis = [5, 20, 0] 如何讓 lis = [0, 5, 20]
#	(A)	lis.reverse()
#	(B)	lis.sort()
#	(C)	lis.sort(reverse=True)
#	(D)	lis.sort(reverse=False)
#	(E)	無正確答案可選

Nick:
everse() 會反轉列表的順序，結果會變成 [0, 20, 5]
sort() 會將列表按照升序排列，結果會變成 [0, 5, 20]
sort(reverse=True) 會將列表按照降序排列，結果會變成 [20, 5, 0]

#第四題
#(  C  ) 4. lis = [5, 20,  0] 如何讓 lis = [20, 5, 0]
#	(A)	lis.reverse()
#	(B)	lis.sort()
#	(C)	lis.sort(reverse=True)
#	(D)	lis.sort(reverse=False)
#	(E)	無正確答案可選
Nick:同上題解析,這邊選C

題目
employee_id   name    age   department_id
1             Alice   25    1
2             Bob     30    2
3             Carol   NULL  NULL
4             Dave    40    1
5             Eve     22    2

#(  B  ) 6. 請選擇查詢員工年齡時的正確描述
#	SELECT COUNT(*), COUNT(age)
#	FROM employees WHERE age > 18
#	(A) 兩者結果相同
#	(B) COUNT(*) 包含 null，另一個則排除
#	(C) COUNT(age) 可能大於 COUNT(*)
#	(D) 無正確答案可選

Nick :
OUNT(*) 會計算指定欄位的數量,包含Null
COUNT(age) 會計算指定欄位非NULL的數量

#(  A  ) 7. 請選擇以下 LEFT JOIN 查詢結果筆數
#	SELECT e.name, d.department_name
#	FROM employees e
#	LEFT JOIN departments d
#	ON e.department_id = d.department_id
#	(A) 最多 5 筆，LEFT JOIN 會保留全部
#	(B) 最多 4 筆，排除 department_id = null
#	(C) 最多 3 筆，因為 JOIN 會去除重複
#	(D) 無正確答案可選

Nick:
這邊語法要搜尋name,這點沒問題,問題出在表格中並沒有department_name的欄位
那結果就是LEFT JOIN 會保留所有查詢紀錄結果
如果department_name有塞對應部門名稱
則搜出來結果就會有對應顯示
Name   department_name
#Alice       NULL
#Bob         NULL
#Carol       NULL
#Dave        NULL
#Eve         NULL


#( B   ) 8. 請選擇篩選 age 排除 null 的正確語法
#	(A) WHERE age != NULL
#	(B) WHERE age IS NOT NULL
#	(C) WHERE age IS DISTINCT FROM NULL
#	(D) 無正確答案可選

Nick:
C的選項也可以用,但我對PostgreSQL不熟
所以我選B

#第九題
#查詢最年長的 3 位員工

Nick:
SELECT * FROM employees
WHERE age IS NOT NULL
ORDER BY age DESC
LIMIT 3;

如果我想要看年齡從小到大排序,
並排除年齡為 22的Eva 我會這樣寫
SELECT * FROM employees 
WHERE age IS NOT NULL AND age != 22 
ORDER BY age ASC 
LIMIT 3;

#第十題
#查詢不同的 department_id 有幾個
Nick:由於題目沒有給資料表名稱,我假設資料表名稱叫做nicktest
SELECT COUNT(DISTINCT department_id) FROM nicktest;          
查詢結果為2 兩個不同的department_id
排除NULL