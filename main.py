from everything import *

def main():
    data = read_file('BTCPrice.csv')
    data_clean = cleaning(data)
    data_analysis = analysis(data_clean)
    print(data_analysis.head())
    #data_api = api(data_analysis)


if __name__ == "__main__":
    main()
