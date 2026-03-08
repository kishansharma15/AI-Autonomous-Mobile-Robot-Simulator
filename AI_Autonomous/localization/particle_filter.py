import random

class ParticleFilter:

    def __init__(self,n):

        self.particles = [(random.random(),random.random()) for _ in range(n)]

    def predict(self):

        self.particles = [(p[0]+random.uniform(-0.1,0.1),
                           p[1]+random.uniform(-0.1,0.1))
                          for p in self.particles]

    def estimate(self):

        x = sum(p[0] for p in self.particles)/len(self.particles)
        y = sum(p[1] for p in self.particles)/len(self.particles)

        return x,y