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

G = 6.674e-11 # for CGS

class Body:
	def __init__(self, pos, vel, mass, acc=np.array([0,0,0]), dt=1, F=np.array([0,0,0])):
		# pos and vel must be numpy arrays  
		self.pos=pos
		self.vel=vel
		self.mass=mass
		self.acc=acc
		self.dt=dt
		self.F=F
		self.history_channel = [pos]
		self.time = [0.0]

	def __repr__(self):
		return f'Body(pos:{self.pos}, vel:{self.vel}, acc:{self.acc}, mass:{self.mass})'
	
	def computeR(self,p1):
		# Compute distance between objects
		return np.linalg.norm(self.pos-p1)
	
	def computeU(self,p1):
		# U is a numpy array in the direction of the other Body object
		return p1-self.pos
	
	def integrate(self, B):
		# B is a Body object
		# t_delta is a scalar for transpired time
		r = self.computeR(B.pos)
		u = self.computeU(B.pos)
		self.F = (G*B.mass*self.mass/(r**3))*u
		self.acc = (G*B.mass/(r**3))*u
		self.vel = self.vel + self.acc*self.dt
		self.pos = self.pos + self.vel*self.dt
		
	def update_position(self, time, save):
		self.pos = self.pos + self.vel*self.dt
		if save:
			self.time.append(time)
			self.history_channel.append(self.pos)
		
	def getKineticEnergy(self):
		k = 0.5*self.mass*np.linalg.norm(self.vel)
		return k
	
	def computeV(self, B):
		# B is a Body object
		# t_delta is a scalar for transpired time
		r = self.computeR(B.pos)
		u = self.computeU(B.pos)
		F = (G*B.mass*self.mass/(r**3))*u
		acc = (G*B.mass/(r**3))*u
		vel = acc*self.dt
		return vel
		
	def updateV(self, v):
		self.vel=self.vel + v
		
	def getPos(self):
		return self.pos

	def getVel(self):
		return self.vel
	
	def setdt(self,dt):
		self.dt=dt
		
	def getTrajectory(self):
		return self.time, self.history_channel
		
class Potential: # Calculate all forces between all particles and add them for each one to determine the total force
	def __init__(self, system, dt):
		self.system=system # set of Body objects
		self.dt=dt
	
	def integrate(self, time, save):
		for particle in self.system:
			for other in self.system:
				if other!=particle:
					velocity = particle.computeV(other)
					particle.updateV(velocity)
		for particle in self.system:
			particle.update_position(time, save)
			
		return self.system


if __name__ == '__main__':
	p0 = np.array([0.0, 0.0, 0.0]) #m
	v0 = np.array([1.0, 1.0, 1.0]) #m/s
	m = 1.0 #kg

	p1 = np.array([10.0, 0.0, 0.0]) #m
	v1 = np.array([0.0, 0.0, 0.0]) #m/s
	m1 = 1e24 #kg


	dt = 1.0 #sec
	G = 6.674e-11

	A = Body(p0, v0, m)
	A.setdt(dt)
	B = Body(p1, v1, m1)
	twoBody = Potential([A,B], dt)
	x=[]
	y=[]
	for t in range(1,100):
		system = twoBody.integrate(float(t)*dt)
