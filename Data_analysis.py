import pandas as pd
from myradiomics.data_util import NormalizeData, trimm_correlated
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import seed
# from heatmap import heatmap, corrplot
import seaborn as sns
from sklearn.decomposition import PCA
import scipy.cluster.hierarchy as hclust



# parameters initialization
elimn_corr_threshold = 0.80
Visualize_Feature_Matrix = False
TSNE_VISUAL = False

pca_seed = 1964
seed(pca_seed)
sequence = "t1"
type_features = "All_features"
path = "add path to data with radiomic features"

data = pd.read_csv(path+"radiomics_4biopsy_all_features_"+sequence+".csv")
print(data.head())
data.drop('pat_id', axis=1, inplace=True)
idx = np.nonzero(np.all(np.asarray(data) == 0, axis=0))[
    0]
data.drop(columns=data.columns[idx], axis=1, inplace=True)
corr = data.corr()
x = sns.heatmap(
        corr,
        vmin=-1, vmax=1, center=0,
        cmap=sns.diverging_palette(20, 220, n=200),
        square=True
    )

data = (data - data.mean()) / data.std()
data = data.dropna(1)
data = data.drop(columns=data.keys()[data.std() < 0.1])
print(data.head())

plt.savefig("Results/"+sequence+"/correlogram.png", dpi=300)
plt.close()


# # Visualize features
plt.figure(1), plt.imshow(data.values)
plt.axis("off")
plt.savefig("Results/"+sequence+"/All_features.png", dpi=300)
plt.close()


#Check correlation
high_corr_pairs = []
remove_ids = []
remove_features = []
corr = data.corr()
cr = np.triu(corr.abs().values, k=1)
plt.axis("off")
plt.imshow(corr)
plt.savefig("Results/"+sequence+"/correlation.png", dpi=300)
plt.close()

data = trimm_correlated(data, 0.80)
print(data.head())
corr = data.corr()
# # Visualize features
plt.figure(1), plt.imshow(data.values, vmin=-1, vmax=1)
plt.axis("off")
plt.savefig("Results/"+sequence+"/Fselection.png", dpi=300)
plt.close()


pdist = hclust.distance.pdist(corr)
Z = hclust.linkage(pdist, method='complete')
idx = hclust.fcluster(Z, 0.5 * pdist.max(), 'distance')
fig = plt.figure(figsize=(10, 10))
dn = hclust.dendrogram(Z)
plt.savefig("Results/"+sequence+"/Fselection_dendrogram.png", dpi=300)
plt.close()

x = sns.heatmap(
        corr,
        vmin=-1, vmax=1, center=0,
        cmap=sns.diverging_palette(20, 220, n=200),
        square=True
    )
plt.savefig("Results/"+sequence+"/Fselection_correlogram.png", dpi=300)
plt.close()