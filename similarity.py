import pandas as pd
import numpy as np
from tqdm import tqdm
from sklearn.preprocessing import StandardScaler


def sim_cal(s,t):
    n = len(s)
    m = len(t)
    #print(n)
    #print(m)
    # 定义状态矩阵
    d = np.zeros((n + 1, m + 1))
    #初始化状态矩阵
    i = 0
    for i in range(n+1):
        d[i][0] = i
    j = 0
    for j in range(m+1):
        d[0][j] = j
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            c = 0 if s[i - 1] == t[j - 1] else 1
            # d[i - 1][j - 1] + c是替换当前路段，d[i - 1,j] + 1是删去，d[i, j - 1] + 1是增加
            min_value = min(d[i - 1][j - 1] + c, d[i - 1,j] + 1, d[i, j - 1] + 1)
            d[i][j] = min_value
    return d[n][m]

    
def similarity():
    data = pd.read_csv('data\\bj_test_demo.csv',sep=';')
    roadList = data.iloc[:,1]
    sum = len(roadList)
    sim_matrix = np.zeros((sum, sum))
    sim_array = []
    k = 0
    for i in tqdm(range(sum)):
        for j in range(i + 1, sum):
            sim = sim_cal(roadList.iloc[i], roadList.iloc[j])
            sim_array.append(sim)
    sclar_array = z_score(sim_array)
    k = 0
    for i in range(sum):
        for j in range(i + 1, sum):
            sim_matrix[i][j] = sclar_array[k]
            sim_matrix[j][i] = sclar_array[k]
            k = k + 1
    return sim_matrix


 # 
def z_score(array):
    std = np.std(array)  # 计算数组的标准差
    divided_array = array / std  # 对数组中的每个元素除以标准差
    return divided_array

import time
# test
def runSim():
    # 记录开始时间
    start_time = time.time()
    # 在这里写入您的代码
    matrix = similarity()
    df = pd.DataFrame(matrix)
    df.to_csv('data\\similarity.csv', index = False)
    # 记录结束时间
    end_time = time.time()

    # 计算运行时间
    run_time = end_time - start_time
    print("相似度程序运行时间：", run_time, "秒")
