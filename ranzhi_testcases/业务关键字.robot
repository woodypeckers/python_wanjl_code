*** Settings ***
Resource          业务关键字.robot

*** Keywords ***
前台登陆
    [Arguments]    ${base_url}    ${username}    ${password}    ${title}
    打开浏览器前台    ${base_url}
    sleep    3
    输入用户名    ${username}
    sleep    3
    输入密码    ${password}
    sleep    3
    验证确认登陆    ${title}

退出登陆
    Unselect Frame
    sleep    3
    选择用户
    sleep    3
    选择退出
    sleep    3

关闭浏览器
    Unselect Frame
    sleep    3
    关闭浏览器

关闭所有浏览器
    Unselect Frame
    sleep    3
    关闭当前所有浏览器

管理员前台登陆
    前台登陆    http://localhost/ranzhi/www/    admin    123456    然之
