*** Settings ***
Resource    resources.robot
Suite Setup    Create API Session

*** Test Cases ***

Register Restaurant
    ${body}=    Create Dictionary
    ...    name=Robot Hub
    ...    category=Veg
    ...    location=Hyderabad
    ...    contact=99999

    ${res}=    POST On Session    foodie
    ...    url=/api/v1/restaurants
    ...    json=${body}

    Status Should Be    201    ${res}


Update Restaurant
    ${body}=    Create Dictionary    location=Bangalore

    ${res}=    PUT On Session    foodie
    ...    url=/api/v1/restaurants/1
    ...    json=${body}

    Status Should Be    200    ${res}


Disable Restaurant
    ${res}=    PUT On Session    foodie
    ...    url=/api/v1/restaurants/1/disable

    Status Should Be    200    ${res}


View Restaurant Profile
    ${res}=    GET On Session    foodie
    ...    url=/api/v1/restaurants/1

    Status Should Be    200    ${res}