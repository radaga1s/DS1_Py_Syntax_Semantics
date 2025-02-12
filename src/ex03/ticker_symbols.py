import sys

def get_key_by_val(dct, name):
    for key, val in dct.items():
        if name == val:
            return key
    return -1

def main():
    _, *args = sys.argv
    if len(args) != 1:
        return
    tick_name = args[0].upper()
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
    if (cmp_name := get_key_by_val(COMPANIES, tick_name)) == -1:
        print('Unknown ticker')
    else:
        print(cmp_name, STOCKS[tick_name])

if __name__ == '__main__':
    main()
