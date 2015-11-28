# coding: utf-8


class Movie(object):

    def __init__(self, title=None, year=None, imdb=None, aka=None, duration=None, rating=None):
        self.title = title
        self.year = year
        self.imdb = imdb
        self.aka = aka
        self.duration = duration
        self.rating = rating

    @classmethod
    def required_field(cls, title, year):
        return cls(title=title, year=year)
