# coding: utf-8

from selenium_fixture import app
from model.user import User
from model.movie import Movie


def test_create_movie(app):
    app.go_to_home_page()
    app.login(User.Admin())
    app.create_movie(Movie.required_field('The Terminal', '2004'))
    expected_text = "The Terminal (2004)"
    assert app.is_movie_created() == expected_text, "Title is not equal"
    app.logout()


def test_movie_not_creatable_without_required_field(app):
    app.go_to_home_page()
    app.login(User.Admin())
    is_url_changed = app.create_movie_without_req_field(Movie('Terminator'))
    assert is_url_changed, 'URLs are not matched'
    assert app.is_not_movie_created(), 'Text is not equal'
    app.logout()
