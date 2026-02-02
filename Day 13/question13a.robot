* Settings *
Library    SeleniumLibrary

* Variables *
${BROWSER}    chrome
${URL}        https://www.google.com
${TITLE}      Google

* Test Cases *
Open Browser And Verify Title
    [Documentation]    Opens browser, navigates to URL, verifies title, captures screenshot, closes browser

    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    Title Should Be    ${TITLE}

    Capture Page Screenshot

    Close Browser