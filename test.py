from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
import hdbscan
from sklearn.metrics import pairwise_distances
from sklearn.cluster import AgglomerativeClustering, KMeans, SpectralClustering

def run_cluster():
    # 从CSV文件加载数据
    data = np.loadtxt('data\\similarity.csv', delimiter=',', skiprows=1)

    # 打印加载的数据
    # print("Loaded data:")
    # print(data)

    # 将数据转换为矩阵
    matrix = np.matrix(data)
    matrix = np.asarray(matrix)
    # 使用 层次进行聚类
    agg_clustering = AgglomerativeClustering(n_clusters=8, metric='precomputed', linkage='average')
    agg_labels = agg_clustering.fit_predict(matrix)

    print("层次聚类结果：")
    print(agg_labels)
    from sklearn import metrics


    # 计算评估指标
    silhouette_coefficient = metrics.silhouette_score(matrix, agg_labels)
    calinski_harabasz_index = metrics.calinski_harabasz_score(matrix, agg_labels)
    davies_bouldin_index = metrics.davies_bouldin_score(matrix, agg_labels)

    # 打印评估结果
    print(f"Silhouette Coefficient: {silhouette_coefficient:.3f}")
    print(f"Calinski-Harabasz Index: {calinski_harabasz_index:.3f}")
    print(f"Davies-Bouldin Index: {davies_bouldin_index:.3f}")


