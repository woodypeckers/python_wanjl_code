*** Settings ***
Library           Selenium2Library
Resource          登陆通用模块.robot
Resource          测试用例通用模块.robot
Library           String

*** Variables ***
${base_url}       http://localhost/ranzhi/www
${username}       admin
${password}       123456
${title}          然之协同

*** Test Cases ***
ranzhi_addcustomer
    [Setup]    前台登陆
    Click Button    xpath=/html/body/div[1]/div[1]/div[1]/ul[1]/li[2]/button    #点击左侧边栏客户管理(xpath不唯一，带绝对路径)
    sleep    3
    Select Frame    id=iframe-1
    sleep    3
    Click link    xpath=/html/body/nav[1]/div[2]/ul/li[4]/a    #点击客户管理
    sleep    3
    @{list}    List Windows
    Log    list[0]    debug
    sleep    3
    Click link    xpath=/html/body/nav/div[2]/ul/li[4]/a    #点击客户
    sleep    3
    Click Link    xpath=.//*[@id='menuActions']/a    #添加客户
    sleep    3
    Input Text    id=name    zhangsan
    Input Text    id=contact    lisi
    Input Text    id=phone    12345678910
    Input Text    id=email    123456@qq.com
    Input Text    id=qq    123456
    Select From List By Value    id=type    national
    Select From List By Index    id=size    1
    Select From List By Value    id=status    signed
    Select From List By Value    id=level    C
    Input Text    id=intension    产品很好
    Click Button    id=submit

ranzhi_addproduct
    [Setup]    前台登陆
    Click Button    xpath=/html/body/div[1]/div[1]/div[1]/ul[1]/li[2]/button    #点击左侧边栏客户管理(xpath不唯一，带绝对路径)
    sleep    3
    Select Frame    name=iframe-1
    Click Element    xpath=.//*[@id='mainNavbar']/div[2]/ul/li[7]/a    #点击产品
    sleep    3
    Click Element    xpath=.//*[@id='menuActions']/a    #添加产品
    sleep    3
    Input Text    name    product1
    Input Text    code    product1
    #Select From List By Value    line    default
    Select From List By Value    type    service
    Select From List By Label    status    正常
    sleep    3
    Click Button    submit
    [Teardown]    清除添加产品

ranzhi_addcontract
    [Setup]    前台登陆
    Click Button    xpath=/html/body/div[1]/div[1]/div[1]/ul[1]/li[2]/button    #点击左侧边栏客户管理(xpath不唯一，带绝对路径)
    sleep    3
    Select Frame    name=iframe-1
    sleep    3
    Click link    xpath=.//*[@id='mainNavbar']/div[2]/ul/li[3]/a    #点击合同
    sleep    3
    ${list2}    List Windows
    log    ${list2}    debug
    sleep    3
    Click link    xpath=.//*[@id='menuActions']/a    #创建合同
    sleep    3
    #Select From List By Label    xpath=.//*[@id='customer_chosen']/a/div/b    zhangsan    #有问题
    Input Text    id=name    contract1
    Input Text    id=code    1f3d
    Select From List By Value    id=currency    rmb
    Input Text    id=amount    100000
    #Select From List By Value    id=contact    \    #有问题
    #Input Text    xpath=.//*[@id='signedBy_chosen']/a    admin    #有问题
    Input Text    id=signedDate    2012-1-1
    Input Text    id=begin    2009-1-1
    Input Text    id=end    2099-1-1
    Input Text    xpath=.//*[@id='handlers_chosen']/ul/li/input    admin
    Click Element    id=submit    \    #有问题

*** Keywords ***
前台登陆
    打开浏览器前台    ${base_url}
    sleep    3
    输入用户名    ${username}
    sleep    3
    输入密码    ${password}
    sleep    3
    验证确认登陆    ${title}
    sleep    3

清除添加产品
    Click Element    xpath=.//*[@id='productList']/tbody/tr/td[8]/a[2]
    sleep    3
    Dismiss Alert
