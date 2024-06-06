import pandas as pd
from sklearn.model_selection import train_test_split
import  similarity
import n2cluster
import test


# 加载原始数据 test
data = pd.read_csv('data\\bj_test.csv', sep=';')

# 划分数据集
# 现在我们一共选择了400个点，其中所需时间最长的就是计算任意轨迹之间的相似度
data, test_data = train_test_split(data, test_size=0.03, random_state=42)

# 转换data列的格式
# train_data['data'] = train_data['data'].apply(lambda x: process_list(eval(x)))
# test_data['data'] = test_data['data'].apply(lambda x: process_list(eval(x)))
# eval_data['data'] = eval_data['data'].apply(lambda x: process_list(eval(x)))

# 保存划分后的数据集为 CSV 文件
test_data.to_csv('data\\bj_test_demo.csv', index=False, sep=';')

# run cluster
similarity.runSim()
# n2cluster.run_cluster()
test.run_cluster()
# test commit
# test
# test commit
