class Cinema :
    def __init__(self,cinema_name):
        self.__cinema_name = cinema_name
        self.__userlist = []
        self.__movie_list = []
        self.__show_list = []

    @property
    def movie_list (self) : return self.__movie_list
    
    def add_movie (self,Movie) : self.__movie_list.append(Movie)

    def add_user (self,User) : self.__userlist.append(User)

    def add_show (self,Show) :self.__show_list.append(Show)
    
    def search_user_by_username (self,username) :
        for user in self.__userlist :
            if user.username == username :
                return user
    
    def search_movie_by_type (self,movie_type) :
        found_movies = []
        for movie in self.__movie_list :
            if movie.movie_type == movie_type :
                found_movies.append(movie.movie_name)
        return found_movies

    def search_movie_time_by_movie_name(self,movie_name) :
        found_show_time = []
        for show_movie in self.__show_list :
            if show_movie.movie.movie_name == movie_name :
                found_show_time.append(show_movie.time)
        return found_show_time

    
    

