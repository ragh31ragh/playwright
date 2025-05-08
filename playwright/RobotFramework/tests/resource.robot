*** Settings ***
Documentation     To validate the Login form
Library    SeleniumLibrary

*** Variables ***
${username}        rahulshettyacademy
${InvalidPassword}    12232323
${validPassword}    learning
${url}             https://rahulshettyacademy.com/loginpagePractise/
*** Keywords ***
Open the browser with Mortgage Payment URL
    Create Webdriver    Chrome
    Go To    ${url}

Close Browser Session
    Close Browser