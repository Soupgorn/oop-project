from models import *

def print_header(title):
    print("=" * 50)
    print(f"         SF CINEMA")
    print(f"  {title}")
    print("=" * 50)


def setup_cinema():#Setup Cinema
    cinema = Cinema("SF Cinema")

    fast10   = Movie("Fast & Furious X", "Action")
    in_youth = Movie("In Youth We Trust", "Drama")
    under    = Movie("The Undertaker",    "Drama")

    cinema.add_movie(fast10)
    cinema.add_movie(in_youth)
    cinema.add_movie(under)

    show1 = Show(fast10,   "14:00")
    show2 = Show(in_youth, "14:30")
    show3 = Show(under,    "15:00")
    show4 = Show(fast10,   "16:00")

    cinema.add_show(show1)
    cinema.add_show(show2)
    cinema.add_show(show3)
    cinema.add_show(show4)

    for sh in [show1, show4]:
        for row in ["A", "B", "C"]:
            for num in range(1, 5):
                t = "VIP" if row == "A" else "Normal"
                sh.add_seat(Seat(f"{row}{num}", t))

    for sh in [show2, show3]:
        for row in ["A", "B"]:
            for num in range(1, 4):
                t = "VIP" if row == "A" else "Normal"
                sh.add_seat(Seat(f"{row}{num}", t))

    arm = User("armlnwza007", "1234")
    jet = User("jetlnwza007", "5678")
    law = User("why.law","1234")
    cinema.add_user(arm)
    cinema.add_user(jet)
    cinema.add_user(law)

    cinema._shows = [show1, show2, show3, show4]
    return cinema


def screen_login(cinema): #Login
    while True:
        print_header("WELCOME")
        print("\n  1  Login")
        print("  2  Register")
        print("  0  Quit")
        print()

        choice = input("  Choose : ").strip()

        if choice == "0":
            return None
        elif choice == "1":
            user = do_login(cinema)
            if user:
                return user
        elif choice == "2":
            do_register(cinema)
        else:
            print("\n  Invalid choice")
            input("  (press Enter)")


def do_login(cinema):#Login Process
    print_header("LOGIN")
    username = input("\n  Username : ")
    password = input("  Password : ")

    user = cinema.search_user_by_username(username)
    if user and password == user.password:
        print(f"\n  Welcome, {username}!")
        input("  (press Enter to continue)")
        return user
    else:
        print("\n  Invalid username or password")
        input("  (press Enter to try again)")
        return None


def do_register(cinema):#Register Process
    print_header("REGISTER")
    username = input("\n  Username : ").strip()

    if not username:
        print("\n  Username cannot be empty")
        input("  (press Enter)")
        return

    if cinema.search_user_by_username(username):
        print(f"\n  Username '{username}' is already taken")
        input("  (press Enter)")
        return

    password = input("  Password : ").strip()
    if not password:
        print("\n  Password cannot be empty")
        input("  (press Enter)")
        return

    confirm = input("  Confirm Password : ").strip()
    if password != confirm:
        print("\n  Passwords do not match")
        input("  (press Enter)")
        return

    new_user = User(username, password)
    cinema.add_user(new_user)
    print(f"\n  Account created! Welcome, {username}!")
    input("  (press Enter to login)")


def screen_shows(cinema, user): #Shows
    while True:
        print_header(f"NOW SHOWING  |  {user.username}")
        print(f"\n  {'No.':<5} {'Time':<8} {'Movie':<26} {'Seats'}")
        print("  " + "-" * 46)

        shows = cinema._shows
        for i, sh in enumerate(shows):
            seats = sh.seat_list
            avail = sum(1 for s in seats if not s.is_reserved)
            total = len(seats)
            print(f"  {i+1}    {sh.time:<8} {sh.movie.movie_name:<26} {avail}/{total} available")

        print("\n  " + "-" * 46)
        print(f"  T  My Tickets ({len(user.ticket_list)} ticket(s))")
        print("  0  Logout")
        print()

        choice = input("  Choose : ").strip()

        if choice == "0":
            return
        elif choice.lower() == "t":
            screen_my_tickets(user)
        elif choice.isdigit() and 1 <= int(choice) <= len(shows):
            screen_seats(user, shows[int(choice) - 1])
        else:
            print("\n  Invalid choice, please try again")
            input("  (press Enter)")


def screen_seats(user, show):#Seats Choosing
    while True:
        print_header(f"{show.movie.movie_name}  @  {show.time}")

        seats = show.seat_list
        rows = {}
        for s in seats:
            r = s._Seat__seat_no[0]
            rows.setdefault(r, []).append(s)

        print()
        print("  [ ] = Available (Normal)   [V] = Available (VIP)   [X] = Taken")
        print()
        print("       ", end="")
        for s in rows[sorted(rows)[0]]:
            print(f" {s._Seat__seat_no[1:]} ", end="")
        print()

        for row_letter in sorted(rows):
            print(f"  {row_letter}    ", end="")
            for s in rows[row_letter]:
                if s.is_reserved:
                    print("[X]", end=" ")
                elif s._Seat__seat_type == "VIP":
                    print("[V]", end=" ")
                else:
                    print("[ ]", end=" ")
            print()

        print()
        avail_seats = [s for s in seats if not s.is_reserved]
        print(f"  Available seats: {len(avail_seats)}/{len(seats)}")
        print()

        if not avail_seats:
            print("  No seats available for this show")
            input("  (press Enter to go back)")
            return

        print("  Enter seat(s) to book e.g. A1 or A1 A2 B1")
        print("  0  Back")
        print()

        choice = input("  Choose : ").strip()

        if choice == "0":
            return

        seat_names = choice.upper().split()
        booking = Booking(user, show)
        success = []
        failed  = []

        for name in seat_names:
            found = next((s for s in seats if s._Seat__seat_no == name), None)
            if not found:
                failed.append(f"{name} (not found)")
            else:
                result = booking.select_seat(found)
                if result == "ok":
                    success.append(name)
                else:
                    failed.append(f"{name} (already taken)")

        print()
        if success:
            print(f"  Added to cart: {', '.join(success)}")
        if failed:
            print(f"  Could not book: {', '.join(failed)}")

        if not success:
            input("  (press Enter)")
            booking.cancel_booking()
            continue

        print()
        confirm = input("  Confirm booking? (y/n) : ").strip().lower()
        if confirm == "y":
            booking.confirm_booking()
            print(f"\n  Booking confirmed! {len(success)} seat(s) booked.")
            input("  (press Enter)")
            return
        else:
            booking.cancel_booking()
            print("  Booking cancelled")
            input("  (press Enter)")

def screen_my_tickets(user):#User's Tickets
    while True:
        print_header(f"MY TICKETS  |  {user.username}")

        tickets = user.ticket_list
        if not tickets:
            print("\n  You have no tickets yet. Go book a show!")
            print()
            input("  (press Enter to go back)")
            return

        print(f"\n  {'No.':<5} {'Time':<8} {'Movie':<26} {'Seat':<8} {'Type'}")
        print("  " + "-" * 55)
        for i, t in enumerate(tickets):
            seat = t._Ticket__seat
            show = t.show
            print(f"  {i+1:<5} {show.time:<8} {show.movie.movie_name:<26} {seat._Seat__seat_no:<8} {seat._Seat__seat_type}")

        print("\n  " + "-" * 55)
        print("  Enter ticket number to cancel, or 0 to go back")
        print()

        choice = input("  Choose : ").strip()

        if choice == "0":
            return
        elif choice.isdigit() and 1 <= int(choice) <= len(tickets):
            t = tickets[int(choice) - 1]
            seat = t._Ticket__seat
            show = t.show
            print(f"\n  Cancel: {show.movie.movie_name} @ {show.time} | Seat {seat._Seat__seat_no}")
            confirm = input("  Are you sure? (y/n) : ").strip().lower()
            if confirm == "y":
                booking = Booking(user, show)
                booking._Booking__booked_seats = [seat]
                user.cancel_booking_by_show(show, booking)
                print("  Ticket cancelled.")
            else:
                print("  Cancelled aborted.")
            input("  (press Enter)")
        else:
            print("\n  Invalid choice, please try again")
            input("  (press Enter)")


if __name__ == "__main__":
    cinema = setup_cinema()
    while True:
        user = screen_login(cinema)
        if user:
            screen_shows(cinema, user)