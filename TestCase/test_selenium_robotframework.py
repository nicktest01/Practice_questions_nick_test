# -*- coding:utf-8 -*-
*** Settings ***
Settings test demo

*** Variable ***
${MESSAGE}    Hello, world!

*** Test Cases ***    
Open Google and Search Nicktest
    [Documentation]    Example test
    Log    ${MESSAGE}
    show robot test

*** Keywords ***    
show robot test
    Open Browser    google.com    Browser
    Input Text      name    # 找到搜尋框並輸入 "nicktest"
    Press Keys      name    # 模擬按下 Enter 鍵
    Close Browser