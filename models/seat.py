
class Seat :
    def __init__ (self,seat_no,seat_type) :
        self.__seat_no = seat_no
        self.__seat_type = seat_type
        self.__is_reserved=False
    
    @property 
    def is_reserved (self): return self.__is_reserved
    
    def reserve_seat (self) : 
        self.__is_reserved = True

    def unreserve_seat(self): 
        self.__is_reserved = False