#!/usr/bin/env python3
#
# Body.py implements Body class
# Copyright (C) 2019 Jorge Antonio Camarena Pliego (camarenapliego@gmail.com)
# Keshava Tonathiu Sanchez Barbosa (keshava.t.s.b@gmail.com)
# Stephany Dzoara Vargas Mier (stephanydvm@comunidad.unam.mx)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import numpy as np
import math

G = 6.674e-8 # for CGS

class Body:
	def __init__(self, pos, vel, mass, acc=np.array([0,0,0])):
		# pos and vel must be numpy arrays  
		self.pos=pos
		self.vel=vel
		self.mass=mass
		self.acc=acc
	
	def __repr__(self):
		return f'Body(pos:{self.pos}, vel:{self.vel}, acc:{self.acc}, mass:{self.mass})'
	
	def computeR(self,p1):
		# Compute distance between objects
		return np.linalg.norm(self.pos-p1)
	
	def computeU(self,p1):
		# U is a numpy array in the direction of the other Body object
		return p1-self.pos
	
	def update_position(self, t_delta, p1, m1):
		# t_delta is a scalar for transpired time
		r = self.computeR(p1)
		u = self.computeU(p1)
		self.vel = self.vel+(G*m1*t_delta/(r**3))*u
		self.pos = self.pos + self.vel*t_delta
		
	def getKineticEnergy(self):
		k = 0.5*self.mass*np.linalg.norm(self.vel)
		return k
		
	def getPos(self):
		return self.pos

	def getVel(self):
		return self.vel


#testing:
'''
body=Body(np.array((1,1,1)), np.array((1,1,1)))
print(body)
body.update_position(2)
print(body)
'''
