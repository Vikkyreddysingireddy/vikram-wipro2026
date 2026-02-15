*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    http://localhost:5001

*** Keywords ***
Open Browser To App
    Open Browser    ${URL}    chrome
    Maximize Browser Window
    Wait Until Page Contains    Patient Registration    10s

Fill Patient Form
    Input Text    name=name    Ram
    Input Text    name=age     30
    Select From List By Label    name=gender    Male
    Input Text    name=contact    9999999999
    Input Text    name=disease    Fever
    Input Text    name=doctor     Dr Hari
    Click Button    Submit

Close Browser Session
    Close All Browsers
