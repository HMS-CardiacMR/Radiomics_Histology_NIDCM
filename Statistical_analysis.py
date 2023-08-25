import sys
sys.path.append('')
from data_util import NormalizeData, split_data, trimm_correlated
from sklearn.cluster import KMeans
from sklearn.cluster import SpectralClustering
import pandas as pd
import numpy as np


features_data = pd.read_csv('')
features_data.drop('pat_id', axis=1, inplace=True)
idx = np.nonzero(np.all(np.asarray(features_data) == 0, axis=0))[
    0]  # remove features that are all zeros in all patients
features_data.drop(columns=features_data.columns[idx], axis=1, inplace=True)
features_data.to_csv("", index=False)
features_data = trimm_correlated(features_data, 0.80)
print(features_data.head())


trainX = np.asarray(features_data.iloc[:, :])
trainX = NormalizeData(trainX, feats_axis=1,
                                     norm_type='unit_max')

print(trainX)


kmeans = KMeans(n_clusters=2, init='k-means++').fit_predict(trainX)
spectral = SpectralClustering(n_clusters=2).fit_predict(trainX)

print('K-means:')
print(kmeans)
print('SpectralClustering:')
print(spectral)

from pyckmeans import CKmeans
ckm = CKmeans(k=2, n_rep=100, p_samp=0.8, p_feat=0.5)
ckm.fit(trainX)
ckm_res = ckm.predict(trainX)

# plot consensus matrix and consensus clustering
fig = ckm_res.plot(figsize=(7, 7))
# consensus matrix
ckm_res.cmatrix
fig.savefig("consensus_single_K.png")
# clustering metrics
print('Bayesian Information Criterion:', ckm_res.bic)
print('Davies-Bouldin Index:', ckm_res.db)
print('Silhouette Score:', ckm_res.sil)
print('Calinski-Harabasz Index:', ckm_res.ch)

# consensus clusters
print('Cluster Membership:', ckm_res.cl)

from pyckmeans import MultiCKMeans
mckm = MultiCKMeans(k=[2, 3, 4, 5], n_rep=100, p_samp=0.8, p_feat=0.5)
mckm.fit(trainX)
mckm_res = mckm.predict(trainX)


# clustering metrics
print('Metrics:')
print(mckm_res.metrics)

# plot clustering metrics against k
# BIC, DB: lower is better
# SIL, CH: higher is better
fig = mckm_res.plot_metrics(figsize=(10,5))
fig.savefig("consensus_multiple_K.png")

