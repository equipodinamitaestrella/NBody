#!/usr/bin/env python3

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

You eshould have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""

# Graficar la trayectoria de un campo vectorial(streaming)
# Necesitamos
#  1: posicion x,y,z
#  2: conjunto de ternas(vectores) que simbolizan la trayectoria de cada particula

import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

k = 9e9 #Nwm²cou^⁻2 Aire en la tierra

# u = position vector
# q = charge
# v = position vector of q

def ElectrostaticField(u,q,X,Y):
    q1 = -1.0
    x0 = u[0]
    y0 = u[1]
    
    # v-u = v[0]-u[0], v[1]-u[1]
    r_vec_x = X - x0
    r_vec_y = Y - y0
    #r_vec = v-u
    
    r = np.hypot(r_vec_x,r_vec_y)
    #r = np.sqrt(r_vec.dot(r_vec))
    
    E0 = [k * (q / r**3) * (r_vec_x), k * (q / r**3) * (r_vec_y)]
    
    q1 = 1.0
    x0 = u[0] + 1.0
    y0 = u[1]
    
    # v-u = v[0]-u[0], v[1]-u[1]
    r_vec_x = X - x0
    r_vec_y = Y - y0
    #r_vec = v-u
    
    r = np.hypot(r_vec_x,r_vec_y)
    #r = np.sqrt(r_vec.dot(r_vec))
    
    E = [E0[0] + k * (q / r**3) * (r_vec_x), E0[1] + k * (q / r**3) * (r_vec_y)]
    
    return E
    
u = np.array([-0.5,0])
q = 1.0
#v = np.array([1e-6,0,0])

nx, ny = 64, 64
x = np.linspace(-1,1,nx)
y = np.linspace(-1,1,ny)
X, Y = np.meshgrid(x,y)

"""Ex = []
Ey = []
for a in x:
    for b in y:"""
[Ex, Ey] = ElectrostaticField(u,q,X,Y)
        #Ex.append(E[0])
        #Ey.append(E[1])

fig = plt.figure()
ax = fig.add_subplot(111)
ax.streamplot(x, y, Ex, Ey, linewidth=1, cmap=plt.cm.inferno, density=2, arrowstyle="->", arrowsize=1.5)
plt.show()

#F = ElectrostaticForce(u,q,v)
print(F)
