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

    # Draw a plane
    plane_1.set_data([x[num]-40,x[num]+20],[y[num],y[num]])
    plane_2.set_data([x[num]-15,x[num]+10],[y[num],y[num]])
    plane_3.set_data([x[num]-45,x[num]-30],[y[num]+80,y[num]])
    plane_4.set_data([x[num]-55,x[num]-40],[y[num],y[num]])

    # Trajectory
    plane_trajectory.set_data(x[0:num],y[0:num])

    # Connect plane with axes
    pos_x.set_data(t[0:num],x[0:num])
    pos_y.set_data(t[0:num],y[0:num])

    arrow_test=ax0.arrow(0,0,1000,500,
        length_includes_head=True,head_width=40,head_length=80,color='g',linewidth=2)
    arrow_test2=ax0.arrow(1000,500,1000,500,
        length_includes_head=True,head_width=40,head_length=80,color='b',linewidth=2)

    return plane_1,plane_2,plane_3,plane_4,plane_trajectory,pos_x,pos_y,arrow_test, \
        arrow_test2


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

# Position X vs time
ax1=fig.add_subplot(gs[1,0],facecolor=(0.9,0.9,0.9))
pos_x,=ax1.plot([],[],'-b',linewidth=3,label='X = '+str(x_i)+ ' + '+str(a)+'t')
plt.xlim(t0,t_end)
plt.ylim(0,max(x))
plt.xlabel('time [s]',fontsize=15)
plt.ylabel('position_x [m]',fontsize=15)
plt.grid(True)
plt.legend(loc='lower right',fontsize='x-large')

# Position Y vs time
ax2=fig.add_subplot(gs[1,1],facecolor=(0.9,0.9,0.9))
pos_y,=ax2.plot([],[],'-b',linewidth=3,label='Y = '+str(y_i)+ ' + ('+str(b)+')t')
plt.xlim(t0,t_end)
plt.ylim(0,max(y)+100)
plt.xlabel('time [s]',fontsize=15)
plt.ylabel('position_y [m]',fontsize=15)
plt.grid(True)
plt.legend(loc='lower right',fontsize='x-large')

plane_ani=animation.FuncAnimation(fig,update_plot,
    frames=frame_amount,interval=20,repeat=True,blit=True)

plt.show()
