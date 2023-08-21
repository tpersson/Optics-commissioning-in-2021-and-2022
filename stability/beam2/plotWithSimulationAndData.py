import tfs
import matplotlib.pyplot as plt
import numpy as np

BETX_FILE = '/getbetax_free.out'
BETY_FILE = '/getbetay_free.out'
BETX_MDL = 'BETXMDL'
BETY_MDL = 'BETYMDL'

def get_pd_diff(inref, incomp, plane):
	if(plane == 'X'):
		f_name = BETX_FILE
		m_name = BETX_MDL
		c_name = "BETX"
		e_name = "ERRBETX"
	else:
		f_name = BETY_FILE
		m_name = BETY_MDL
		c_name = "BETY"
		e_name = "ERRBETY"

	bet_ref = tfs.read(inref + f_name, index="NAME")
	bet_comp = tfs.read(incomp + f_name, index="NAME")
	diff_bet = bet_ref - bet_comp
	diff_bet['S'] = bet_ref['S']
	diff_bet[m_name] = bet_ref[m_name]
	diff_bet['err_comp'] = bet_comp[e_name]
	diff_bet['err_ref']  = bet_ref[e_name]
	diff_bet['errorbar'] = np.sqrt(diff_bet['err_comp']**2 + diff_bet['err_ref']**2)/diff_bet[m_name]
	diff_bet['beat'] = diff_bet[c_name]/diff_bet[m_name]
	return diff_bet

plt.rcParams.update({'font.size': 16})

max_min = 0.15
ref_folder = ['/user/slops/data/LHC_DATA/OP_DATA/Betabeat/2022-05-26/LHCB2/Results/b2_30cm_nocorrinarcs/', '/afs/cern.ch/eng/sl/lintrack/LHC_commissioning2022/COM_2022_06_17_vertical_vaistShift/30cm_delta_energy/']
ref_name   = '26May'
beam = "LHCB2"
output_name = "plot_BB_B2_9May-vs-26May_DIFF"
comp_folders = ['/user/slops/data/LHC_DATA/OP_DATA/Betabeat/2022-05-08/LHCB2/Results/5kicks_30cm/',  '/afs/cern.ch/eng/sl/lintrack/LHC_commissioning2022/COM_2022_06_17_vertical_vaistShift/30cm_on_off_momentum_b2/']


fig , (ax1,ax2) = plt.subplots(2)
plt.subplots_adjust(top=0.7)
markers = ['.k', '*g']
labels = ['Diff 9th May - 26th May', 'Diff Relative Energy trim $10^{-4}$', 'Diff Simulate Relative Energy trim $10^{-4}$']
for i in range(0, len(comp_folders)):
	print(comp_folders[i] , "  ", ref_folder[i])
	betx_diff = get_pd_diff(ref_folder[i], comp_folders[i], 'X')
	bety_diff = get_pd_diff(ref_folder[i], comp_folders[i], 'Y')
	print(i, betx_diff)

	#ax1.set_title("Ref is " + ref_name + "\n compared to \n " + comp_names[i] + "\n" + beam)
	ax1.errorbar(betx_diff["S"],betx_diff['beat'],yerr=betx_diff['errorbar'],  fmt=markers[i], label=labels[i])
	ax2.errorbar(bety_diff["S"],bety_diff['beat'],yerr=bety_diff['errorbar'],  fmt=markers[i])

	plt.savefig(output_name + str(i) + ".png" )
	
path2ip1 = "twiss_on.tfs"
path2ip5 = "twiss_corr.tfs"
original = tfs.read(path2ip1, index="NAME")
q8_and_higher = tfs.read(path2ip5, index="NAME")
diff_x = q8_and_higher['BETX'] - original['BETX'] 
diff_y = q8_and_higher['BETY'] -  original['BETY'] 

diff_dx = original['DX'] - q8_and_higher['DX']
diff_dy = original['DY'] - q8_and_higher['DY']

ax1.plot(original['S'], diff_x/original['BETX'],'s',zorder=3, label=labels[2])
ax2.plot(original['S'], diff_y/original['BETY'],'s',zorder=3)

ax1.set_ylim([-max_min, max_min])
ax2.set_ylim([-max_min, max_min])
ax2.set_xlabel("S [m]")
ax1.set_ylabel(r"$\frac{\Delta \beta _x}{\beta _{x,ref}}$")
ax2.set_ylabel(r"$\frac{\Delta \beta _y}{\beta _{y,ref}}$")
#fig.legend(bbox_to_anchor = (0.9, 1.0))


plt.tight_layout()
plt.savefig("all1.png" )
plt.show()

#ax1.set_xlabel(r"$\textrm{S [m]}$")
#ax1.set_ylabel(r"$\frac{\beta_{x, OFF}-\beta_{x, ON}}{\beta_{x, OFF}}$")

