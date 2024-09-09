#!/usr/bin/env python
#coding=utf-8

'''
scipy-image-noise-and-filter
================

Image manipulation and processing using Numpy and Scipy

    https://scipy-lectures.org/advanced/image_processing/index.html

Author:
- scipy-lectures.org

Reference:
- https://github.com/scipy-lectures/scipy-lecture-notes
- http://scipy-lectures.org
'''


from os import path
from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import os
import sys

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

def dataframe_parser():
    df = pd.read_csv("ds-radar-patent.csv", encoding="utf-8")
    print(df)

    return df

def dataframe_dump(df):
    print("there are {} rows and {} cols in dataframe".format(df.shape[0], df.shape[1]))
    # print(df.columns.tolist())    # column names
    # print(df.describe())          # statistics by column
    # print(df.info())              # dataframe information
    # print(df.axes)                # row and column index

    angles = np.linspace(0, 2*np.pi, df.shape[0], endpoint=False)
    labels = df.values[:, 0]
    values = df.values[:, 1]
    print("angles:{}".format(angles))
    print("labels:{}".format(labels))
    print("values:{}".format(values))
    return df

def plot_radar_patent(df):
    # support Chinese encoding
    plt.rcParams['font.sans-serif']=['Microsoft YaHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.figure(figsize=(8,6), dpi=80)
    plt.figure(1)

    # divide 360 degrees into N equal parts，N = df.shape[0]
    angles = np.linspace(0, 2*np.pi, df.shape[0], endpoint=False)
    angles = np.concatenate((angles, [angles[0]]))
    labels = df.values[:, 0]
    labels = np.concatenate((labels, [labels[0]]))

    for idx in range(1, df.shape[1]):
        values = df.values[:, idx]
        values = np.concatenate((values, [values[0]]))
        ax = plt.subplot(220 + idx, projection = 'polar')
        ax.plot(angles, values, 'm-', linewidth=2)
        ax.fill(angles, values, 'm', alpha=0.25)
        ax.set_thetagrids(angles*180/np.pi, labels)
        ax.set_ylim(0,20)    # the value range of the factor
        ax.set_title(df.columns.values[idx],fontsize = 20)
        ax.grid(True)

    plt.show()

    return df

if __name__ == '__main__':
    df = dataframe_parser()
    # df = dataframe_dump(df)
    df = plot_radar_patent(df)