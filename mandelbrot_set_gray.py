from __future__ import division
from numpy import empty
from pylab import imshow,gray,show, savefig,colorbar
from math import sqrt
##
side = 4
points = 500
spacing = side/points
step = 500
z = complex(0, 0)
s = empty([points+1,points+1],float)
##
for m in range(points+1):
    x = -2+spacing*m
    for n in range(points+1):
        y = -2+spacing*n
        c = complex(x,y)
        z = complex(0, 0)
        for k in range(step):
            z = z**2+c
            if abs(z)>2:
                s[n][m] = 0      
                break
        else:
            s[n][m] = 1
###
imshow(s,origin="lower",extent=[-side/2,side/2,-side/2,side/2])
colorbar()
gray()
savefig('fig1.pdf')