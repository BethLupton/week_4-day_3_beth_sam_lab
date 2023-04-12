class Task:

    def __init__(self, title, genre, year_of_release, id = None, ):
        self.title = title
        self.genre = genre
        self.year_of_release = year_of_release
        self.id = id

    def mark_complete(self):
        self.completed = True
