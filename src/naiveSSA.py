import numpy as np


class NaiveSSA():
    def __init__(self, molecules, k, delta, samples=60) -> None:
        self._mol = molecules
        self._k = k
        self._delta = delta
        self._samples = samples

        if molecules * k * delta > 0.1:
            raise ValueError('A * k * Δt must less than 0.1')

    def react(self, random_sample):
        if random_sample < self._mol * self._k * self._delta:
            self._mol -= 1
            return self._mol + 1
        else:
            return self._mol
    
    def simulate(self):
        timepoints = np.linspace(0, self._samples, int(self._samples / self._delta))
        random_samples = np.random.rand(len(timepoints))
        sim = [self.react(r) for r in random_samples]
        
        return sim
    
    def visual(self):
        raise NotImplementedError