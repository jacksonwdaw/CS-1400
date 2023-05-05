import csv, operator

movie_csv = "student_folder/.labs/movie_data.csv"

def fetch_movie_data(movie_csv):
    """Return movie data from a CSV file"""
    with open(movie_csv, "r") as movie_file:
        reader = csv.reader(movie_file)
        movie_info = []
        for row in reader:
          movie_info.append(row)
        return movie_info

def get_money(gross):
    return float(gross[3])

def print_movie_data(data):
    """Print the movie data in easy to read columns"""
    for title, genre, rotten, gross, year in data:
        print("{:36} {:10} {:18} ${:16} {}".format(title, genre, rotten, gross, year))
    
def sort_movie_data(data, index, descending):
    """Sort movie data based on the column data"""
    header = data[0]
    sorted_movies = data[1:]
    if index == 3:
        sorted_movies.sort(key=get_money)
    else:
        sorted_movies.sort(key=operator.itemgetter(index))
    if descending:
        sorted_movies.reverse()
    sorted_movies.insert(0, header)
    return sorted_movies

def ask_column():
    """Ask the user by which criteria they want to sort the data"""
    column = input("""How do you want to sort the movie data? Enter '6' to exit the program.
        1) By Film Title
        2) By Genre
        3) By Rotten Tomatoes Score
        4) By Worldwide Gross
        5) By Year
        6) Quit\n""")
    return column

def sanitize_column(column):
    """Return True if the user entered a valid number, else return False"""
    try:
        int(column)
        return int(column) >= 1 and int(column) <= 5
    except ValueError:
        return False

def ask_order():
    """Ask the user how they want the data sorted: ascending or descending"""
    order = input("""How do you want the movie data ordered?
          1) Ascending Order
          2) Descending Order\n""")
    return order

def sanitize_order(order):
    """Return True if the user entered a valid number, else return False"""
    try:
        int(order)
        return int(order) >= 1 and int(order) <= 2
    except ValueError:
        return False

def user_interface():
    """Ask user how they want to sort the movie data"""
    while True:
        column = ask_column()
        if column == "6":
            break
        if sanitize_column(column):
            order = ask_order()
            if sanitize_order(order):
                movie_data = fetch_movie_data(movie_csv) 
                print_movie_data(sort_movie_data(movie_data, int(column) - 1, int(order) == 2))
            else:
                print("Enter a number 1 or 2.\n")
        else:
            print("Enter a number 1 to 6.\n")

user_interface()


def to_upper(case):
  return case.upper()


'''
answers:
1: local, global
2: pass allows you to have a function header but acts as a placeholder
for the function body until you write it.
3: 5, 7
4: Function Composition
5: helper functions
'''