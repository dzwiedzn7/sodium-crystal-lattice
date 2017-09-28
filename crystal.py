

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA


def vectors_to_angles(vec1,vec2,vec3):
    alpha =   np.arccos(np.dot(vec1,vec2)/(LA.norm(vec1)*LA.norm(vec2)))
    beta =   np.arccos(np.dot(vec2,vec3)/(LA.norm(vec2)*LA.norm(vec3)))
    return (np.degrees(alpha),np.degrees(beta))

angles = vectors_to_angles([0,0,1],[1,1,1],[1,0,0])
print angles

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect("equal")

count = 2
# draw cube
for x in range(-count,count+1):
    for y in range(-count,count+1):
        for z in range(-count,count+1):
            #if x == 0 and y == 0 and z == 0:
            if ((x+y+z+3*count)%2) == 0:
                ax.scatter(*zip([x,y,z]), color="r")
            else:
                ax.scatter(*zip([x,y,z]), color="b")
	        #ax.scatter([0],[0],[0], color="g")
	        #ax.scatter([0],[0],[0], s=100)
            #ax.scatter(*zip([0,0,0]), s=100)
            ax.scatter(*zip([0,0,0]),color='g',s=100)

ax.view_init(*angles)
plt.show()

"""
###shot a series of pictures at given angle,angle changes from 0 to 360 every 60
for ii in xrange(0,360,60):
        ax.view_init(elev=ii, azim=ii)
        plt.savefig("movie%d.png" % ii)


camera = dict(
    up=dict(x=0, y=0, z=1),
    center=dict(x=0, y=0, z=0),
    down=dict(x=0.1, y=2.5, z=0.1)
)

"""
