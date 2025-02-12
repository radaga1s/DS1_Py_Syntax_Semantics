import sys

def main():
    _, *args = sys.argv
    if len(args) != 1:
        return
    cmp_name = args[0].lower().capitalize()
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'}
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37}
    print(STOCKS.get(COMPANIES.get(cmp_name, 'unknown'), 'Unknown company'))

if __name__ == '__main__':
    main()