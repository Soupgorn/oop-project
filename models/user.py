class User :
    def __init__(self,username,password):
        self.__username = username
        self.__password = password
        self.__ticket_List = []

    @property
    def username (self) : return self.__username

    @property
    def password (self) : return self.__password

    @property
    def ticket_list (self) : return self.__ticket_List

    def cancel_booking_by_show(self, show, booking_object):
        cancelled_seats = list(booking_object.booked_seats)
        booking_object.cancel_booking()
        self.__ticket_List = [t for t in self.__ticket_List if not (t.show == show and t.seat in cancelled_seats)]
