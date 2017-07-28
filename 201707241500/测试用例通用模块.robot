*** Settings ***
Library           Selenium2Library

*** Keywords ***
等待时间
    [Arguments]    ${time}
    Sleep    ${time}
