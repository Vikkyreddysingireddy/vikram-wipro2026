*** Settings ***
Resource    resources.robot
Suite Setup    Open Browser To App
Suite Teardown    Close Browser Session

*** Test Cases ***
Register Patient
    Fill Patient Form
