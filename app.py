import json
import pandas as pd
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import datetime
import matplotlib.animation as animation
import matplotlib.dates as mdates

def main0():
    mpl.rcParams["legend.fontsize"] = 10
    fig = plt.figure()
    # df1 = pd.read_csv("相关score.csv", engine="python", encoding="utf-8")
    # df2 = pd.read_csv("涨幅score.csv", engine="python", encoding="utf-8")
    
    
    df1 = pd.read_csv("20日相关.csv", engine="python", encoding="utf-8")
    df2 = pd.read_csv("20日涨幅.csv", engine="python", encoding="utf-8")

    df1.set_index("date", drop=True, inplace=True)
    df2.set_index("date", drop=True, inplace=True)
    df1=df1['2020':]
    df2=df2['2020':]
    i = 0
    plt.plot()
    plt.subplots_adjust(
        top=1.0, bottom=0.0, left=0.11, right=0.9, hspace=0.2, wspace=0.2
    )
    for column in df1.columns:
        i=i+1

        try:
            ax = fig.gca(projection="3d")
            x = np.arange(0, len(df1.index))
            y = df1[column]-0
            z = df2[column]-0
            ax.plot(x, y, z, label=column)
            ax.set_xlabel("时间(2020.01.01-2020.10.31)")
            ax.set_ylabel("相关")
            ax.set_zlabel("涨跌")
        except :
            continue
    fig.canvas.set_window_title("创业板所有股票时空")
    plt.show()
    return

def main0_1():
    mpl.rcParams["legend.fontsize"] = 10
    fig = plt.figure()
    df1 = pd.read_csv("相关score.csv", engine="python", encoding="utf-8")
    df2 = pd.read_csv("涨幅score.csv", engine="python", encoding="utf-8")
    
    
    # df1 = pd.read_csv("20日相关.csv", engine="python", encoding="utf-8")
    # df2 = pd.read_csv("20日涨幅.csv", engine="python", encoding="utf-8")

    df1.set_index("date", drop=True, inplace=True)
    df2.set_index("date", drop=True, inplace=True)
    df1=df1['2020':]
    df2=df2['2020':]
    i = 0
    plt.plot()
    plt.subplots_adjust(
        top=1.0, bottom=0.0, left=0.11, right=0.9, hspace=0.2, wspace=0.2
    )
    for column in df1.columns:
        i=i+1

        try:
            ax = fig.gca(projection="3d")
            x = np.arange(0, len(df1.index))
            y = df1[column]-0
            z = df2[column]-0
            ax.plot(x, y, z, label=column)
            ax.set_xlabel("时间(2020.01.01-2020.10.31)")
            ax.set_ylabel("相关")
            ax.set_zlabel("涨跌")
        except :
            continue
    fig.canvas.set_window_title("创业板所有股票时空")
    plt.show()
    return
def main1():
    mpl.rcParams["legend.fontsize"] = 10
    fig = plt.figure()
    # df1 = pd.read_csv("相关score.csv", engine="python", encoding="utf-8")
    # df2 = pd.read_csv("涨幅score.csv", engine="python", encoding="utf-8")
    
    
    df1 = pd.read_csv("20日相关.csv", engine="python", encoding="utf-8")
    df2 = pd.read_csv("20日涨幅.csv", engine="python", encoding="utf-8")

    df1.set_index("date", drop=True, inplace=True)
    df2.set_index("date", drop=True, inplace=True)
    df1=df1['2020':]
    df2=df2['2020':]
    i = 0
    plt.plot()
    plt.subplots_adjust(
        top=1.0, bottom=0.0, left=0.11, right=0.9, hspace=0.2, wspace=0.2
    )
    for column in df1.columns:
        i=i+1

        try:
            if(i>20 and i<24):
                ax = fig.gca(projection="3d")
                x = np.arange(0, len(df1.index))
                y = df1[column]-0
                z = df2[column]-0
                ax.plot(x, y, z, label=column)
                ax.set_xlabel("时间(2020.01.01-2020.10.31)")
                ax.set_ylabel("相关")
                ax.set_zlabel("涨跌")
                ax.legend()
        except :
            continue
    fig.canvas.set_window_title("创业板少数股票股票时空")
    plt.show()
    return

def main1_1():
    mpl.rcParams["legend.fontsize"] = 10
    fig = plt.figure()
    df1 = pd.read_csv("相关score.csv", engine="python", encoding="utf-8")
    df2 = pd.read_csv("涨幅score.csv", engine="python", encoding="utf-8")
    
    
    # df1 = pd.read_csv("20日相关.csv", engine="python", encoding="utf-8")
    # df2 = pd.read_csv("20日涨幅.csv", engine="python", encoding="utf-8")

    df1.set_index("date", drop=True, inplace=True)
    df2.set_index("date", drop=True, inplace=True)
    df1=df1['2020':]
    df2=df2['2020':]
    i = 0
    plt.plot()
    plt.subplots_adjust(
        top=1.0, bottom=0.0, left=0.11, right=0.9, hspace=0.2, wspace=0.2
    )
    for column in df1.columns:
        i=i+1

        try:
            if(i>20 and i<24):
                ax = fig.gca(projection="3d")
                x = np.arange(0, len(df1.index))
                y = df1[column]-0
                z = df2[column]-0
                ax.plot(x, y, z, label=column)
                ax.set_xlabel("时间(2020.01.01-2020.10.31)")
                ax.set_ylabel("相关")
                ax.set_zlabel("涨跌")
                ax.legend()
        except :
            continue
    fig.canvas.set_window_title("创业板少数股票股票时空")
    plt.show()
    return
def main2():
    mpl.rcParams["legend.fontsize"] = 10
    fig = plt.figure()
    df1 = pd.read_csv("相关score.csv", engine="python", encoding="utf-8")
    df2 = pd.read_csv("涨幅score.csv", engine="python", encoding="utf-8")

    df1.set_index("date", drop=True, inplace=True)
    df2.set_index("date", drop=True, inplace=True)
    i = 0
    plt.plot()
    plt.subplots_adjust(
        top=1.0, bottom=0.0, left=0.11, right=0.9, hspace=0.2, wspace=0.2
    )

    i=0
    for column in df1.columns:
        i=i+1
        if(i==4):
            break
        ax = fig.gca(projection="3d")
        x = np.arange(0, len(df1.index))
        y = df1[column]
        z = df2[column]
        ax.plot(x, y, z, label=column)
        ax.set_xlabel("时间(2020.01.01-2020.10.31)")
        ax.set_ylabel("相关")
        ax.set_zlabel("涨跌")
    ax.legend()
    fig.canvas.set_window_title("创业板三支股票时空")
    plt.show()
    return

def main3(date):
    mpl.rcParams["legend.fontsize"] = 10
    fig = plt.figure()
    # df1 = pd.read_csv("相关score.csv", engine="python", encoding="utf-8")
    # df2 = pd.read_csv("涨幅score.csv", engine="python", encoding="utf-8")
    # df3 = pd.read_csv("配对score.csv", engine="python", encoding="utf-8")
    df1 = pd.read_csv("20日相关.csv", engine="python", encoding="utf-8")
    df2 = pd.read_csv("20日涨幅.csv", engine="python", encoding="utf-8")
    df3 = pd.read_csv("20日交易.csv", engine="python", encoding="utf-8")
    df1.set_index("date", drop=True, inplace=True)
    df2.set_index("date", drop=True, inplace=True)
    df3.set_index("date", drop=True, inplace=True)
    i = 0
    plt.plot()
    plt.subplots_adjust(
        top=1.0, bottom=0.0, left=0.11, right=0.9, hspace=0.2, wspace=0.2
    )
    i=0
    x=df1.loc[date].values
    y=df2.loc[date].values
    z=df3.loc[date].values
    d=np.arange(0,len(df1.columns))
    ax = fig.gca(projection="3d")
    ax.scatter(x, y, z,c=d,cmap='hsv')
    ax.set_xlabel("相关")
    ax.set_ylabel("涨跌")
    ax.set_zlabel("收益")
    ax.legend()
    fig.canvas.set_window_title(str(date)+"创业板")
    plt.show()
    return

def main4():
    mpl.rcParams["legend.fontsize"] = 10
    fig = plt.figure()

   
    plt.plot()
    plt.subplots_adjust(
        top=1.0, bottom=0.0, left=0.11, right=0.9, hspace=0.2, wspace=0.2
    )
    df1 = pd.read_csv("相关score.csv", engine="python", encoding="utf-8")
    df2 = pd.read_csv("涨幅score.csv", engine="python", encoding="utf-8")
    df3 = pd.read_csv("配对score.csv", engine="python", encoding="utf-8")
    df1.set_index("date", drop=True, inplace=True)
    df2.set_index("date", drop=True, inplace=True)
    df3.set_index("date", drop=True, inplace=True)
    i = 0
    i=0
    x=df1.loc['2020-01-02'].values
    y=df2.loc['2020-01-02'].values
    z=df3.loc['2020-01-02'].values
    # d=np.arange(0,len(df1.columns))
    d=z
    ax = fig.gca(projection="3d")
    ax.scatter(x, y, z,c=d,cmap='hsv')

    ax.set_xlabel("相关")
    ax.set_ylabel("涨跌")
    ax.set_zlabel("收益")
    ax.legend()
    fig.canvas.set_window_title("2020年1月2日创业板")
    def update(number):
        print(number)
    anim = animation.FuncAnimation(plt.gcf(), update, interval=1)
    plt.show()
    return


if __name__ == "__main__":
    plt.rcParams["font.family"] = ["sans-serif"]
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams["axes.unicode_minus"] = False
    # 创业板所有股票 
    main0()
    # 创业板少数股票 
    main1()
    # 创业板所有股票 概率 
    main0_1()
    # 创业板少数股票 概率 
    main1_1()
    
    # main2()
    main3('2020-01-06')
    main3('2020-01-07')
    main3('2020-01-08')

