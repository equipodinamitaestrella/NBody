import numpy as np

class Body:
	def __init__(self, pos, vel):
		# pos and vel must be numpy arrays  
		self.pos=pos
		self.vel=vel
		return self
