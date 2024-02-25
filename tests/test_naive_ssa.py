import sys, os
sys.path.append(os.path.curdir)

from src.ssa.naiveSSA import NaiveSSA

naive_ssa = NaiveSSA(20, 0.1, 0.001, samples=10)

simulate_times = 2
simulate_results = [naive_ssa.simulate() for _ in range(simulate_times)]

print(simulate_results[0])
print(simulate_results[1])