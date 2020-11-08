# -*- coding: utf-8 -*-
def get_random(low,high):
 return((high-low)*random.random()+low)

from matplotlib import pyplot as plt  # 用来绘制图形
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random

x = [1,1]
y = [1,1]
z = [1,1]


colors1 = '#00CED1' #点的颜色
colors2 = '#DC143C'
plt.ion()# 创建实时动态窗口
for i in range(30000):
    plt.clf()  # 清除之前画的图
    fig = plt.gcf()  # 获取当前图
    ax = fig.gca(projection='3d')
    ax.scatter(x[:-1], y[:-1], z[:-1],c=colors1) #之前点为蓝色
    ax.scatter(x[-1:], y[-1:], z[-1:],c=colors2,label='now:({},{},{}) before:({},{},{})'.format(\
    round(x[-1],2),round(y[-1],2),round(z[-1],2),round(x[-2],2),round(y[-2],2),round(z[-2],2)))   #显示点的值
    ax.legend() #增加图例
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_zlim(0, 10)

    ax.view_init(elev=20, azim=-73) ## Customize the view angle so it's easier to see that the scatter points lie on the plane y=0
    plt.pause(0.5)  # 暂停一段时间
    plt.ioff()  # 关闭画图窗口
    ## 更新数据
    x1 = get_random(0,10)
    y1 = get_random(0,10)
    z1 = get_random(0,10)
    x.append(x1)
    y.append(y1)
    z.append(z1)

plt.show() #绘制完后不让窗口关闭
