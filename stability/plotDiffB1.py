import tfs
import matplotlib.pyplot as plt
import numpy as np

BETX_FILE = '/getbetax_free.out'
BETY_FILE = '/getbetay_free.out'
BETX_MDL = 'BETXMDL'
BETY_MDL = 'BETYMDL'

#betx1 = tfs.read("getbetax1_free.out", index="NAME")
#betx2 = tfs.read("getbetax2_free.out", index="NAME")
#betx1.rename(columns = {'BETXMDL':'newModel'}, inplace = True)

#diff_betx = betx1 - betx2
#diff_betx['S'] = betx1['S']
#diff_betx['BETXMDL'] = betx1['BETXMDL']
#print(diff_betx)

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
#/user/slops/data/LHC_DATA/OP_DATA/Betabeat/2022-05-29/
# 5_files_tct_symmetrical_beam1
# 30cm_tct_after_nlo_seq_played_for_tct
## 4_files_no_xing_no_sep_half_rf
# 04-47-48_NORMALANALYSIS_SUSSIX_11_ForOptics
#ref_folder = 'LHCB1/Results/5_files_tct_symmetrical_beam1/'
#'LHCB1/Results/30cm_tct_after_nlo_seq_played_for_tct',
compNum = 1
if compNum == 0: 
	max_min = 0.08
	ref_folder = 'LHCB1/Results/30cm_5files_noXing_Ip1_ip5_but_withSeparation/'
	ref_name   = '28th may with pre-cycle'
	beam = "Beam 1"
	comp_folders = ['LHCB1/Results/4_files_no_xing_no_sep_half_rf'
	,'LHCB1/Results/04-47-48_NORMALANALYSIS_SUSSIX_11_ForOptics', 'LHCB1/Results/b1_shift14.5_5kicks_first_analysis']
	comp_names = ["Half RF", "No Pre-Cyle", 'Pre-cyle 20h after']
	
#01-46-22_import_B1_New_Fill_For_Coupling_Correction
if compNum == 1:
	max_min = 0.08
	ref_folder = 'LHCB1/Results/01-56-56_import_15-52-52_import_03-16-23_import_b1_30cm_onmomentum_with_if/'
	ref_name   = '9th after Pre-cyle + De-Gauss'
	beam = "Beam 1"
	output_name = "9th2First"
	comp_folders = []
	comp_names = ["1st June only local" ]
	comp_folders.append('/user/slops/data/LHC_DATA/OP_DATA/Betabeat/2022-06-01/LHCB1/Results/B1_only_local_corr_right_model/')
	startPath = '/user/slops/data/LHC_DATA/OP_DATA/Betabeat/2022-05-29/'	
	ref_folder =  startPath  + ref_folder

if compNum == 2:
	max_min = 0.05
	ref_folder = 'LHCB1/Results/5_files_tct_symmetrical_beam1/'
	ref_name   = 'TCT symmetrical'
	beam = "Beam 1"
	output_name = "tct_movement"

	comp_folders = ['LHCB1/Results/30cm_tct_after_nlo_seq_played_for_tct/']
	comp_names = ["TCT moved with NLO seq"]
	startPath = '/user/slops/data/LHC_DATA/OP_DATA/Betabeat/2022-05-29/'	
	for i in range(0, len(comp_folders)):
		comp_folders[i] = startPath + comp_folders[i]
	ref_folder =  startPath  + ref_folder


if compNum == 3:
	max_min = 0.08
	ref_folder = 'LHCB1/Results/01-46-22_import_B1_New_Fill_For_Coupling_Correction/'
	ref_name   = '26th (No pre-cycle)'
	beam = " (Beam 1)"
	output_name = "ref26th_no_pre"
	comp_folders = ['LHCB1/Results/01-56-56_import_15-52-52_import_03-16-23_import_b1_30cm_onmomentum_with_if/', 'LHCB1/Results/4_files_no_xing_no_sep_half_rf'
	,'LHCB1/Results/04-47-48_NORMALANALYSIS_SUSSIX_11_ForOptics', 'LHCB1/Results/b1_shift14.5_5kicks_first_analysis']
	comp_names = ["9th after Pre-cyle + De-Gauss", "29th Pre-cyle + (Q1-Q4 off) + Half RF", "29th No Pre-Cyle", '29th Pre-cyle + (Q1-Q4 off) + (evening) after', '1st June 12h at injection']
	startPath = '/user/slops/data/LHC_DATA/OP_DATA/Betabeat/2022-05-29/'	
	for i in range(0, len(comp_folders)):
		comp_folders[i] = startPath + comp_folders[i]
	comp_folders.append('/user/slops/data/LHC_DATA/OP_DATA/Betabeat/2022-06-01/LHCB1/Results/B1_only_local_corr_right_model/')
	ref_folder =  startPath  + ref_folder
if compNum == 4:
	max_min = 0.08
	ref_folder = '/user/slops/data/LHC_DATA/OP_DATA/Betabeat/2022-05-10/LHCB1/Results/B1_30cm_on_off_momentum/'
	ref_name   = '10th (No pre-cycle) + global Corr'
	beam = " (Beam 1)"
	output_name = "ref10th_no_pre_global"
	comp_folders = ['/user/slops/data/LHC_DATA/OP_DATA/Betabeat/2022-06-01/LHCB1/Results/B1_with_global_corr']
	comp_names = ["1st June 12h at injection global Corr"]


#LHCB2/Results/00-52-59_import_16-11-17_import_03-17-18_import_5kicks_30cm/ #9th May
#LHCB2/Results/00-53-26_import_b2_30cm_nocorrinarcs/ #26th pre or not pre
#B2_29May_IP15-xingremoved-sepin #Pre cycle
#B2_29May_noprecycle_IP15-xingremoved-sepin #No Pre

for i in range(0, len(comp_folders)):
	print(comp_folders[i])
	betx_diff = get_pd_diff(ref_folder, comp_folders[i], 'X')
	bety_diff = get_pd_diff(ref_folder, comp_folders[i], 'Y')

	fig , (ax1,ax2) = plt.subplots(2)
	ax1.set_title("Ref is " + ref_name + "\n compared to \n " + comp_names[i] + "\n" + beam)
	ax1.errorbar(betx_diff["S"],betx_diff['beat'],yerr=betx_diff['errorbar'],  fmt='.k')
	ax2.errorbar(bety_diff["S"],bety_diff['beat'],yerr=bety_diff['errorbar'],  fmt='.k')
	ax1.set_ylim([-max_min, max_min])
	ax2.set_ylim([-max_min, max_min])
	ax2.set_xlabel("S [m]")
	ax1.set_ylabel("Horizontal")
	ax2.set_ylabel("Vertical")

	plt.tight_layout()
	plt.savefig(output_name + str(i) + ".png" )
	#plt.show()
#ax1.set_xlabel(r"$\textrm{S [m]}$")
#ax1.set_ylabel(r"$\frac{\beta_{x, OFF}-\beta_{x, ON}}{\beta_{x, OFF}}$")






