import booking_engine
import storage
import os


def history():
    if os.path.exists("bookings.txt"):
        print("\n--- RECENT BOOKINGS ---")
        with open("bookings.txt", "r") as f:
            print(f.read())
    else:
        print("No bookings found yet.")

def main():
    while True:
        print("\n" + "="*40)
        print("   TICKET BOOKING SYSTEM")
        print("="*40)

        print("1. Movies Menu")
        print("2. Book Tickets")
        print("3. View Booking History")
        print("4. Exit")
    
        choice =int(input("Select Option (1-4): "))
        
        if choice == 1:
            movie_see()
        elif choice == 2:
            booking_engine.book_ticket()
        elif choice == 3:
            history()
        elif choice == 4:
            print("Thanks for using CineMatch")
            break
        else:
            print("Please choose from the options available")

def movie_see():
    movies = storage.load_movies()
    print("\n--- NOW SHOWING ---")
    print(f"{'ID':<5} {'Title':<25} {'Price':<8} {'Seats Left'}\n")
    print("-" * 50)
    
    for m in movies:
        if m['seats'] > 0:
            status = m['seats']
        else:
            status = "SOLD OUT"
        print(f"{m['id']:<5} {m['title']:<25} Rs. {m['price']:<7} {status}\n")
    
    print("-" * 50)
    return movies

if __name__ == "__main__":
    main()