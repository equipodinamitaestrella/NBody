"""
main.py solve the n-body problem using newton
Copyright (C) 2019 Jorge Antonio Camarena Pliego (camarenapliego@gmail.com)
Keshava Tonathiu Sanchez Barbosa (keshava.t.s.b@gmail.com)
Stephany Dzoara Vargas Mier (stephanydvm@comunidad.unam.mx)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""

import numpy
from Body import *
from plott import *
import time

if __name__ == '__main__':
    sun = Body(np.array([0,0,0]), np.array([0,0,0]), 2e30)
    mercury = Body(np.array([0,5.7e10,0]), np.array([47000,0,0]), 3.285e23)
    venus = Body(np.array([0, 1.1e11, 0]), np.array([35000,0,0]), 4.8e24)
    earth = Body(np.array([0, 1.5e11, 0]), np.array([30000, 0, 0]), 6e24)
    mars = Body(np.array([0.0,2.2e11,0.0]), np.array([24000.0,0.0,0.0]), 2.4e24)
    jupiter = Body(np.array([0.0, 7.7e11, 0.0]), np.array([13000, 0.0, 0.0]), 1e28)
    saturn = Body(np.array([0,1.4e12,0]), np.array([9000,0,0]), 5.7e26)
    uranus = Body(np.array([0,2.8e12,0]), np.array([6835,0,0]), 8.7e25)
    neptune = Body(np.array([0,4.5e12,0]), np.array([5477,0,0]), 1e26)
    pluto = Body(np.array([0,3.7e12,0]), np.array([4748,0,0]), 1.3e22)

    dt = 1 #sec
    lenTime = 3600*24*90 #sec

    n_steps = int(lenTime/dt)
    print(n_steps)

    """
    p0 = np.array([0.001, 0.0, 0.0]) #m
    v0 = np.array([0.0, 0.0, 0.0]) #m/s
    m = 1e1 #kg

    p1 = np.array([0.0, 0.0, 0.0]) #m
    v1 = np.array([0.0, 0.0, 1e-3]) #m/s
    m1 = 1e1 #kg

    G = 6.674e-11

    A = Body(p0, v0, m)
    B = Body(p1, v1, m1)
    C = Body([0.0, 0.001, 0.0], [0.0, 0.0, 0.0], 1e1)

    particles = [A, B, C]
    twoB = Potential(particles, dt)

    #B.setdt(dt)
    """
    particles = [sun, mercury, venus, earth]
    solar_system = Potential(particles, dt)
    x = []
    y = []
    #v = []
    #a = []
    
    #x.append(0)
    #y.append(B.getPos()[0])
    #v.append(B.getVel()[0])
    #y.append(B.getPos())
    #v.append(B.getVel())
    #a.append(0.0)
    #v1 = B.getVel()[0]

    """
    for t in range(1, 100):
        lastX = B.getPos()[0]
        lastV = v1

        B.update_position(A)
        
        print(B.getPos())
        
        x.append(float(t)*dt)
        y.append(B.getPos()[0])
        v1 = (B.getPos()[0] - lastX)/B.dt
        v.append(v1)
        a.append((v1 - lastV)/B.dt)
    """

    """
    for t in range(1, 100):
        B.update_position(A)
        x.append(float(t)*dt)
        y.append(B.getPos())
    """

    """
    Sun_pos = np.array([0,0,0])
    Sun_mass = 1.989e30
    Earth_mass = 5.972e24
    Earth_pos = np. array([149600000000,0,0])
    Earth_vel = np.array([0,20000,0])
    Earth = Body(Earth_pos, Earth_vel, Earth_mass)
    Sun = Body(Sun_pos, np.array([0,0,0]), Sun_mass)
    planets=[Earth, Sun]
    solar_system = Potential(planets, 1e20)
    """
    skip = 0
    start = time.time()
    save = False
    for t in range(1, n_steps):
        if skip == 1000:
            skip = 0
            save = True
            print(t, n_steps)    
        system = solar_system.integrate(float(t)*dt, save)
        save = False
        skip += 1
        #system = solar_system.integrate(float(t)*1e20)

    stop = time.time()
    print(stop-start)
    #plot3d(x, y, v, a, A)
    print("plot?")
    dynamicPLot3d(system, particles)
