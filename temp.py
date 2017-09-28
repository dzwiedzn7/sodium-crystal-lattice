"""
# draw sphere
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
ax.plot_wireframe(x, y, z, color="r")

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def gen_crystal_struct():
    var = True
    while var:
        insert = int(raw_input('insert lenght: '))
        if insert % 2 == 1:
            var = False
    lenght = range(- insert,insert + 1)
    for x in lenght:
        for y in lenght:
            for z in lenght:

    return np.array([[lenght],[lenght],[lenght]])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

struct = gen_crystal_struct()

ax.scatter(struct)
plt.show()

from visual import sphere,color

count = 2
R=0.5

for x in range(-count,count+1):
    for y in range(-count,count+1):
        for z in range(-count,count+1):
            if ((x+y+z+3*count)%2) == 0:
                sphere(pos=[x,y,z],radius=R,color=color.red)
            else:
                sphere(pos=[x,y,z],radius=R,color=color.blue)

from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d


class Arrow3D(FancyArrowPatch):

    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)

a = Arrow3D([0, 1], [0, 1], [0, 1], mutation_scale=20,
            lw=1, arrowstyle="-|>", color="k")
ax.add_artist(a)
plt.show()

"""
