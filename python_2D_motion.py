import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# Time array
t0=0
t_end=10
dt=0.02
t=np.arange(t0,t_end+dt,dt)

# Create the x array
x_i=1000 # [m]
a=200
x=x_i+a*t

# Create the y array (landing)
y_i=1500 # [m]
b=-100
y=y_i+b*t

############################## ANIMATION ##############################
frame_amount=len(t)
def update_plot(num):

    return


# Set up the figure properties
fig=plt.figure(figsize=(16,9),dpi=80,facecolor=(0.8,0.8,0.8))
gs=gridspec.GridSpec(2,2)

# Airplane motion
ax0=fig.add_subplot(gs[0,:],facecolor=(0.9,0.9,0.9))

# Draw an airplane
plane_1,=ax0.plot([],[],'k',linewidth=10)
plane_2,=ax0.plot([],[],'w',linewidth=5)
plane_3,=ax0.plot([],[],'k',linewidth=4)
plane_4,=ax0.plot([],[],'w',linewidth=3)

plane_trajectory,=ax0.plot([],[],'--k',linewidth=2)

plt.xlim(0,max(x))
plt.ylim(0,max(y)+100)
plt.xlabel('position_x [m]',fontsize=15)
plt.ylabel('position_y [m]',fontsize=15)
plt.grid(True)


plt.show()
