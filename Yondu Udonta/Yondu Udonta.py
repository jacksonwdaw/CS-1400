'''
Project Name: Yondu Udonta
Author: Jackson Daw
Due Date: 1/27/2023
Course: CS1400-002

This program takes the number of reavers including the captain Yondu Udonta and first mate Peter Quill and the loot they acquired in their raids and outputs how the loot is divied up among the crew.
In doing this project I learned that sometimes when coding and debugging, it may be better to just redo a section that has a problem rather than play where's waldo with the bug.
I also learned that there is many more ways to simplify code that make sense but I didn't understand them till I actually used them.
The only note I can think of that matters is that when inputting how many reavers are there total, know that Yondu and Peter must be included in that total.
It should be good besides that. 
'''

def main():
    '''
    Program starts here.
    '''
    try:
        reavers = int(input("How many reavers are there total? "))
        units = int(input("How many units are there when they arrive in port? "))
    except ValueError:
        print("Enter positive integers for reavers and units.")
        return

    if reavers < 1 or units < 1:
        print("Enter positive integers for reavers and units.")
        return

    if reavers < 3:
        print("Not enough crew.")
        return

    if units <= 3 * reavers:
        print("Not enough units.")
        return

    shore_cut = 3
    units_after_cut = units - ((reavers - 2) * shore_cut)
    units_check = units_after_cut
    
    yondu_share = int(units_after_cut * .13)
    units_after_cut -= yondu_share
    
    quill_share = int(units_after_cut * .11)
    units_after_cut -= quill_share
    
    crew_share = int(units_after_cut * (1 / reavers))
    rbf_donation = int(units_after_cut % reavers)
    
    print()
    print(f"Yondu's cut is {yondu_share+crew_share} units")
    print(f"Peter's cut is {quill_share+crew_share} units")
    print(f"The crews cut is {crew_share} units each")
    print(f"The donation to the Reavers Benevolent Fund is {rbf_donation} units")
    
    code_check = (int(yondu_share) + int(quill_share) + int((crew_share) * reavers) + int(rbf_donation))



    if code_check == units_check:
        print("This code works!")
    else:
        print("This code needs work...")
main()
