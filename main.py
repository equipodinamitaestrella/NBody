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

if __name__ == '__main__':
    p0 = np.array([5e-2, 1e-3, 0.0]) #m
    v0 = np.array([0.0, 0.0, 0.0]) #m/s
    m = 1e7 #kg

    p1 = np.array([0.0, 0.0, 0.0]) #m
    v1 = np.array([1.0, 0.0, 0.0]) #m/s
    m1 = 1e7 #kg


    dt = 0.001 #sec
    G = 6.674e-11

    A = Body(p0, v0, m)
    B = Body(p1, v1, m1)

    particles = [A,B]
    twoB = Potential(particles, dt)

    #B.setdt(dt)

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

    for t in range(1, 100):
        system = twoB.integrate(float(t)*dt)

    #plot3d(x, y, v, a, A)

    dynamicPLot3d(system, particles)