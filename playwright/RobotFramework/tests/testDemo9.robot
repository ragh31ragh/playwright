*** Settings ***
Documentation     To validate the Login form
Library    SeleniumLibrary


*** Test Cases ***
Validate Unsuccessful Login
    Open the browser with Mortgage Payment URL

*** Keywords ***
Open the browser with Mortgage Payment URL
    #Create Webdriver    Chrome
    Create Webdriver    Edge
    Go To    https://rahulshettyacademy.com/loginpagePractise/
    Sleep    3
