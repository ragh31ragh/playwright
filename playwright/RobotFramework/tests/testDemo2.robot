*** Settings ***
Documentation     To validate the Login form
Library    SeleniumLibrary
Test Teardown    Close Browser
Documentation     To validate the Login form__TestSuite1
Library    SeleniumLibrary
Library    Collections
Test Setup        Open the browser with Mortgage Payment URL
#Test Teardown    Close Browser Session
Resource         resource.robot

*** Variables ***
${Error_Message_Login}    css:.alert-danger
${shop_page_load}    css:.nav-link

*** Test Cases ***
Validate Unsuccessful Login
    Fill the Login form    ${username}    ${InvalidPassword}
    wait for element to be visible    ${Error_Message_Login}
    verify error message is corrected

Verify Cards display in shopping Page
    Fill the Login form    ${username}    ${validPassword}
    wait for element to be visible    ${shop_page_load}
    Verify card titles in the shop page
    Select the card    Blackberry

Select the form and Navigate to Child Window
    Fill the login details and select the form
*** Keywords ***


Fill the login form
    [Arguments]    ${username}    ${password}
    Input Text    id:username    ${username}
    Input Password    id:password    ${password}
    Click Button    signInBtn



verify error message is corrected
    ${result}=    Get Text    ${Error_Message_Login}
    Should Be Equal As Strings    ${result}    Incorrect username/password.
    Element Text Should Be    ${Error_Message_Login}    Incorrect username/password.

wait for element to be visible
    [Arguments]    ${element}
    Wait Until Element Is Visible    ${element}

Verify card titles in the shop page
    @{expectedList} =    Create List    iphone X    Samsung Note 8     Nokia Edge    Blackberry
    @{elements} =    Get Webelements    css:.card-title
    @{actualList} =    Create List
    FOR    ${ele}    IN    @{elements}
        Log    ${ele.text}
        Append To List    ${actualList}    ${ele.text}
    END
    Lists Should Be Equal     ${expectedList}    ${actualList}

Select the card
    [Arguments]    ${cardname}
    ${index} =    Set Variable    1
    @{elements} =    Get Webelements    css:.card-title
    FOR    ${ele}    IN    @{elements}
        Exit For Loop If    '${cardname}' == '${ele.text}'
            ${index}=    Evaluate    ${index} + 1
            Log    ${ele.text}
    END
    Click Button    xpath:(//*[@class='card-footer']/button)[${index}]

Fill the login details and select the form
    Input Text    id:username    rahulshettyacademy
    Input Password    id:password    learning
    Click Element    xpath://input[@value='user']
    Wait Until Element Is Visible    id:okayBtn
    Select From List By Value    xpath://select[@class='form-control']    teach
    Select Checkbox    terms
    Checkbox Should Be Selected    terms