#!/usr/bin/python3

import numpy
import matplotlib.pyplot as plt

ax = plt.subplot()
#ax.set_xlabel("x")
ax.set_xlim(0.0,1.0)
#ax.set_ylabel("y")
ax.set_ylim(4.15,4.4)

# The psi function
X=numpy.array( [0.0, 0.22, 0.25, 0.47, 0.5, 0.72,0.75, 1.0] )
Y=numpy.array( [4.2, 4.2,  4.25, 4.25, 4.3, 4.3, 4.35, 4.35] )
ax.plot( X, Y, color="blue" )

# The "corridors" though which psi must pass
for i in range(len(X)//2):
    y1 = Y[2*i]-1/32
    ax.plot( [0.0,1.0], [y1,y1], linestyle="dashed", linewidth="0.5", color="blue" )
ax.plot( [0.0,1.0], [y1+1/16,y1+1/16], linestyle="dashed", linewidth="0.5", color="blue" )

plt.savefig( "kat_psi1.png", dpi=300 )
plt.close()



ax = plt.subplot()
ax.set_xlim(0.1,0.6)
ax.set_ylim(0.5,2.5)

# The psi function
X=numpy.array( [0.0, 0.22, 0.25, 0.47, 0.5, 0.72] )
Y=numpy.array( [0.8, 0.8,  1.6,  1.6,  2.4, 2.4] )
ax.plot( X, Y, color="blue" )
# The corridor
h = 1.6
ax.plot( [0.25,0.47], [h-0.2,h-0.2], linestyle="dashed", linewidth="0.5", color="blue" )
ax.plot( [0.25,0.47], [h+0.2,h+0.2], linestyle="dashed", linewidth="0.5", color="blue" )

# The k+1 intervals
ax.axvspan( 0.2, 0.38, facecolor="red", alpha=0.2  )
ax.axvspan( 0.4, 0.58, facecolor="red", alpha=0.2  )

# The "corridors" for the 3 non-overlapping intervals in k+1
ax.axhspan( 1.65, 1.67, facecolor="red", alpha=0.8  )
ax.axhspan( 1.70, 1.72, facecolor="red", alpha=0.8  )
ax.axhspan( 1.75, 1.77, facecolor="red", alpha=0.8  )
    

plt.savefig( "kat_psi2.png", dpi=300 )
plt.close()



X1 = numpy.linspace( 0.0, 1.0, 100 )
X2 = numpy.linspace( 0.0, 1.0, 100 )

def Y(X1,X2):
    if X1 < 0.22:   y = 0.8
    elif X1 < 0.25: y = 0.8 + (X1-0.22)*80/3
    elif X1 < 0.47: y = 2*0.8
    elif X1 < 0.5:  y = 2*0.8 + (X1-0.47)*80/3
    elif X1 < 0.72: y = 3*0.8
    elif X1 < 0.75: y = 3*0.8 + (X1-0.72)*80/3
    else:           y = 4*0.8

    if X2 < 0.22:   y += 4 * 0.8
    elif X2 < 0.25: y += 4 * (0.8 + (X2-0.22)*80/3)
    elif X2 < 0.47: y += 4 * 2*0.8
    elif X2 < 0.5:  y += 4 * (2*0.8 + (X2-0.47)*80/3)
    elif X2 < 0.72: y += 4 * 3*0.8
    elif X2 < 0.75: y += 4 * (3*0.8 + (X2-0.72)*80/3)
    else:           y += 4 * 4*0.8

    #print( f"{X1} {X2} {y}" )
    return y


x,y = numpy.meshgrid(X1,X2)
z = numpy.array( [Y(x1,y1) for x1 in X1 for y1 in X2] ).reshape( x.shape )

ax = plt.subplot( projection="3d" )
ax.set_xlim(0.0,1.0)
ax.set_ylim(0.0,1.0)
ax.set_zlim(0.0,16.0)
ax.plot_surface(x,y,z,linewidth=0)
ax.view_init( azim=250 )
plt.savefig( "kat_psi3.png", dpi=300 )
