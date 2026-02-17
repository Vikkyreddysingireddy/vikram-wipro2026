*** Settings ***
Resource    resources.robot
Suite Setup    Create API Session

*** Test Cases ***

Place Order
    ${body}=    Create Dictionary
    ...    user_id=1
    ...    restaurant_id=1
    ...    dish=Pizza

    ${res}=    POST On Session    foodie
    ...    url=/api/v1/orders
    ...    json=${body}

    Status Should Be    201    ${res}


Give Rating
    ${body}=    Create Dictionary
    ...    order_id=1
    ...    rating=5
    ...    comment=Excellent Taste

    ${res}=    POST On Session    foodie
    ...    url=/api/v1/ratings
    ...    json=${body}

    Status Should Be    201    ${res}


View Orders By Restaurant
    ${res}=    GET On Session    foodie
    ...    url=/api/v1/restaurants/1/orders

    Status Should Be    200    ${res}


View Orders By User
    ${res}=    GET On Session    foodie
    ...    url=/api/v1/users/1/orders

    Status Should Be    200    ${res}