import csv
import matplotlib.pyplot as plt

# 定义道路类型字典
highway_types = {
    1: "Living Street",
    2: "Motorway",
    3: "Motorway Link",
    4: "Primary",
    5: "Primary Link",
    6: "Residential",
    7: "Road",
    8: "Secondary",
    9: "Secondary Link",
    10: "Tertiary",
    11: "Tertiary Link",
    12: "Trunk",
    13: "Trunk Link"
}

# 读取CSV文件
with open('data\\road.csv', 'r') as file:
    reader = csv.DictReader(file)    
    # 初始化道路类型计数器
    highway_counts = {key: 0 for key in highway_types.keys()}
    
    # 统计道路类型数量
    for row in reader:
        highway = int(row['highway'])
        if highway in highway_counts:
            highway_counts[highway] += 1
    
    # 提取道路类型和数量
    labels = [highway_types[key] for key in highway_counts.keys()]
    values = list(highway_counts.values())
    
    # 绘制柱状图
    plt.bar(labels, values)
    plt.xlabel("道路类型")
    plt.ylabel("数量")
    plt.title("道路类型统计")
    plt.xticks(rotation=45)
    plt.show()