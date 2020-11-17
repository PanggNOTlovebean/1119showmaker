"""
============
3D animation
============

A simple example of an animated plot... In 3D!
"""
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
import pandas as pd

def Gen_RandLine(length, dims=2):
    """
    Create a line using a random walk algorithm

    length is the number of points for the line.
    dims is the number of dimensions the line has.
    """
    lineData = np.empty((dims, length))
    lineData[:, 0] = np.random.rand(dims)   # 初始化起点
    for index in range(1, length):
        # scaling the random numbers by 0.1 so
        # movement is small compared to position.
        # subtraction by 0.5 is to change the range to [-0.5, 0.5]
        # to allow a line to move backwards.
        step = ((np.random.rand(dims) - 0.5) * 0.1)  # 步长
        # 下一步的位置
        lineData[:, index] = lineData[:, index - 1] + step

    return lineData   # 返回一个shape为（3,25）的数组,3维坐标25帧


def update_lines(num, dataLines, lines):
    for line, data in zip(lines, dataLines):
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data(data[0:2, :num])
        line.set_3d_properties(data[2, :num])
    return lines

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)

# Fifty lines of random 3-D lines  (长为50的数组，每个元素为shape为3,25的ndarray，最后实际效果就是50条路径)
# data = [Gen_RandLine(25, 3) for index in range(50)]
# print(np.array(data).shape)
df1 = pd.read_csv("20日相关.csv", engine="python", encoding="utf-8").dropna()
df2 = pd.read_csv("20日涨幅.csv", engine="python", encoding="utf-8").dropna()
df3 = pd.read_csv("20日交易.csv", engine="python", encoding="utf-8").dropna()
df1.set_index("date", drop=True, inplace=True)
df2.set_index("date", drop=True, inplace=True)
df3.set_index("date", drop=True, inplace=True)
df1=df1['2020':]
df2=df2['2020':]
df3=df3['2020':]

data=[]
for column in df1.columns:
    try:
        # d1=(df1[column].values-np.min(df1[column].values))/(np.max(df1[column].values)-np.min(df1[column].values))
        # d2=(df2[column].values-np.min(df2[column].values))/(np.max(df2[column].values)-np.min(df2[column].values))
        # d3=(df3[column].values-np.min(df3[column].values))/(np.max(df3[column].values)-np.min(df3[column].values))
        d1=df1[column].values-0
        d2=df2[column].values-0
        d3=df3[column].values-0
        dt=np.array([d1,d2,d3])
        print(d3)
        data.append(dt)
    except :
        continue
# Creating fifty line objects.
# NOTE: Can't pass empty arrays into 3d version of plot()
lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data[:20]] # 每条路径的起始点

# Setting the axes properties
ax.set_xlabel('相关')
ax.set_xlim(-0.5,1)
ax.set_ylabel('涨跌')
ax.set_ylim(-0.75,1)
ax.set_zlabel('收益')
ax.set_zlim(-0.75,0.75)



ax.set_title('3D Test')

# Creating the Animation object
line_ani = animation.FuncAnimation(fig, update_lines, 199, fargs=(data, lines),
                                   interval=200, blit=False,repeat=False)

plt.show()