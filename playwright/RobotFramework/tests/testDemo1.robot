*** Settings ***
Documentation     To validate the Login form
Library    SeleniumLibrary
Test Teardown    Close Browser

*** Variables ***
${Error_Message_Login}    css:.alert-danger

*** Test Cases ***
Validate Unsuccessful Login
    Open the browser with Mortgage Payment URL
    Fill the Login form
    wait until it checks display error message
    verify error message is corrected

*** Keywords ***
Open the browser with Mortgage Payment URL
    Create Webdriver    Chrome
    Go To    https://rahulshettyacademy.com/loginpagePractise/

Fill the login form
    Input Text    id:username    rahulshettyacademy
    Input Password    id:password    12232323
    Click Button    signInBtn

wait until it checks display error message
    Wait Until Element Is Visible    ${Error_Message_Login}

verify error message is corrected
    ${result}=    Get Text    ${Error_Message_Login}
    Should Be Equal As Strings    ${result}    Incorrect username/password.
    Element Text Should Be    ${Error_Message_Login}    Incorrect username/password.

Close Browser Session