import threading
from math import factorial


def main():
    run_status()
    conjecture()


def conjecture():
    p = 1
    while True:
        x = factorial(p)
        b = p
        i = 1
        while b < x:
            b *= (p+i)
            i += 1

        if x == b:
            print("n = {}, p = {}, x = {}".format(p+i-1, p, x))
        p += 1


def run_status():
  threading.Timer(5.0, run_status).start()
  print("Running...")


if __name__ == "__main__":
    main()
