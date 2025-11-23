import os

FILE_NAME = "movies_data.txt"

def initialize_data():
    if not os.path.exists(FILE_NAME):
        defaults = [
            "101|Avatar: Way of Water|12.50|50",
            "102|Oppenheimer|15.00|30",
            "103|Spider-Man: No Way Home|10.00|0",
            "104|Inception|11.00|25"
        ]
        with open(FILE_NAME, "w") as f:
            f.write("\n".join(defaults))

def load_movies():
    initialize_data()
    movies = []
    with open(FILE_NAME, "r") as f:
        lines = f.readlines()
        for line in lines:
            if "|" in line:
                parts = line.strip().split("|")
                movies.append({
                    "id": parts[0],
                    "title": parts[1],
                    "price": float(parts[2]),
                    "seats": int(parts[3])
                })
    return movies

def update_movies(movie_list):
    lines = []
    for m in movie_list:
        line = f"{m['id']}|{m['title']}|{m['price']}|{m['seats']}"
        lines.append(line)
    
    with open(FILE_NAME, "w") as f:
        f.write("\n".join(lines))

def save_booking(user_name, movie_title, tickets, total_cost):
    with open("bookings.txt", "a") as f:
        f.write(f"User: {user_name} | Movie: {movie_title} | Tix: {tickets} | Total: Rs. {total_cost}")