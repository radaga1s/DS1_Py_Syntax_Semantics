import sys


def main():    
    try:
        adress = sys.argv[1]
    except IndexError:
        print('path not specified')
        return
    with open(adress, 'r') as inp, open('employees.tsv', 'w') as out:
        out.write('Name\tSurname\tE-mail\n')
        for line in inp.readlines():
            name, surname = line.split('@')[0].split('.')
            out.write(f'{name.capitalize()}\t{surname.capitalize()}\t{line}')

if __name__ == '__main__':
    main()
