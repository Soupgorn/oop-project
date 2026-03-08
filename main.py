from models import *
if __name__ == "__main__":
    cinema = Cinema("SF")

    fast10 = Movie("Fast & Furious X","Action") #Fast10
    in_youth = Movie("In Youth We Trust","Drama") #วัยหนุ่ม2544
    under = Movie("The Undertaker" , "Drama") #สัปเหร่อ

    cinema.add_movie(fast10)
    cinema.add_movie(in_youth)
    cinema.add_movie(under)

    show1 = Show(fast10,"14.00")
    show2 = Show(in_youth,"14.30")
    show3 = Show(under,"15.00")
    show4 = Show(fast10,"16.00")
    
    cinema.add_show(show1)
    cinema.add_show(show2)
    cinema.add_show(show3)
    cinema.add_show(show4)


    s1_a1 = Seat("A1", "Normal")
    s1_a2 = Seat("A2", "VIP")
    show1.add_seat(s1_a1)
    show1.add_seat(s1_a2)

    s2_a1 = Seat("A1", "Normal")
    s2_a2 = Seat("A2", "VIP")
    show2.add_seat(s2_a1)
    show2.add_seat(s2_a2)

    arm = User("armlnwza007","1234")
    jet = User("jetlnwza007","1234")

    cinema.add_user(arm)
    cinema.add_user(jet)

    arm_booking1 = Booking(arm,show1)
    arm_booking1.select_seat(s1_a1)
    arm_booking1.confirm_booking()

    arm_booking2 = Booking(arm,show1)
    arm_booking2.select_seat(s1_a2)
    arm_booking2.confirm_booking()



    print(f"User: {arm.username} has {len(arm.ticket_list)} ticket(s).")

    yo = cinema.search_movie_time_by_movie_name("Fast & Furious X")

    for i in yo :
        print(i)

    arm.cancel_booking_by_show(show1, arm_booking1)
    
    print(f"User: {arm.username} has {len(arm.ticket_list)} ticket(s).")