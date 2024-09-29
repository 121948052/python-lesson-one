'''
Author: Bug Router
Date: 2024-09-29 14:26:03
Description: Default
'''
import matplotlib.pyplot as plt
import numpy as np

# 生成数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 绘制线图
plt.plot(x, y)

# 添加标题和标签
plt.title('Sine Wave')
plt.xlabel('X')
plt.ylabel('Y')

# 显示图形
plt.show()