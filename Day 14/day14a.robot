*** Settings ***
Suite Setup       Log To Console    === Suite Setup: Before All Test Cases ===
Suite Teardown    Log To Console    === Suite Teardown: After All Test Cases ===
Test Setup        Log To Console    --- Test Setup: Before Each Test ---
Test Teardown     Log To Console    --- Test Teardown: After Each Test ---

*** Test Cases ***
Smoke Test Case
    [Tags]    smoke
    Log To Console    Executing Smoke Test Case
    Should Be Equal    10    10

Regression Test Case
    [Tags]    regression
    Log To Console    Executing Regression Test Case
    Should Be True    ${True}