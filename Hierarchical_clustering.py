from myradiomics.data_util import NormalizeData, trimm_correlated
import pandas as pd
import numpy as np
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering, KMeans
import seaborn as sns
import matplotlib.pyplot as plt

sequence = ""


path = ""
data = pd.read_csv(".csv")
idx = np.nonzero(np.all(np.asarray(data) == 0, axis=0))[
    0]
data.drop(columns=data.columns[idx], axis=1, inplace=True)
data.drop('pat_id', axis=1, inplace=True)
data.drop('Histopathology_label', axis=1, inplace=True)
data = data.loc[:, (data != data.iloc[0]).any()]
data = data.loc[:, data.apply(pd.Series.nunique) != 1]
corr = data.corr()

x = sns.heatmap(
        corr,
        vmin=-1, vmax=1, center=0,
        cmap=sns.diverging_palette(20, 220, n=200),
        square=True
    )
plt.axis("off")
plt.xlabel("off")
plt.savefig("Results/"+sequence+"/correlogram_all_features.png", dpi=300))
plt.close()

data = trimm_correlated(data, 0.80)
corr = data.corr()
x = sns.heatmap(
        corr,
        vmin=-1, vmax=1, center=0,
        cmap=sns.diverging_palette(20, 220, n=200),
        square=True
    )
plt.axis("off")
plt.savefig("Results/"+sequence+"/correlogram_after_F.png", dpi=300)
plt.close()
print(data.head())


trainX = np.asarray(data.iloc[:, :])
trainX = NormalizeData(trainX, feats_axis=1,
                       norm_type='unit_max')

trainX = trainX.T
print(trainX.shape)
dendrogram = sch.dendrogram(sch.linkage(trainX, method="ward"))
plt.title("Dendrogram")
plt.xlabel("Radiomics features")
plt.ylabel("Euclidian Distance")
plt.savefig("Results/"+sequence+"/Dendrogram_with_normalization_"+sequence+".png", dpi=300)
plt.close()

hc = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')

y_hc = hc.fit_predict(trainX)

print(y_hc)
print(len(y_hc))
f = open("Results/"+sequence+"/clusters_"+sequence+".csv", "w")
for element in y_hc:
    f.write(str(element))
    f.write("\n")

f.close()
data.to_csv("Results/"+sequence+"/Features_selected_"+sequence+".csv")