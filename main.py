from models import *

def print_header(title):
    print("=" * 50)
    print(f"         SF CINEMA")
    print(f"  {title}")
    print("=" * 50)


def setup_cinema():
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
    law = User("why.law", "1234")
    admin = User("admin", "admin")
    cinema.add_user(arm)
    cinema.add_user(jet)
    cinema.add_user(law)
    cinema.add_user(admin)

    cinema._shows = [show1, show2, show3, show4]
    cinema._admins = {"admin"}
    return cinema


# ── Login / Register ──────────────────────────────────────────────────────────

def screen_login(cinema):
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


def do_login(cinema):
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


def do_register(cinema):
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


# ── Admin ─────────────────────────────────────────────────────────────────────

def screen_admin(cinema):
    while True:
        print_header("ADMIN PANEL")
        print("\n  1  Add movie")
        print("  2  Add show")
        print("  3  Search movie by genre")
        print("  4  Search showtime by movie name")
        print("  0  Logout")
        print()

        choice = input("  Choose : ").strip()

        if choice == "0":
            return
        elif choice == "1":
            do_add_movie(cinema)
        elif choice == "2":
            do_add_show(cinema)
        elif choice == "3":
            do_search_by_genre(cinema)
        elif choice == "4":
            do_search_by_name(cinema)
        else:
            print("\n  Invalid choice")
            input("  (press Enter)")


def do_add_movie(cinema):
    print_header("ADD MOVIE")
    name = input("\n  Movie name : ").strip()
    if not name:
        print("\n  Name cannot be empty")
        input("  (press Enter)")
        return
    genre = input("  Genre      : ").strip()
    if not genre:
        print("\n  Genre cannot be empty")
        input("  (press Enter)")
        return
    cinema.add_movie(Movie(name, genre))
    print(f"\n  Movie '{name}' added!")
    input("  (press Enter)")


def do_add_show(cinema):
    print_header("ADD SHOW")
    movies = cinema.movie_list
    if not movies:
        print("\n  No movies in system. Add a movie first.")
        input("  (press Enter)")
        return

    print()
    for i, m in enumerate(movies):
        print(f"  {i+1}  {m.movie_name} ({m.movie_type})")
    print()

    choice = input("  Select movie No. : ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(movies)):
        print("\n  Invalid choice")
        input("  (press Enter)")
        return

    movie = movies[int(choice) - 1]
    time = input("  Showtime (e.g. 14:00) : ").strip()
    if not time:
        print("\n  Time cannot be empty")
        input("  (press Enter)")
        return

    rows_input = input("  Seat rows (e.g. A B C) : ").strip().upper().split()
    if not rows_input:
        print("\n  At least one row required")
        input("  (press Enter)")
        return

    seats_per_row = input("  Seats per row : ").strip()
    if not seats_per_row.isdigit() or int(seats_per_row) < 1:
        print("\n  Invalid number")
        input("  (press Enter)")
        return

    vip_rows = input("  VIP rows (e.g. A), leave blank for none : ").strip().upper().split()

    show = Show(movie, time)
    for row in rows_input:
        for num in range(1, int(seats_per_row) + 1):
            t = "VIP" if row in vip_rows else "Normal"
            show.add_seat(Seat(f"{row}{num}", t))

    cinema.add_show(show)
    cinema._shows.append(show)
    total = len(rows_input) * int(seats_per_row)
    print(f"\n  Show added! {movie.movie_name} @ {time} — {total} seats")
    input("  (press Enter)")


def do_search_by_genre(cinema):
    print_header("SEARCH BY GENRE")
    genre = input("\n  Genre : ").strip()
    results = cinema.search_movie_by_type(genre)
    if results:
        print(f"\n  Found {len(results)} movie(s):")
        for m in results:
            print(f"    - {m}")
    else:
        print("\n  No movies found.")
    input("  (press Enter)")


def do_search_by_name(cinema):
    print_header("SEARCH SHOWTIME")
    name = input("\n  Movie name : ").strip()
    results = cinema.search_movie_time_by_movie_name(name)
    if results:
        print(f"\n  Showtimes for '{name}':")
        for t in results:
            print(f"    - {t}")
    else:
        print("\n  No showtimes found.")
    input("  (press Enter)")


# ── User screens ──────────────────────────────────────────────────────────────

def screen_shows(cinema, user):
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
        print(f"  S  Search")
        print(f"  T  My Tickets ({len(user.ticket_list)} ticket(s))")
        print("  0  Logout")
        print()

        choice = input("  Choose : ").strip()

        if choice == "0":
            return
        elif choice.lower() == "t":
            screen_my_tickets(user)
        elif choice.lower() == "s":
            screen_search(cinema)
        elif choice.isdigit() and 1 <= int(choice) <= len(shows):
            screen_seats(user, shows[int(choice) - 1])
        else:
            print("\n  Invalid choice, please try again")
            input("  (press Enter)")


def screen_search(cinema):
    while True:
        print_header("SEARCH")
        print("\n  1  Search movie by genre")
        print("  2  Search showtime by movie name")
        print("  0  Back")
        print()

        choice = input("  Choose : ").strip()

        if choice == "0":
            return
        elif choice == "1":
            do_search_by_genre(cinema)
        elif choice == "2":
            do_search_by_name(cinema)
        else:
            print("\n  Invalid choice")
            input("  (press Enter)")


def screen_seats(user, show):
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
                elif s.seat_type == "VIP":
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
            found = next((s for s in seats if s.seat_no == name), None)
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


def screen_my_tickets(user):
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
            seat = t.seat
            show = t.show
            print(f"  {i+1:<5} {show.time:<8} {show.movie.movie_name:<26} {seat.seat_no:<8} {seat.seat_type}")

        print("\n  " + "-" * 55)
        print("  Enter ticket number to cancel, or 0 to go back")
        print()

        choice = input("  Choose : ").strip()

        if choice == "0":
            return
        elif choice.isdigit() and 1 <= int(choice) <= len(tickets):
            t = tickets[int(choice) - 1]
            seat = t.seat
            show = t.show
            print(f"\n  Cancel: {show.movie.movie_name} @ {show.time} | Seat {seat._Seat__seat_no}")
            confirm = input("  Are you sure? (y/n) : ").strip().lower()
            if confirm == "y":
                booking = Booking(user, show)
                booking.booked_seats = [seat]
                user.cancel_booking_by_show(show, booking)
                print("  Ticket cancelled.")
            else:
                print("  Cancelled aborted.")
            input("  (press Enter)")
        else:
            print("\n  Invalid choice, please try again")
            input("  (press Enter)")


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    cinema = setup_cinema()
    while True:
        user = screen_login(cinema)
        if user is None:
            print("\n  Goodbye!")
            break
        if user.username in cinema._admins:
            screen_admin(cinema)
        else:
            screen_shows(cinema, user)