import os
import sys
sys.path.append('')
from data_util import NormalizeData
import pandas as pd
from consensusClustering import ConsensusCluster
import numpy as np
from sklearn.cluster import KMeans, AgglomerativeClustering
import matplotlib.pyplot as plt
from tqdm import tqdm


def perform_clustering(path):
    data = pd.read_csv(path+"features.csv")
    # cls = ConsensusCluster(KMeans, L=2, K=7, H=5, resample_proportion=0.7)
    print(data.head())
    cls = ConsensusCluster(AgglomerativeClustering, L=2, K=7, H=5, resample_proportion=0.7)
    trainX = np.asarray(data.iloc[:, 3:])
    print(trainX.shape)
    trainX = NormalizeData(trainX, feats_axis=1,
                           norm_type='unit_max')
    trainX = trainX.T
    print(trainX.shape)

    # data.iloc[:, 3:] = trainX
    cls.fit(trainX)
    print(cls.predict())
    print("Area under the conditional density function curve: ", cls.Ak)
    print("changes in areas under conditional density function: ", cls.deltaK)
    print("Number of clusters that was found to be best: ", cls.bestK)
    print("\n")
    cluster_indexes = cls.predict()
    data_to_save = pd.DataFrame(columns=["pat_id", "Outcome", "Histopathology_label", "Cluster"])
    data_to_save["pat_id"] = data["pat_id"]
    data_to_save["Outcome"] = data["Outcome"]
    data_to_save["Histopathology_label"] = data["Histopathology_label"]
    data_to_save["Cluster"] = cluster_indexes
    data.drop('pat_id', axis=1, inplace=True)
    data.drop('Outcome', axis=1, inplace=True)
    data.drop('Histopathology_label', axis=1, inplace=True)
    data_to_save = pd.DataFrame(columns=["Cluster"])
    data_to_save["Cluster"] = cluster_indexes
    dtable = pd.concat([data_to_save, data], axis=1)
    dtable.to_csv(path + "features_with_cluster.csv", index=False)
    plt.imshow(cls.Mk[0])
    plt.savefig(path+"consensus_matrix.png")

list_of_groups = os.listdir("Data_processed/")

for group in tqdm(list_of_groups):
    list_of_sequences = os.listdir("Data_processed/"+group)
    for sequence in list_of_sequences:
        perform_clustering("Data_path")
