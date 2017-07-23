import numpy as np
from mne.stats import spatio_temporal_cluster_1samp_test
from mne.stats import permutation_cluster_1samp_test


# Decoding plots parameters
sfreq = 40
tmin = -0.2
tmax = 3.0

sample_times = np.linspace(0, (tmax-tmin)*sfreq, (tmax-tmin)*sfreq + 1)
times = sample_times/sfreq + tmin

def plot(scores, ax, analysis):
    im = ax.matshow(scores, origin='lower', cmap='RdBu_r',
                    extent=[tmin, tmax, tmin, tmax])
    # im = ax.matshow(scores, origin='lower', cmap='RdBu_r',
    #                  extent=[tmin, tmax, tmin, tmax], vmin=-0.15, vmax=0.15)

    ax.set_xticks([0, 0.4, 0.8, 1.2, 1.6, 2, 2.4, 2.8 ])
    ax.set_yticks([0, 0.4, 0.8, 1.2, 1.6, 2, 2.4, 2.8 ])
    ax.set_xlabel('Train Times', fontsize='x-large')
    ax.set_ylabel('Test Times', fontsize='x-large')
    ax.xaxis.set_ticks_position('bottom')
    ax.set_title(analysis)
    return im

def decod_stats(X, chance):
    """Statistical test applied across subjects"""
    # check input
    X = np.array(X)
    # stats function report p_value for each cluster
    null = np.repeat(chance, len(times))
    # Non-corrected t-test...
    # T_obs, p_values_ = ttest_1samp(X, null, axis=0)
    T_obs_, clusters, p_values, _ = permutation_cluster_1samp_test(
        X, out_type='mask', n_permutations=2**12, n_jobs=-1,
        verbose=False)
    # format p_values to get same dimensionality as X
    p_values_ = np.ones_like(X[0]).T
    for cluster, pval in zip(clusters, p_values):
        p_values_[cluster] = pval

    return np.squeeze(p_values_)

def gat_stats(X):
    """Statistical test applied across subjects"""
    # check input
    X = np.array(X)
    X = X[:, :, None] if X.ndim == 2 else X

    # stats function report p_value for each cluster
    T_obs_, clusters, p_values, _ = spatio_temporal_cluster_1samp_test(
        X, out_type='mask',
        n_permutations=2**12, n_jobs=-1, verbose=False)

    # format p_values to get same dimensionality as X
    p_values_ = np.ones_like(X[0]).T
    for cluster, pval in zip(clusters, p_values):
        p_values_[cluster.T] = pval

    return np.squeeze(p_values_).T
