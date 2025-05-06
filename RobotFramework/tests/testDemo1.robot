*** Settings ***
Documentation     To validate the Login form
Library    SeleniumLibrary

*** Test Cases ***
Validate Unsuccessful Login
    Open the browser with Mortgage Payment URL
    Fill the Login form
    #wait until it checks display error message
    #verify error message is corrected

*** Keywords ***
Open the browser with Mortgage Payment URL
    Create Webdriver    Chrome
    Go To    https://rahulshettyacademy.com/loginpagePractise/

Fill the login form
    Input Text    id:username    rahulshettyacademy
    Input Password    id:password    12232323
    Click Button    signInBtn