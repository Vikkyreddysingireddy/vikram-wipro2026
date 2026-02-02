*** Settings ***
Library    BuiltIn

*** Variables ***
${TRUE}     True
${FALSE}    False

*** Keywords ***
Validate Login
    [Arguments]    ${username}    ${password}
    Run Keyword If    '${username}' == 'admin' and '${password}' == 'admin123'
    ...    Return From Keyword    ${TRUE}
    Return From Keyword    ${FALSE}

*** Test Cases ***
Login Test 1
    ${status}=    Validate Login    admin    admin123
    Should Be Equal    ${status}    ${TRUE}

Login Test 2
    ${status}=    Validate Login    admin    wrongpass
    Should Be Equal    ${status}    ${FALSE}

Login Test 3
    ${status}=    Validate Login    user    admin123
    Should Be Equal    ${status}    ${FALSE}

Login Test 4
    ${status}=    Validate Login    admin    admin123
    Should Be Equal    ${status}    ${TRUE}