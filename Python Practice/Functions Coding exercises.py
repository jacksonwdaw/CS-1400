#exercise 1
def avg(n1, n2):
    """Return average of two numbers
    Return a message is a non-number is passed"""
    try:
      return(n1 + n2) / 2
    except TypeError:
      return("Please use two numbers as parameters")
#exercise 2
def odds_or_evens(my_bool, nums):
    """Returns all of the odd or
    even numbers from a list"""
    return_list = []
    for num in nums:
      if my_bool:
          if num % 2 == 0:
              return_list.append(num)
      else:
          if num % 2 != 0:
              return_list.append(num)
                
    return return_list
#exercise 3
def search_list(lst, term):
    """Search for item in a list
    Return the index if found
    Return -1 if not found"""
    for item in lst:
        if item.lower() == term.lower():
            return lst.index(item)
    return -1
#exercise 4
import csv

mlb_data = "student_folder/.exercises/mlb_data.csv"

def best_team(file):
    """Read a CSV of baseball data.
    Return the team name with the most wins"""
    with open(file, "r") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        most_wins = 0
        best_team = ""
        for row in reader:
            if int(row[3]) > most_wins:
                most_wins = int(row[3])
                best_team = row[0]
        return best_team
#exercise 5
def is_palindrome(palindrome):
  if palindrome == palindrome[::-1]:
    return True
  else:
    return False