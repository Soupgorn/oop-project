from .ticket import Ticket

class Booking :
    def __init__(self,User,Show):
        self.__user = User
        self.__show = Show
        self.__booked_seats = []
    
    @property
    def show(self): return self.__show
    
    def select_seat(self,Seat) :
        if Seat.is_reserved == False :
            Seat.reserve_seat()
            self.__booked_seats.append(Seat)
        else :
            return "Seat is unavailable"
        
    def confirm_booking (self):
        for seat in self.__booked_seats :
            ticket = Ticket(self.__show,seat)
            self.__user.ticket_list.append(ticket)

    def cancel_booking(self):
        for seat in self.__booked_seats:
            seat.unreserve_seat()
        self.__booked_seats = []

            