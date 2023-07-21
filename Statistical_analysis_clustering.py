from sklearn.metrics import auc, roc_curve
import pandas as pd

data = pd.read_csv("Data_processed/group_1_2_3_4/cine_lge_t1/With_correlation/Without_PCA/features_with_cluster.csv")
outcome = data["Outcome"].values
cluster = data["Cluster"].values
print(cluster)

fpr = dict()
tpr = dict()
roc_auc = dict()
fpr[1], tpr[1], _ = roc_curve(outcome, cluster)
roc_auc[1] = auc(fpr[1], tpr[1])
print('AUC = {AUC}'.format(AUC=roc_auc[1]))