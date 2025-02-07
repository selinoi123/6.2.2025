import sqlite3

conn = sqlite3.connect("6.2.2025.3.db")
cursor = conn.cursor()

def show_all_movies():
    cursor.execute("SELECT * FROM movies")
    movies = cursor.fetchall()
    if movies:
        print("All Movies -")
        for movie in movies:
            print(movie)
    else:
        print("No movies in the database.")


def search_movie():
    search_term = input("Enter movie name or part of it: ")
    query = "SELECT * FROM movies WHERE movie_name LIKE ?"
    cursor.execute(query, ('%' + search_term + '%',))

    results = cursor.fetchall()

    if results:
        print("Movies found:")
        for movie in results:
            print(movie)
    else:
        print("No movies found.")


def add_movie():
    movie_name = input("Enter movie title: ")
    genre = input("Enter genre: ")
    country = input("Enter country: ")
    language = input("Enter language: ")

    while True:
        try:
            year = int(input("Enter release year (2009 or later): "))
            if year < 2009:
                print("Year must be 2009 or later. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid year.")

    while True:
        try:
            revenue = float(input("Enter revenue (in millions, non-negative): "))
            if revenue < 0:
                print("Revenue cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid revenue amount.")

    query = """INSERT INTO movies (movie_name, genre, country, language, year, revenue) 
               VALUES (?, ?, ?, ?, ?, ?)"""

    try:
        cursor.execute(query, (movie_name, genre, country, language, year, revenue))
        conn.commit()
        print("Movie added successfully!")
    except sqlite3.IntegrityError:
        print("Error: Movie with this name already exists.")

show_all_movies()
search_movie()
add_movie()

conn.close()
