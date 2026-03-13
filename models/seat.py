
class Seat :
    def __init__ (self,seat_no,seat_type) :
        self.__seat_no = seat_no
        self.__seat_type = seat_type
        self.__is_reserved=False
    
    @property 
    def is_reserved (self): return self.__is_reserved
    
    @property
    def seat_no (self) : return self.__seat_no

    @property 
    def seat_type (self) : return self.__seat_type
    
    def reserve_seat (self) : 
        self.__is_reserved = True

    def unreserve_seat(self): 
        self.__is_reserved = False