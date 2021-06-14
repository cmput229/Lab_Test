from argparse import ArgumentParser
from functools import lru_cache

@lru_cache
def fib(n: int) -> int:
    assert n >= 0
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def main():
    parser = ArgumentParser(description='Fibonacci number generator.')
    parser.add_argument('n', type=int)
    args = parser.parse_args()
    print(fib(args.n))

if __name__ == '__main__':
    main()
