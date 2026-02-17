*** Settings ***
Resource    resources.robot
Suite Setup    Create API Session

*** Test Cases ***

User Registration
    ${body}=    Create Dictionary
    ...    name=Chintu
    ...    email=Chintu@gmail.com
    ...    password=1212121212

    ${res}=    POST On Session    foodie
    ...    url=/api/v1/users/register
    ...    json=${body}

    Status Should Be    201    ${res}


Search Restaurants
    ${res}=    GET On Session    foodie
    ...    url=/api/v1/restaurants/search
    ...    params=name=Sattibabu

    Status Should Be    200    ${res}