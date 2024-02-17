import sys
sys.path.append('../')

from src import reaction
from src.gillespieSSA import Gillespie


species = {
    'A': 0,
}

reactions = [
    reaction(species=['A'], propensity=lambda x: x, react=lambda x: x - 1, rate=0.1),
    reaction(species=['A'], propensity=lambda x: 1, react=lambda x: x + 1, rate=1)
]

ssa = Gillespie(species.copy(), reactions, timesteps=100)

simulate_times = 2
simulate_results = [ssa.simulate(species.copy()) for _ in range(simulate_times)]

print(simulate_results[0])
print(simulate_results[1])