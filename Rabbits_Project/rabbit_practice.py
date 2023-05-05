import pandas as pd

def main():
    rabbits_csv = pd.read_csv('rabbits.csv')
    print(rabbits_csv.columns)

if __name__ == "__main__":
    main()