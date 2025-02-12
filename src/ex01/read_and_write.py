def is_even(counter):
    return counter % 2 == 0

def main():
    quot_cnt = 0
    with open("ds.csv", "r") as inp, open("ds.tsv", "w") as out:
        for line in inp.readlines():
            lst_line = list(line)
            for ind, ch in enumerate(lst_line):
                if ch == '"':
                    quot_cnt += 1
                if ch == ',' and is_even(quot_cnt):
                    lst_line[ind] = '\t'
            out.write(''.join(lst_line))        

if __name__ == '__main__':
    main()