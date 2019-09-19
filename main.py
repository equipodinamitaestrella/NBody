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
    p0 = np.array([1.0, 0.0, 0.0]) #m
    v0 = np.array([0.0, 0.0, 0.0]) #m/s
    m = 1.0 #kg

    p1 = np.array([0.0, 0.0, 0.0]) #m
    v1 = np.array([1.0, 0.0, 0.0]) #m/s
    m1 = 1 #kg


    dt = 0.01 #sec
    G = 6.674e-11

    A = Body(p0, v0, m)
    B = Body(p1, v1, m1)

    B.setdt(dt)

    x = []
    y = []
    v = []
    
    x.append(0)
    y.append(B.getPos()[0])
    v.append(B.getVel()[0])

    lastX = B.getPos()[0]

    for t in range(1, 100):
        #A.update_position(dt, p1, m1)
        lastX = B.getPos()[0]
        B.update_position(A)
        print(B.getPos())
        x.append(float(t)*dt)
        y.append(B.getPos()[0])
        v.append((B.getPos()[0] - lastX)/B.dt)
    
    plott(x, y, v)