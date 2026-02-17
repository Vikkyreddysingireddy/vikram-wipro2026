*** Settings ***
Resource    resources.robot
Suite Setup    Create API Session

*** Variables ***
${RID}    None
${DID}    None

*** Test Cases ***

Create Restaurant For Dish Tests
    ${body}=    Create Dictionary
    ...    name=Sattibabu Biryani
    ...    category=Veg/Non - Veg
    ...    location=Hyderabad
    ...    contact=11223344556

    ${res}=    POST On Session    foodie
    ...    url=/api/v1/restaurants
    ...    json=${body}

    Status Should Be    201    ${res}
    ${json}=    Set Variable    ${res.json()}
    Set Suite Variable    ${RID}    ${json["id"]}


Add Dish
    ${body}=    Create Dictionary    name=Pizza    price=200

    ${res}=    POST On Session    foodie
    ...    url=/api/v1/restaurants/${RID}/dishes
    ...    json=${body}

    Status Should Be    201    ${res}
    ${json}=    Set Variable    ${res.json()}
    Set Suite Variable    ${DID}    ${json["id"]}


Update Dish
    ${body}=    Create Dictionary    price=250

    ${res}=    PUT On Session    foodie
    ...    url=/api/v1/restaurants/${RID}/dishes/${DID}
    ...    json=${body}

    Status Should Be    200    ${res}


Enable Disable Dish
    ${body}=    Create Dictionary    enabled=${False}

    ${res}=    PUT On Session    foodie
    ...    url=/api/v1/restaurants/${RID}/dishes/${DID}/status
    ...    json=${body}

    Status Should Be    200    ${res}


Delete Dish
    ${res}=    DELETE On Session    foodie
    ...    url=/api/v1/restaurants/${RID}/dishes/${DID}

    Status Should Be    200    ${res}