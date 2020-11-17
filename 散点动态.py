import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import pandas as pd
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

# create the parametric curve
df1 = pd.read_csv("相关score.csv", engine="python", encoding="utf-8")
df2 = pd.read_csv("涨幅score.csv", engine="python", encoding="utf-8")
df3 = pd.read_csv("配对score.csv", engine="python", encoding="utf-8")
df1.set_index("date", drop=True, inplace=True)
df2.set_index("date", drop=True, inplace=True)
df3.set_index("date", drop=True, inplace=True)
data=[]
for column in df1.columns:
    dt=np.array([df1[column],df2[column],df3[column]])
    data.append(dt)

points=[]
for i in len(df1.columns):
    # create the first plot
    point, = ax.plot([], [], [], 'r')



# point2, =ax.plot([], [], [], '.')
# line, = ax.plot(x, y, z, label='parametric curve')
# ax.legend()
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

# second option - move the point position at every frame
def update_point(n, data, points):
    # point2.set_data([x[0:n], y[0:n]])
    # point2.set_3d_properties(z[0:n], 'z')
    point.set_data([x[n], y[n]])
    point.set_3d_properties(z[n], 'z')
    # point.set_array([255,0,0])
    return point

ani=animation.FuncAnimation(fig, update_point, 99, fargs=(x, y, z, points))
ani.save('test5.gif',writer='pillow')
plt.show()