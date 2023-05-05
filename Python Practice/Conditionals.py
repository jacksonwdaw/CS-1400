def main():
    x = 25
    if x // 5 and x % 5 == 0:
        print(f"{x} is divisible by 5 and even")
        
        getmonth(3,x)
    else:
        print(f"{x} is not divisible by 5 or it is odd")

main()

#If statements only ask if a boolean expression is true.
#If statements are the simplest of all the conditionals.
def getmonth(month, n):
    
    if month == 1:
      print("January")
    if month == 2:
      print("February")
    if month == 3:
      print("March")
    if month == 4:
      print("April")
    if month == 5:
      print("May")
    if month == 6:
      print("June")
    if month == 7:
      print("July")
    if month == 8:
      print("August")
    if month == 9:
      print("September")
    if month == 10:
      print("October")
    if month == 11:
      print("November")
    if month == 12:
      print("December")

