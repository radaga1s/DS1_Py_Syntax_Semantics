import sys

def get_key_by_val(dct: dict, name: str) -> str:
    for key, val in dct.items():
        if name == val:
            return key

def get_cmp_stck(cmp_d: dict, stck_d: dict, name: str) -> str:
    cmp_name =  name.lower().capitalize()
    stck_name = name.upper()
    if cmp_name in cmp_d:
        res = f'{cmp_name} stock price is {stck_d[cmp_d[cmp_name]]}'
    elif stck_name in stck_d:
        res = f'{stck_name} is a ticker symbol for {get_key_by_val(cmp_d, stck_name)}'
    else:
        res = f'{name} is an unknown company or an unknown ticker symbol'
    return res

def main():
    _, *args = sys.argv
    if len(args) != 1:
        return
    else:
        names_str = args[0].replace(' ', '')
        if names_str.count(',,'):
            return
        names = names_str.split(',')
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
    for name in names:
        print(get_cmp_stck(COMPANIES, STOCKS, name))

if __name__ == '__main__':
    main()
