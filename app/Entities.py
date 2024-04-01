class Movie(object):
    def __init__(self, title, date, budget, length, origin, language, genra):
        self.title = title
        self.date = date
        self.budget = budget
        self.length = length
        self.origin = origin
        self.language = language
        self.genra = genra


class TheaterPlay(object):
    def __init__(self, title, date, budget, length, origin, language, genra, theater):
        self.title = title
        self.date = date
        self.budget = budget
        self.length = length
        self.origin = origin
        self.language = language
        self.genra = genra
        self.theater = theater
