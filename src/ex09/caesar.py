import sys


def encode(alphabet: str, string: str, offset: int) -> str:
    res = [alphabet[(alphabet.index(c) + offset) % len(alphabet)] if c in alphabet else c for c in string]
    return ''.join(res)

def decode(alphabet: str, string: str, offset: int) -> str:
    res = [alphabet[(alphabet.index(c) - offset) % len(alphabet)] if c in alphabet else c for c in string]
    return ''.join(res)

def main():
    if len(sys.argv) != 4:
        raise Exception('Incorrect number of arguments')
    if any(ord(c) > 126 for c in sys.argv[2]):
        raise Exception('The script does not support your language yet')
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    d = dict(encode=encode, decode=decode)
    print(d[sys.argv[1]](alphabet, sys.argv[2], int(sys.argv[3])))

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
