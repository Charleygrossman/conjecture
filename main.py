from typing import *
from argparse import ArgumentParser
from threading import Timer
from math import factorial


def main():
    try:
        start, end, no_status = args()
    except Exception as e:
        raise ValueError(f"Failed to parse arguments: {e}")

    global a, done
    a, done = start, False

    ok = lambda a, end: a <= end if end is not None else True

    if not no_status:
        status()

    result = compute(ok, end)
    done = True
    print("All found:")
    for v in result:
        print(f"a: {v[0]} b: {v[1]} value: {v[2]}")


def compute(ok: Callable[[int, int], bool], end: int) -> List[Tuple[int, int, int]]:
    result = []
    global a
    val = factorial(a-1)
    while ok(a, end):
        val *= a
        x, i = a, 1
        while x < val:
            x *= a + i
            i += 1
        b = a + i - 1
        if x == val and a < b:
            print(f"Found: a={a} b={b} value={val}")
            result.append((a, b, val))
        a += 1
    return result

def status():
    if not done:
        print(f"Current a: {a}")
        Timer(2, status).start()

def args() -> Tuple[int, Optional[int], bool]:
    p = ArgumentParser()
    p.add_argument('--start', type=int, required=False, default=1, help="start value of a")
    p.add_argument('--end', type=int, required=False, default=None, help="end value of a")
    p.add_argument('--no-status', type=bool, required=False, default=False, help="disable status output")
   
    args = p.parse_args()
    s, e = args.start, args.end
    if s < 1:
        raise ValueError(f"start must be a positive integer: start={s}")
    if e is not None:
        if e < 1:
            raise ValueError(f"end must be a positive integer: end={e}")
        if s > e:
            raise ValueError(f"start must come before or on end: start={s} end={e}")
    return s, e, args.no_status


if __name__ == "__main__":
    main()
