*** Settings ***
Resource    resources.robot
Suite Setup    Create API Session

*** Test Cases ***

Approve Restaurant
    ${res}=    PUT On Session    foodie
    ...    url=/api/v1/admin/restaurants/1/approve

    Status Should Be    200    ${res}


Admin Disable Restaurant
    ${res}=    PUT On Session    foodie
    ...    url=/api/v1/admin/restaurants/1/disable

    Status Should Be    200    ${res}


View Feedback
    ${res}=    GET On Session    foodie
    ...    url=/api/v1/admin/feedback

    Status Should Be    200    ${res}


View Order Status
    ${res}=    GET On Session    foodie
    ...    url=/api/v1/admin/orders

    Status Should Be    200    ${res}