restaurants = {}
dishes = {}
users = {}
orders = {}
ratings = {}

restaurant_id_counter = 1
dish_id_counter = 1
user_id_counter = 1
order_id_counter = 1
rating_id_counter = 1

def reset_storage():
    global restaurants, dishes, users, orders, ratings
    global restaurant_id_counter, dish_id_counter
    global user_id_counter, order_id_counter, rating_id_counter

    restaurants.clear()
    dishes.clear()
    users.clear()
    orders.clear()
    ratings.clear()

    restaurant_id_counter = 1
    dish_id_counter = 1
    user_id_counter = 1
    order_id_counter = 1
    rating_id_counter = 1