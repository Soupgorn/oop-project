
class Movie :
    def __init__(self,movie_name,movie_type):
        self.__movie_name = movie_name
        self.__movie_type = movie_type

    @property
    def movie_name (self) : return self.__movie_name
    
    @property
    def movie_type (self) : return self.__movie_type
