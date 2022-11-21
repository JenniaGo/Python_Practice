from flask import Flask, render_template, url_for, request, redirect
import requests
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import InputRequired



app = Flask(__name__)

db = SQLAlchemy(app)

# Movie object
class Movie:
    def __init__(self,id,title,overview,poster,vote_average,vote_count,date_release):
        self.id = id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.vote_average = vote_average
        self.vote_count = vote_count
        self.date_release = date_release

# tmdb api token
api_key = 'COPY API TOKEN HERE'

# tmdb reqeust urls
discover_base_url = "https://api.tmdb.org/3/discover/movie/?api_key="+api_key
base_url = "https://api.themoviedb.org/3/movie/{}?api_key={}"


def process_results(movie_list):
    """
    Function  that processes the movie result and transform them to a list of Objects
    Args:
        movie_list: A list of dictionaries that contain movie details
    Returns :
        movie_results: A list of movie objects
    """
    movie_results = []
    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')
        date_release = movie_item.get('release_date')

        if poster:
            movie_object = Movie(id, title, overview, poster, vote_average, vote_count, date_release)
            movie_results.append(movie_object)

    return movie_results

# get movies from categories
def get_movies(category):
    """
    Function that gets the json response to our url request
    """
    get_movies_url = base_url.format(category, api_key)
    get_movies_response = requests.get(get_movies_url).json()

    if get_movies_response['results']:
        movie_results_list = get_movies_response['results']
        movie_results = process_results(movie_results_list)

    return movie_results

# get movie details from movie id
def get_movie(id):
    get_movie_details_url = base_url.format(id, api_key)
    movie_details_response = requests.get(get_movie_details_url).json()

    if movie_details_response:
        id = movie_details_response.get('id')
        title = movie_details_response.get('original_title')
        overview = movie_details_response.get('overview')
        poster = movie_details_response.get('poster_path')
        vote_average = movie_details_response.get('vote_average')
        vote_count = movie_details_response.get('vote_count')
        date_release = movie_details_response.get('release_date')

        movie_object = Movie(id, title, overview, poster, vote_average, vote_count,date_release)

    return movie_object

# Search movie by name
def search_movie(movie_name):

    search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key, movie_name)
    search_movie_response = requests.get(search_movie_url).json()

    if search_movie_response['results']:
        search_movie_list = search_movie_response['results']
        search_movie_results = process_results(search_movie_list)
        print(search_movie_results)
        return search_movie_results

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    popular_movies = get_movies("popular")
    upcoming_movie = get_movies("upcoming")
    now_showing_movie = get_movies("now_playing")
    title = 'Home - Welcome to The best Movie Review Website Online'

    search_movie = request.args.get('movie_query')
    if search_movie:
        return redirect(url_for('search',movie_name=search_movie))
    else:
        return render_template('index.html',
                                title = title,
                                popular = popular_movies,
                                upcoming = upcoming_movie,
                                now_showing = now_showing_movie)

    # conn = requesto.urlopen(discover_base_url)
    # json_data = json.loads(conn.read())
    # return render_template("index.html", elements=json_data["results"])

# Show detail of each movie
@app.route("/movie/<int:id>")
def movie(id):
    movie = get_movie(id)
    title = f'{movie.title}'
    #reviews = Review.query.filter_by(movie_id =id).all()
    return render_template("movie.html", id=id, title=title, movie=movie) #,reviews=reviews)

# Search movie by name
@app.route('/search/<movie_name>')
def search(movie_name):
    '''
    View function to display the search results
    '''
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'
    return render_template("search.html", title = title, movies = searched_movies)

@app.route('/Poster')
def Poster():
    return render_template("Poster.html")


if __name__ == "__main__":
    app.run(debug=True, port=5007)
