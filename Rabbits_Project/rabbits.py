'''
rabbits.py
Jackson Daw
CS-1400-002
2/22/2022

docstring here

open the file in write mode
print the first month
calculate babies for each pair of adults
calculate babies becoming adults
increment month
print to file month, adults, babies, total
repeat until cages are full
close file

  
'''
import csv
    
def do_reasearch(cages, adults, babies):
    month = 1
    total = adults + babies
    with open('rabbits.csv', 'w', newline='') as rabbit_start:
        rabbit_start = csv.writer(rabbit_start, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        rabbit_start.writerow(["Month,Adults,Babies,Total"])
        rabbit_start.writerow([month] + [adults] + [babies] + [total])        
    if total < cages:
        month += 1
        adults += adults
        babies += babies
    elif total >= cages:
        with open('rabbits.csv', 'w', newline='') as rabbit_output:
            rabbit_writer = csv.writer(rabbit_output, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#             rabbit_writer.writerow(["Cages will run out in month"] + [month])

def main():
    cages = 500
    adults = 1
    babies = 0
    do_reasearch(cages, adults, babies)
if __name__ == "__main__":
    main()