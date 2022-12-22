#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    prime_func = __import__('prime_func').prime_factor
    with open("test", encoding = 'utf-8') as f:
        for line in f:
            line = int(line)
            val = prime_func(line)
            print(f"{line} = {val[0]} * {val[1]}")
