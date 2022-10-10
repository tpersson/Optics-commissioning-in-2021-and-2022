import tfs
import matplotlib.pyplot as plt
import numpy as np
path2ip1 = "twiss_on.tfs"
path2ip5 = "twiss_corr.tfs"
original = tfs.read(path2ip1, index="NAME")
q8_and_higher = tfs.read(path2ip5, index="NAME")
diff_x = q8_and_higher['BETX'] - original['BETX'] 
diff_y = q8_and_higher['BETY'] -  original['BETY'] 

diff_dx = original['DX'] - q8_and_higher['DX']
diff_dy = original['DY'] - q8_and_higher['DY']

plt.plot(original['S'], diff_x/original['BETX'],label="horizontal")
plt.plot(original['S'], diff_y/original['BETY'],label="vertical")
plt.legend()
plt.xlabel("S [m]")
plt.ylabel("beta-beat")
plt.show()
exit()
plt.figure()
plt.plot(original['S'], diff_dx)
plt.plot(original['S'], diff_dy)
plt.figure()

plt.plot(original['S'], q8_and_higher['BETX'])
plt.plot(original['S'], q8_and_higher['BETY'])

#plt.xlim([-0.15,0.15])
#plt.ylim([0.20, 0.65])
plt.show()
