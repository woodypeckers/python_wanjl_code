*** Settings ***
Library           Selenium2Library

*** Keywords ***
输入用户名
    [Arguments]    ${username}
    Input Text    name=account    ${username}

输入密码
    [Arguments]    ${password}
    Input Password    id=password    ${password}

打开浏览器前台
    [Arguments]    ${base_url}
    Open Browser    ${base_url}    ff

验证确认登陆
    [Arguments]    ${title}
    Click Button    id=submit
    Page Should Contain    ${title}

选择用户
    Click Button    id=start

选择退出
    Click Link    xpath=.//*[@id='startMenu']/li[10]/a

关闭浏览器
    Close Browser

关闭当前所有浏览器
    Close All Browsers
