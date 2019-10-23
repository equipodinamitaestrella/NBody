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
from matplotlib.animation import FuncAnimation
import time
import matplotlib.animation as animation

if __name__ == '__main__':

    jupyter = Body(np.array([0, 0, 0]), np.array([0, 0, 0]), 1.898e27)
    io = Body(np.array([0, 422000000, 0]), np.array([17334, 0, 0]), 8.94e22)
    europe = Body(np.array([0, 671000000, 0]), np.array([13740, 0, 0]), 4.80e22)
    ganymede = Body(np.array([0, 1070000000, 0]), np.array([10880, 0, 0]), 1.48e23)
    callilsto = Body(np.array([0, 1883000000, 0]), np.array([8204, 0, 0]), 1.08e23)

    dt = 1 #sec
    lenTime = 3600*24*8 #sec

    n_steps = int(lenTime/dt)
    print(n_steps)
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=3600)
    particles = [jupyter, io, europe, ganymede, callilsto]
    jupyter_moons = Potential(particles, dt)
    x = []
    y = []

    skip = 0
    start = time.time()
    save = False
    for t in range(1, n_steps):
        if skip == 1500:
            skip = 0
            save = True
            print((t*100)/n_steps, "%")    
        system = jupyter_moons.integrate(float(t)*dt, save)
        save = False
        skip += 1

    stop = time.time()
    print(stop-start)
    print("plot?")

    step = 0
    i = 0
    def animate(time):
        c = ['g', 'r', 'b', 'c', 'm']
        global i
        global step
        if step >= len(particles[0].history_channel):
            return
        trajectory = dynamicPLot3d(system, particles,step)
        step+=1
        for j in range(trajectory.shape[0]):
            anima = ax.scatter(trajectory[j][0], trajectory[j][1], trajectory[j][2], marker='o', c = c[i])
            i = (i+1)%len(c)
        return anima
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    anim = FuncAnimation(fig, animate,
                               save_count=n_steps, interval=5)
    plt.show()
    anim.save('animation.mp4', writer=writer)
