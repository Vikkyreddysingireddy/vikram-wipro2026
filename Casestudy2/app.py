from flask import Flask, jsonify, request

app = Flask(__name__)

movies = [
    {
        "id": 101,
        "movie_name": "Ironman",
        "language": "English",
        "duration": "2h 9m",
        "price": 250
    }
]

bookings = []

@app.route("/api/movies", methods=["GET"])
def get_movies():
    return jsonify(movies), 200

@app.route("/api/movies/<int:movie_id>", methods=["GET"])
def get_movie_by_id(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return jsonify(movie), 200
    return jsonify({"error": "Movie not found"}), 404


@app.route("/api/movies", methods=["POST"])
def add_movie():
    data = request.get_json()
    movies.append(data)
    return jsonify(data), 201

@app.route("/api/movies/<int:movie_id>", methods=["PUT"])
def update_movie(movie_id):
    data = request.get_json()
    for movie in movies:
        if movie["id"] == movie_id:
            movie.update(data)
            return jsonify(movie), 200
    return jsonify({"error": "Movie not found"}), 404


@app.route("/api/movies/<int:movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            movies.remove(movie)
            return jsonify({"message": "Movie deleted"}), 200
    return jsonify({"error": "Movie not found"}), 404


@app.route("/api/bookings", methods=["POST"])
def book_ticket():
    data = request.get_json()
    if not data.get("movie_id") or not data.get("seats"):
        return jsonify({"error": "Invalid booking data"}), 400

    bookings.append(data)
    return jsonify({"message": "Booking successful"}), 201


if __name__ == "__main__":
    app.run(debug=True)
