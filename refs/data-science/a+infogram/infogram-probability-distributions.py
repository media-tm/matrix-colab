#!/usr/bin/python
# -*- coding: UTF-8 -*-
# https://blog.csdn.net/weixin_39882589/article/details/111611065

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei', 'FangSong']
mpl.rcParams['font.size'] = 10
mpl.rcParams['axes.unicode_minus'] = False

def unit_plot_binom():
    num = 10 #构建事件次数
    probability = 0.6 #事件成功的概率
    binom_x = np.arange(0, num + 1) 
    binom_y = stats.binom.pmf(binom_x, num, probability)
    plt.plot(binom_x, binom_y, marker='o', linestyle='')
    plt.vlines(binom_x, 0, binom_y)
    plt.title('二项式分布(硬币朝上:num=10,p=0.60)')

def unit_plot_bernoulli():
    probability = 0.6 #事件成功的概率
    bernoulli_x =  np.arange(0,2)
    bernoulli_y = stats.bernoulli.pmf(bernoulli_x, probability)
    plt.plot(bernoulli_x, bernoulli_y, marker='o', linestyle='')
    plt.vlines(bernoulli_x, [0, 0], bernoulli_y)
    plt.title('伯努利分布(抛硬币),p=0.60')

def unit_plot_geom():
    num = 10 # 构建事件次数
    probability = 0.6 # 事件成功的概率
    geom_x = np.arange(1, num + 1)
    geom_y = stats.geom.pmf(geom_x, probability)
    plt.plot(geom_x, geom_y, marker='o', linestyle='')
    plt.vlines(geom_x, 0, geom_y)
    plt.title('几何分布(表白k次首次成功:num=10,p=0.60)')

def unit_plot_poisson():
    num =2 # 定义给定时间内发生事件的次数
    k =4 # 求给定时间内事件发生4次的概率
    # 包含了发生0次，1次，2次，3次，4次
    poisson_x = np.arange(0,5)
    poisson_y = stats.poisson.pmf(poisson_x, num)
    plt.plot(poisson_x, poisson_y, marker='o', linestyle='')
    plt.vlines(poisson_x,0,poisson_y)
    plt.title('泊松分布(给定时间内发生k次事)')

def unit_plot_norm():
    norm_x = np.arange(-5, 5, 1)
    norm_y = stats.norm.pdf(norm_x)
    plt.plot(norm_x, norm_y, marker='o', linestyle='')
    plt.vlines(norm_x,0,norm_y)
    plt.title("正态分布概率密度")

# 为什么有了正态分布，还有出现幂律分布呢？是因为有些事件理论上是正态分布，真实却都遵循着幂律分布。
# 例如财富分布，极少部分人占据了绝大部分的社会财富，幂律分布其实更加贴近现实。
# 在我们日常生活中，Power-law Distributions(幂律分布)是一种常见的数学模型，
# 如二八原则：20%的人口拥有80%的财富，20%的上市公司创造80%的价值，80%的收入来自20%的商品等等。
def unit_plot_powerlaw():
    powerlaw_x = np.linspace(0,1,100)
    powerlaw_y = stats.powerlaw.pdf(powerlaw_x, 5)
    # powerlaw_y = stats.powerlaw.rvs(1.66, size=500)
    plt.plot(powerlaw_x, powerlaw_y, marker='o', linestyle='')
    plt.vlines(powerlaw_x, 0, powerlaw_y)
    plt.title("幂律分布概率密度")

if __name__ == '__main__':
    plt.subplot(231)
    unit_plot_binom()
    plt.subplot(232)
    unit_plot_bernoulli()
    plt.subplot(233)
    unit_plot_geom()
    plt.subplot(234)
    unit_plot_poisson()
    plt.subplot(235)
    unit_plot_norm()
    plt.subplot(236)
    unit_plot_powerlaw()
    plt.show()
