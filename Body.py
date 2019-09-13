import numpy as np

class Body:
	def __init__(self, pos, vel):
		# pos and vel must be numpy arrays  
		self.pos=pos
		self.vel=vel
	
	def __repr__(self):
		return f'Body(pos:{self.pos}, vel:{self.vel})'
	
	def update_position(self, t_delta):
		# t_delta is a scalar for transpired time
		self.pos = self.pos + self.vel*t_delta


#testing:
'''
body=Body(np.array((1,1,1)), np.array((1,1,1)))
print(body)
body.update_position(2)
print(body)
'''
