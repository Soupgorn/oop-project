class Ticket :  
    def __init__(self,Show,Seat):
        self.__show = Show
        self.__seat = Seat
    @property
    def show(self): return self.__show

    @property
    def seat(self): return self.__seat