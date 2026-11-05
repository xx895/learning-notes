# demo.py — 环境验证脚本
# 目的：确认 Python 环境可用，并预览"用代码算统计指标"的感觉。
# 后续学 Pandas 后，这类计算会一行搞定，这里是打基础。

import statistics

# 假设这是某次小测验的成绩
scores = [85, 92, 78, 90, 88, 76, 95, 89, 84, 91]

print("数据:", scores)
print("样本量 :", len(scores))
print("均值   :", round(statistics.mean(scores), 2))
print("中位数 :", statistics.median(scores))
print("标准差 :", round(statistics.pstdev(scores), 2))
print("方差   :", round(statistics.pvariance(scores), 2))
print("\n✅ Python 环境正常，可以开始学习！")
