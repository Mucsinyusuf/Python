
#Classes are blueprints
#Objects are the actual things you built
#variables => attributes
#functions => methods

class Movie:
    def __init__(self,title,year,imdb_score,have_seen):
        self.title=title
        self.year=year
        self.imdb_score= imdb_score
        self.have_seen= have_seen

    def nice_print(self):
        print("Title: ", self.title)
        print("Year of production: ", self.year)
        print("IMDB Score: ", self.imdb_score)
        print("I have seen it: ", self.have_seen)

film1 =Movie("Life of Brian",1979,6.1,True)
film2 =Movie("Life of joe",1978,7.1,True)
films = [film1,film2]
print(films[1].title,films[0].title)
films[0].nice_print()
# print(film1.title, film2.imdb_score)
# film2.nice_print()