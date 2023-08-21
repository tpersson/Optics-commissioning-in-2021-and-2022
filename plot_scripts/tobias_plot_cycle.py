
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
inj = 0
ramp_s = 1
ramp_corr_out = 1.8
ramp_2m = 3.5
ramp_e = 4
sq_e = 5
rot_e = 5.5
coll_m = 6
coll_e = 7

time_e = np.array([inj, ramp_s, ramp_e, sq_e, rot_e, coll_e])
time_b = np.array([inj, ramp_s, ramp_2m, ramp_e, sq_e, rot_e, coll_e])
time_c = np.array([inj, ramp_s, ramp_corr_out, ramp_2m, ramp_e, sq_e, rot_e, coll_m, coll_e])


energy = np.array([450, 450, 6800,6800,6800,6800])
b_star = np.array([11, 11, 2, 2,1.2,1.2, 0.3])
n_corr = np.array([1,1,0,0,1,1,1,0,-1])

fig, ax1 = plt.subplots()
# plot line chart on axis #1
p1, = ax1.plot(time_e, energy) 
ax1.set_ylabel('Energy')
ax1.set_ylim(0, 7000)
#ax1.legend(['Energy'], loc="upper left")
ax1.yaxis.label.set_color(p1.get_color())
ax1.yaxis.label.set_fontsize(14)
ax1.tick_params(axis='y', colors=p1.get_color(), labelsize=14)
ax1.set_xlabel('Time in cycle ', size=14)
#ax1.tick_params(bottom = False)
ax1.set_xticks([])
# set up the 2nd axis
ax2 = ax1.twinx() 


# plot bar chart on axis #2
p2, = ax2.plot(time_b, b_star, color='orange')
ax2.grid(False) # turn off grid #2
ax2.set_ylabel(r'$\beta^*$')
ax2.set_ylim(0, 12)
#ax2.legend(['beta star'], loc="upper center")
ax2.yaxis.label.set_color(p2.get_color())
ax2.yaxis.label.set_fontsize(14)
ax2.tick_params(axis='y', colors=p2.get_color(), labelsize=14)

# set up the 3rd axis
ax3 = ax1.twinx()
# Offset the right spine of ax3.  The ticks and label have already been placed on the right by twinx above.
ax3.spines.right.set_position(("axes", 1.15))
# Plot line chart on axis #3
p3, = ax3.plot(time_c, n_corr, color='red')
ax3.grid(False) # turn off grid #3
ax3.set_ylabel('New corrections')
ax3.set_ylim(0, 2)
#ax3.legend(['New corrections'], loc="upper right")
ax3.yaxis.label.set_color(p3.get_color())
ax3	.yaxis.label.set_fontsize(14)
ax3.add_patch(Rectangle((ramp_corr_out, 0), ramp_2m-ramp_corr_out, 6,
             facecolor = 'green',
             alpha=0.3,
             fill=True,
             lw=5))
ax3.add_patch(Rectangle((coll_m, 0), 1, 6,
             facecolor = 'green',
             alpha=0.3,
             fill=True,
             lw=5))
ax3.tick_params(axis='y', colors=p3.get_color(), labelsize=14)
plt.tight_layout()
plt.show()

