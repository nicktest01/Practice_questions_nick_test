# -*- coding:utf-8 -*-
# 開啟Google首頁
driver = webdriver.Chrome()
driver.get("https://www.google.com")

# 找到搜尋框，輸入文字並執行搜尋
search_box = driver.find_element_by_name()
search_box.send_keys("nicktest")
search_box.send_keys(Keys.RETURN)

# 瀏覽器視窗等待10秒
driver.implicitly_wait(10)

# 關閉瀏覽器
driver.quit()