"""
Particles

Author: P. W. Talbot
"""

class Particle(object):
  def __init__(self,**kwargs):
    """
    Constructor
    Inputs:
      kwargs, dictionary of arguments
    Outputs:
      None
    """
    self.position = kwargs.get('position',[0,0,0])
    self.velocity = kwargs.get('momentum',[1,1,0])
    self.history = {}

  def updatePosition(self,dt,t):
    """
    Used to update position of particle.
    Inputs:
      dt: float, timestep to update through
      t: float, time at which the particle ends at position
    Outputs:
      None
    """
    for dim in range(3):
      if not self.checkForCollision():
        self.position[0] += dt*self.velocity[0]
    self.history[t] = self.position[:]

  def checkForCollision(self):
    """
    Checks other objects for collision. Probably belongs somewhere else.
    Inputs:
      None
    Outputs:
      None
    """
    #TODO implement
    return False

