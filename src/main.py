from argparse import ArgumentParser
from functools import lru_cache

@lru_cache
def fib(n: int) -> int:
    # TODO: implement your method here
    return 0

def main():
    parser = ArgumentParser(description='Fibonacci number generator.')
    parser.add_argument('n', type=int)
    args = parser.parse_args()
    print(fib(args.n))

if __name__ == '__main__':
    main()
