from flask import Flask, jsonify
from utils import get_movie_by_title, get_movie_by_years, get_movie_by_genre, rating_children, rating_family, \
    rating_adults

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route("/movie/<title>")
def movie_by_title(title):
    films = get_movie_by_title(title)
    return jsonify(films)


@app.route("/movie/<int:year_1>/to/<int:year_2>")
def movie_by_years(year_1, year_2):
    films = get_movie_by_years(year_1, year_2)
    return jsonify(films)


@app.route("/rating/children")
def children_movies():
    films = rating_children()
    return jsonify(films)


@app.route("/rating/family")
def family_movies():
    films = rating_family()
    return jsonify(films)


@app.route("/rating/adults")
def adults_movies():
    films = rating_adults()
    return jsonify(films)


@app.route("/genre/<genre>")
def movie_by_genre(genre):
    films = get_movie_by_genre(genre)
    return jsonify(films)


if __name__ == '__main__':
    app.run(debug=True)
