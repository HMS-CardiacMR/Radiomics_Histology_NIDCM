import numpy as np
import pandas as pd
from sklearn.metrics import pairwise_distances
import warnings
import seaborn as sns
from scipy.stats.stats import pearsonr
import itertools
warnings.filterwarnings("ignore")

data = pd.read_excel("path to data with index for clusters")

cluster1 = data.loc[data["Clusters"] == 0]
features1 = list(cluster1["Features"])
cluster1.drop('Clusters', axis=1, inplace=True)
cluster1.drop('Features', axis=1, inplace=True)

corr = cluster1.corr().values
sns.heatmap(corr)
plt.show()



correlations = {}
columns = cluster1.columns.tolist()

correlation = 0
i = 0
for col_a, col_b in itertools.combinations(columns, 2):
    correlation += np.abs(pearsonr(cluster1.loc[:, col_a], cluster1.loc[:, col_b])[0])
    correlations[str(col_a) + '__' + str(col_b)] = pearsonr(cluster1.loc[:, col_a], cluster1.loc[:, col_b])
    i += 1

print(correlation/i)
result = pd.DataFrame.from_dict(correlations, orient='index')
result.columns = ['PCC', 'p-value']

print(result.sort_index())


cluster1 = np.asarray(cluster1.iloc[:, :])
distance = pairwise_distances(cluster1)
sum_cluster1 = np.sum(distance, axis=0)
index = np.argmin(sum_cluster1)
print("Cluster 1: ", features1[index])

cluster2 = data.loc[data["Clusters"] == 1]
features2 = list(cluster2["Features"])
cluster2.drop('Clusters', axis=1, inplace=True)
cluster2.drop('Features', axis=1, inplace=True)
cluster2 = np.asarray(cluster2.iloc[:, :])
distance = pairwise_distances(cluster2)
sum_cluster2 = np.sum(distance, axis=0)
index = np.argmin(sum_cluster2)
print("Cluster 2: ", features2[index])

cluster3 = data.loc[data["Clusters"] == 2]
features3 = list(cluster3["Features"])
cluster3.drop('Clusters', axis=1, inplace=True)
cluster3.drop('Features', axis=1, inplace=True)
cluster3 = np.asarray(cluster3.iloc[:, :])
distance = pairwise_distances(cluster3)
sum_cluster3 = np.sum(distance, axis=0)
index = np.argmin(sum_cluster3)
print("Cluster 3: ", features3[index])