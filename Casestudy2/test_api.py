import requests

BASE_URL = "http://127.0.0.1:5000"

def test_get_movies():
    response = requests.get(f"{BASE_URL}/api/movies")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_add_movie():
    new_movie = {
        "id": 103,
        "movie_name": "Jumanji",
        "language": "English",
        "duration": "1h 44m",
        "price": 350
    }
    response = requests.post(f"{BASE_URL}/api/movies", json=new_movie)
    assert response.status_code == 201
    assert response.json()["movie_name"] == "Jumanji"

def test_book_ticket():
    booking_data = {
        "movie_id": 101,
        "seats": 2
    }
    response = requests.post(f"{BASE_URL}/api/bookings", json=booking_data)
    assert response.status_code == 201
    assert response.json()["message"] == "Booking successful"
