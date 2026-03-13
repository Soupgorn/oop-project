from .ticket import Ticket

class Booking:
    def __init__(self, User, Show):
        self.__user = User
        self.__show = Show
        self.__booked_seats = []

    @property
    def show(self): return self.__show

    @property
    def booked_seats(self): return self.__booked_seats  

    @booked_seats.setter
    def booked_seats(self, value):
        self.__booked_seats = value


    def select_seat(self, Seat):
        if Seat.is_reserved:
            return "Seat is unavailable"
        Seat.reserve_seat()
        self.__booked_seats.append(Seat)
        return "ok"

    def confirm_booking(self):
        for seat in self.__booked_seats:
            ticket = Ticket(self.__show, seat)
            self.__user.ticket_list.append(ticket)

    def cancel_booking(self):
        for seat in self.__booked_seats:
            seat.unreserve_seat()
        self.__booked_seats = []