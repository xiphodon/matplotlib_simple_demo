#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/7 18:58
# @Author  : GuoChang
# @Site    : https://github.com/xiphodon
# @File    : matplotlib_simple_demo.py
# @Software: PyCharm

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def show_plot():
    '''
    画一条蓝色正弦虚线
    :return:
    '''
    x = np.linspace(0,2*np.pi,50) # x坐标输入，范围为0~2π，选取50个点
    y = np.sin(x)  # 对应的正弦值
    plt.plot(x,y,'bp--') # 画线，蓝色(b)五角星(p)虚线(--)
    plt.show()


def show_pie():
    '''
    画饼图
    :return:
    '''
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs' # 定义标签
    sizes = [15,30,45,10] # 每一块的量（会自动换算比例）
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral'] # 定义每一块颜色
    explode = (0, 0.1, 0, 0) # 突出显示第二块

    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal') # 显示为圆，避免比例压缩为椭圆
    plt.show()


def show_hist():
    '''
    绘制二位条形直方图
    :return:
    '''
    x = np.random.randn(1000) # 1000个服从正态分布的随机数
    plt.hist(x, 100) # 分为100个组
    plt.show()


def show_boxplot():
    '''
    绘制样本数据的箱线图
    :return:
    '''
    x = np.random.randn(1000) # 1000个服从正态分布的随机数
    data = pd.DataFrame([x,x+1]).T # 构造两列的DataFrame
    # data.plot(kind='box')
    data.boxplot()
    plt.show()


def show_log_plot():
    '''
    绘制x或y轴的对数图形
    :return:
    '''
    x = pd.Series(np.exp(np.arange(20))) #原始数据
    x.plot(label=u'原始数据图',legend=True) # legend 图注
    plt.show()
    x.plot(logy=True,label=u'对数数据表',legend=True)
    plt.show()


def show_error_plot():
    '''
    绘制误差图
    :return:
    '''
    error = np.random.randn(10) #定义误差列
    y = pd.Series(np.sin(np.arange(10))) #均值数据列
    y.plot(yerr=error) #绘制误差图
    plt.show()


if __name__ == '__main__':
    # show_plot()
    # show_pie()
    # show_hist()
    # show_boxplot()
    # show_log_plot()
    show_error_plot()