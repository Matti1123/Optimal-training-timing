import numpy as np
import matplotlib.pyplot as plt
from fitness_fatigue import fitness_fatigue


def test_fitness_fatigue():
    """
    Check that perfomance increases after a second training at t > t_peak.
    """
    
    w = np.zeros(100)
    w[0] = 1
    w[20] = 1
    p_star = 100
    n = np.arange(len(w))
    fitness,fatigue,performance = fitness_fatigue(p_star = p_star,w = w)
    
    assert performance[20+14] > performance[19], f" Fail: Peformance at t = 34 :{performance[20+14]} < {performance[19]}"
    print(f"Success: Peformance at t = 34 :{performance[20+14]} > {performance[19]}")

if __name__ == '__main__':
    test_fitness_fatigue()