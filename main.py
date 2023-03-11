import matplotlib.pyplot as plt
import numpy as np


def f(_x):
    return np.sin(_x)


def bisection(e, d, _a, _b):
    while abs(_b - _a) > e:
        u1 = (_a + _b - d) / 2
        u2 = (_a + _b + d) / 2
        if f(u1) < f(u2):
            _b = u2
        elif f(u1) > f(u2):
            _a = u1
        else:
            _a = u1
            _b = u2
    u_s = (_b + _a) / 2
    print(u_s)
    return f(u_s)


def gold(e, _a, _b):
    while abs(_a - _b) > e:
        u1 = _a + ((3 - np.sqrt(5)) / 2) * (_b - _a)
        u2 = _a + ((np.sqrt(5) - 1) / 2) * (_b - _a)
        if f(u1) < f(u2):
            _b = u2
        elif f(u1) > f(u2):
            _a = u1
        else:
            _a = u1
            _b = u2

    u_s = (_a + _b) / 2
    print(u_s)
    return f(u_s)


def main():
    a, b = map(int, input("Input the ends of the segment: ").split())
    eps = 0.1
    delta = 0.01
    res_bisect = bisection(eps, delta, a, b)
    print(res_bisect)
    res_gold = gold(eps, a, b)
    print(res_gold)
    x = np.linspace(a, b, 200)
    y = [0]*len(x)
    for i in range(len(x)):
        y[i] = f(x[i])
    plt.plot(x, y, "red")
    plt.show()


if __name__ == "__main__":
    main()



