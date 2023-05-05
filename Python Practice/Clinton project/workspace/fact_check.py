'''This program takes both labor statistics and a list of presidents with their respective years and political parties and 
calculates how many jobs were made by each party'''
import csv
import pprint as pprint

def do_reasearch():
    '''changes the CSV into a series of lists'''
    with open('./BLS_private.csv', 'r', newline='') as bls_stat:
        bls_stat = csv.reader(bls_stat, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        bls_list = []
        for row in bls_stat:
            bls_list.append(row)
        bls_list = bls_list[5:]
        return bls_list

def do_presidents():
    '''changes the txt file into a series of lists and shows how many presidents were demo or repub'''
    with open('./presidents.txt', 'r', newline='') as pres_file:
        pres_stat = csv.reader(pres_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        pres_list = []
        demo_count = 0
        repub_count = 0
        for row in pres_stat:
            if row[2] == 'Democrat':
                demo_count += 1
            else:
                repub_count += 1
            pres_list.append(row)
        return pres_list
    
def rep_or_dem(bls_list):
    '''takes numbers from the BLS and adds zeroes so there is no empty space'''
    labor_stats = [[0 if y=='' else int(y) for y in x[1:]] for x in bls_list[1:]]
    return labor_stats

def get_months(start_date,end_date):
    '''calculates the periods of demo or repub throughout the time period'''
    start_date = start_date.split('/')
    end_date = end_date.split('/')
    start_date = [int(y) for y in start_date]
    end_date = [int(y) for y in end_date]
    return(((end_date[2] - start_date[2])*12)+ ((end_date[0]-1) - start_date[0]))


def get_ratio(presidents,labor_stats):
    '''calculates the number of jobs made by each party and the total number of jobs made'''
    pres_start_date = ''
    pres_end_date = ''
    check_point = 0
    demo_num = 0
    repub_num = 0
    flat_labor_stats = [x for sub_list in labor_stats for x in sub_list]
    for i,row in enumerate(presidents[:-1]):
        if row[3] != '':
            pres_start_date = row[3]
            for second_row in presidents[i+1:]:
                if second_row[3] != '':
                    pres_end_date = second_row[3]
                    break
            months_in_office = get_months(pres_start_date,pres_end_date)   
            for k in range(check_point,check_point+months_in_office):
                if row[2] == 'Democrat':
                    demo_num += flat_labor_stats[k]
                else:
                    repub_num += flat_labor_stats[k]
            check_point += months_in_office + 1
    print(f'total number of jobs since 1961 to 2013: {demo_num + repub_num}')
    print(f'number of democrat produced jobs: {demo_num}')
    print(f'number of republican produced jobs: {repub_num}')



def main():
    '''runs the program'''
    presidents = do_presidents()
    bls_list = do_reasearch()
    labor_stats = rep_or_dem(bls_list) 
    ratio_numbers = get_ratio(presidents,labor_stats)
if __name__ == "__main__":
    main()