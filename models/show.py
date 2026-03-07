
class Show :
    def __init__(self,Movie,time):
        self.__movie = Movie
        self.__time = time
        self.__seat_list = []
    
    @property
    def seat_list (self) : return self.__seat_list

    @property
    def movie(self) : return self.__movie

    @property
    def time(self) : return self.__time

    def add_seat (self,Seat) :
        self.__seat_list.append(Seat)

