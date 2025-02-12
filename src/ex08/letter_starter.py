import sys


def main():
    try:
        mail = sys.argv[1]
    except IndexError:
        print('E-mail not specified')
        return
    with open('employees.tsv', 'r') as inp:
        for line in inp.readlines():
            splited = line.split('\t')
            if splited[-1].strip() == mail:
                print(f"Dear {splited[0]}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.")
                break

if __name__ == '__main__':
        main()
