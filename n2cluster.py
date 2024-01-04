from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
import hdbscan
from sklearn.metrics import pairwise_distances


def run_cluster():
    # 从CSV文件加载数据
    data = np.loadtxt('data\\similarity.csv', delimiter=',', skiprows=1)

    # 打印加载的数据
    # print("Loaded data:")
    # print(data)

    # 将数据转换为矩阵
    matrix = np.matrix(data)
    matrix = np.asarray(matrix)

    # 使用 HDBSCAN 进行聚类
    clusterer = hdbscan.HDBSCAN(metric='precomputed', min_cluster_size=5, min_samples=2)
    labels = clusterer.fit_predict(matrix)

    from sklearn import metrics


    # 计算评估指标
    silhouette_coefficient = metrics.silhouette_score(matrix, labels)
    calinski_harabasz_index = metrics.calinski_harabasz_score(matrix, labels)
    davies_bouldin_index = metrics.davies_bouldin_score(matrix, labels)

    # 打印评估结果
    print(f"Silhouette Coefficient: {silhouette_coefficient:.3f}")
    print(f"Calinski-Harabasz Index: {calinski_harabasz_index:.3f}")
    print(f"Davies-Bouldin Index: {davies_bouldin_index:.3f}")


