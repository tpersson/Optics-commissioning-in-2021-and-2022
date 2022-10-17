#!/bin/bash
#!/bin/bash

# Plotting beta-beating for B1 after local corrections in IP5
ssh cs-ccr-optics1 /afs/cern.ch/eng/sl/lintrack/miniconda2/bin/python \
	/afs/cern.ch/eng/sl/lintrack/Beta-Beat.src/GetLLM/plot_export.py \
	--accel=LHCB1 \
	--path=/user/slops/data/LHC_DATA/OP_DATA/Betabeat/2022-05-02/LHCB1/Results/02-39-41_import_00-33-36_NORMALANALYSIS_SUSSIX_11,/user/slops/data/LHC_DATA/OP_DATA/Betabeat/2022-05-02/LHCB1/Results/b1_30cm_with_apj_corrs_32%_kicks \
	--folder=/afs/cern.ch/eng/sl/lintrack/LHC_commissioning2022/COM_2022_05_02_squeeze_local_corrections/plots/lhcb1_before_vs_after_localcorr.pdf \
	--plot=Beta_beat \
	--maxx=0.52 \
	--minx=-0.52 \
	--maxy=1.70 \
       	--miny=-1.35 \
	--hmaxx=26614.97265625 \
	--hminx=-0.3448531029978767 \
	--hmaxy=NaN \
       	--hminy=NaN \
       	--mainnode=Beta \
	--legendx=69.0 \
	--legendy=12.0 \
	--legendh=91.0 \
	--labels=B1_Before_LocalCorr,B1_After_LocalCorr

# Plotting beta-beating for B2 after local corrections in IP5
ssh cs-ccr-optics2 /afs/cern.ch/eng/sl/lintrack/miniconda2/bin/python \
	/afs/cern.ch/eng/sl/lintrack/Beta-Beat.src/GetLLM/plot_export.py \
	--accel=LHCB1 \
	--path=/user/slops/data/LHC_DATA/OP_DATA/Betabeat/2022-05-02/LHCB2/Results/02-38-46_import_b2_3files_12percent_30cm_beforecorrection,/user/slops/data/LHC_DATA/OP_DATA/Betabeat/2022-05-02/LHCB2/Results/B2_30cm_after_coupling_correction \
	--folder=/afs/cern.ch/eng/sl/lintrack/LHC_commissioning2022/COM_2022_05_02_squeeze_local_corrections/plots/lhcb2_before_vs_after_localcorr.pdf \
	--plot=Beta_beat \
	--maxx=1.85 \
	--minx=-1.15 \
	--maxy=0.55 \
       	--miny=-0.4 \
	--hmaxx=26614.97265625 \
	--hminx=-0.3448531029978767 \
	--hmaxy=NaN \
       	--hminy=NaN \
       	--mainnode=Beta \
	--legendx=69.0 \
	--legendy=12.0 \
	--legendh=91.0 \
	--labels=B2_Before_LocalCorr,B2_After_LocalCorr
