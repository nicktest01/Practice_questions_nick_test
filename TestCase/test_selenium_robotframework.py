# -*- coding:utf-8 -*-
*** Settings ***
Settings test demo

*** Variable ***
URL test demo

*** Test Cases ***    
Open Google and Search Nicktest
    show robot test

*** Keywords ***    
show robot test
    Open Browser    https://www.google.com    chrome
    Input Text      name    # 找到搜尋框並輸入 "nicktest"
    Press Keys      name    # 模擬按下 Enter 鍵
    Close Browser