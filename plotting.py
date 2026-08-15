from matplotlib import pyplot as plt
import scipy.stats as sps
import numpy as np
import sys,os

def groupplot(means,stds,names,colors):
    ngroups = len(means)
    assert len(stds)==len(means)==len(names)
    
    group_sizes = []
    for m in means:
        group_sizes.append(len(m))

    jitter = {}
    for group_names in names:
        for gn in group_names:
            jitter[gn] = np.random.randn()*0.1
            
    for group_idx,(group_means,group_stds,group_names,group_colors) in enumerate(zip(means,stds,names,colors)):
        for gm,gs,gn,gc in zip(group_means,group_stds,group_names,group_colors):
            plt.errorbar(group_idx+jitter[gn],gm,gs,color=gc,capsize=6,linestyle='none')
            plt.plot(group_idx+jitter[gn],gm,marker='s',color=gc,linestyle='none')

    

def sigboxplot(data,sig_capfrac=0.05):
    # first determine pairwise significance of comparisons
    ndata = len(data)
    pvals = np.ones((ndata,ndata))*np.nan
    for n in range(ndata):
        for m in range(n+1,ndata):
            res = sps.ttest_ind(data[n],data[m])
            pvals[n,m] = sps.ttest_ind(data[n],data[m]).pvalue
            # reflect the pvals to make lookup easier:
            pvals[m,n] = sps.ttest_ind(data[n],data[m]).pvalue
            

    medianprops = dict(linestyle='-', linewidth=2, color='black')
    plt.boxplot(data,medianprops=medianprops)
    ylim = plt.gca().get_ylim()
    yrange = np.diff(ylim)
    caplen = yrange*sig_capfrac
    sigheight = ylim[1]+caplen

    for n in range(ndata):
        for m in range(n+1,ndata):
            pval = pvals[n,m]
            if pval>0.05:
                continue
            annotations = ''
            if pval<=0.05:
                annotations += '*'
            if pval<=0.01:
                annotations += '*'
            if pval<=0.001:
                annotations += '*'

            
            x1 = n+1
            x2 = m+1
            y1 = sigheight
            y2 = sigheight+caplen
            plt.plot([x1,x1,x2,x2],[y1,y2,y2,y1],marker='none',color='k')
            plt.text((x1+x2)/2.0,y2,annotations,ha='center',va='bottom')
            sigheight+=caplen*2
    plt.ylim((ylim[0],sigheight))
            
