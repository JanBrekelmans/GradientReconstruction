import numpy as np


def constant_function(nodes, a):
    r = a * np.ones(nodes.shape[0])
    return r


def linear_function(nodes, a, b, c):
    x = nodes[:, 0]
    y = nodes[:, 1]
    return a + b * x + c * y


def quadratic_function(nodes, a, b, c, d, e, f):
    x = nodes[:, 0]
    y = nodes[:, 1]
    return a + b * x + c * y + d * x * x + e * x * y + f * y * y


def sine_sum(nodes, a, b):
    x = nodes[:, 0]
    y = nodes[:, 1]
    return a * np.sin(b * (x + y))
