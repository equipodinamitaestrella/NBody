import numpy as np

class Body:
	def __init__(self, pos, vel):
		# pos and vel must be numpy arrays  
		self.pos=pos
		self.vel=vel
		return self
	
	def update_position(self, t_delta):
		# t_delta is a scalar for transpired time
		self.pos = self.pos + self.vel*t_delta
