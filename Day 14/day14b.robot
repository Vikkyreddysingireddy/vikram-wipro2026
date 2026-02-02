*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}      https://testautomationpractice.blogspot.com/
${BROWSER}  chrome

*** Test Cases ***
Interact With Web Elements
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible    id=name    10s
    Input Text    id=name    Vikkyreddy
    ${text}=    Get Value    id=name
    Run Keyword If    '${text}' != ''    Log To Console    Text box entered successfully
    Click Element    id=male
    Click Element    id=sunday
    Select From List By Label    id=country    India
    Sleep    3s
    Close Browser