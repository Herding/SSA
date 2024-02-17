import numpy as np


class Gillespie():
    def __init__(self, species, reactions, timesteps=60) -> None:
        self._species = species
        self._reactions = reactions
        self._timesteps = timesteps
    
    @property
    def propensity(self):
        react_species = [tuple(self._species[i] for i in r.species) for r in self._reactions]
        return [r.propensity(*s) * r.rate for s, r in zip(react_species, self._reactions)]
    
    def update(self, reaction):
        args = (self._species[i] for i in reaction.species)
        reacted_species = reaction.react(*args)

        if isinstance(reacted_species, tuple):
            for idx, s in enumerate(reaction.species):
                self._species[s] = reacted_species[idx]
        else:
            self._species[reaction.species[0]] = reacted_species
    
    def react(self, r):
        propensity = np.asarray(self.propensity).cumsum() / sum(self.propensity)
        idx = 0

        for alpha in propensity:
            idx += 1
            if alpha > r:
                break
        
        self.update(self._reactions[idx - 1])
        return self._species.copy()
    
    def simulate(self, species=None):
        self._species = self._species if species is None else species
        
        alpha = sum(self.propensity)
        generate_next_step = np.vectorize(lambda r: np.log(1 / r) / alpha)

        samples4tau = np.random.rand(self._timesteps)
        tau = generate_next_step(samples4tau)
        timesteps = tau.cumsum()
        timesteps = timesteps[timesteps <= self._timesteps]

        samples4react = np.random.rand(len(timesteps))
        sim = [self._species.copy()]
        sim.extend([self.react(r) for r in samples4react])
        
        if timesteps[-1] < self._timesteps:
            sim.append(self._species.copy())
        
        return sim
    
    def visual(self):
        raise NotImplementedError