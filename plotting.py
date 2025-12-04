from matplotlib import pyplot as plt
import scipy.stats as sps
import numpy as np

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
            
