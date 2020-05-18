import numpy as np

def SEIR_model(beta, gamma, a):

    def f(t, x):
        S, E, I, R = x
        return np.array([
            -beta * S * I,
            beta * S * I - a * E,
            a * E - gamma * I,
            gamma * I
        ])
    return f
