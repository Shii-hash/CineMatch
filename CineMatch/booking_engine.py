import storage
import main

def book_ticket():
    movies = main.movie_see()
    
    movie_id = int(input("\nEnter Movie ID to book: "))
    
    selected_movie = None
    for m in movies:
        if int(m[f'id']) == movie_id:
            selected_movie = m
            break
            
    if not selected_movie:
        print("Error: Invalid Movie ID.")
        return

    if selected_movie['seats'] == 0:
        print("show is Housefull.")
        return

    try:
        count = int(input(f"How many tickets for '{selected_movie['title']}'? "))
        if count <= 0:
            print("Error: Invalid number.")
            return
        if count > selected_movie['seats']:
            print(f"Error: Only {selected_movie['seats']} seats remaining.")
            return
            
        total_price = count * selected_movie['price']
        print(f"Total Cost: Rs. {total_price}")
        confirm = input("Confirm booking? (y/n): ")
        
        if confirm.lower() == 'y':
            selected_movie['seats'] -= count
            storage.update_movies(movies)
            
            name = input("Enter your name for booking: ")
            storage.save_booking(name, selected_movie['title'], count, total_price)
        print("Ticket Booked!")
        print(f"Enjoy watching {selected_movie['title']}!")
            
    except ValueError:
        print("Error: Please enter a number.")