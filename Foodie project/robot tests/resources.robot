*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    http://127.0.0.1:2700

*** Keywords ***
Create API Session
    Create Session    foodie    ${BASE_URL}