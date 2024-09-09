import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import interpolate     #插值引用

plt.rcParams['font.sans-serif']=['Microsoft YaHei']
plt.rcParams['axes.unicode_minus']=False

#加载数据
data=pd.read_excel('ds-contour-matrix.xlsx',sheet_name='sheet-01',index_col=0)

#自定义插值函数---二维
def extend_data(data):
    data=np.array(data)
    
    def extend_x(X):
        data=X.copy()
        n=data.shape[1]
        mid_extend=np.zeros(shape=(data.shape[0],n-1))
        out=np.zeros(shape=(data.shape[0],2*n-1))

        for i in range(n-1):
            mid_extend[:,i]=(data[:,i]+data[:,i+1])/2.0

        for i in range(2*n-1):
            if i%2==0:
                out[:,i]=data[:,0]
                data=np.delete(data, 0, axis=1)
            else:
                out[:,i]=mid_extend[:,0]
                mid_extend=np.delete(mid_extend, 0, axis=1)

        return out
    
    def extend_y(Y):
        data=Y.T.copy()

        return extend_x(data).T
    
    data=extend_x(data)
    data=extend_y(data)
    
    return data

#自定义插值函数---一维
def extend_x(X):
    data=X.copy()
    n=data.shape[0]
    mid_extend=np.zeros(n-1)
    out=np.zeros(2*n-1)

    for i in range(n-1):
        mid_extend[i]=(data[i]+data[i+1])/2.0

    for i in range(2*n-1):
        if i%2==0:
            out[i]=data[0]
            data=np.delete(data, 0)
        else:
            out[i]=mid_extend[0]
            mid_extend=np.delete(mid_extend, 0)

    return out

#自定义颜色分割界线
def cmap_def(Height,progression='logspace'):
    '''
    white_min  白色下界
    white_max  白色上界，与白色下界对称
    n          在extend_Height最大值与白色上界等分的数量
    progression  'logspace' 等差数列   'logspace'等比数列
    
    返回：levels
    '''
    white_min=-1*np.max(np.abs(Height))/10     #白色下界
    white_max=1*np.max(np.abs(Height))/10      #白色上界，与白色下界对称
    n=6      #在Height最大值与白色上界等分的数量
    
    Height_max=np.max(np.abs(Height))+np.max(np.abs(Height))/10
    
    if progression=='linspace':         #线性等差分割点
        
        levels=list(np.linspace(-1*Height_max,white_min,n))   #小于白色下界值等分n

        levels.extend(list(np.linspace(white_max,Height_max,n)))
    
    else :    #等比分割点
        levels=-1*np.logspace(np.log(white_max),np.log(Height_max),n,base=np.e)
        levels.sort()
        levels=list(levels)
        levels.extend(list(np.logspace(np.log(white_max),np.log(Height_max),n,base=np.e)))
    
    return levels

x=np.array([0,1,2,3,4,5,6])
y=np.array([0,1,2,3,4,5,6])
Height=data.values
#先进行一次线性插值
n=1
x_extend=x.copy()
y_extend=y.copy()
Height_extend=Height.copy()
for i in range(n):
    x_extend=extend_x(x_extend)
    y_extend=extend_x(y_extend)
    Height_extend=extend_data(Height_extend)

#进行矩阵二元样条插值
Height_R= interpolate.RectBivariateSpline(x_extend,y_extend,Height_extend,kx=2, ky=2,s=0.0000001)
x_new=np.linspace(0,6,2000)
y_new=np.linspace(0,6,2000)
X_new,Y_new=np.meshgrid(x_new, y_new)
Height_new=Height_R(x_new,y_new)

#颜色分割界线
levels=cmap_def(Height)

#自定义颜色阶
colors=['#0c7fa4','#3893b4','#6ebcd2','#8ec9d6','#afd5e4','#ffffff','#f4c0bd','#eb827f','#ea5350','#de333a','#d41f26']

#画图
fig=plt.figure(figsize=(12, 6),dpi=255)

# 填充颜色
a=plt.contourf(X_new, Y_new, Height_new, levels=levels, alpha =1,colors=colors)
# 绘制等高线
c= plt.contour(X_new, Y_new, Height_new, levels=levels, colors = 'white', linewidths=0.3,alpha=1,linestyles='solid')

b=plt.colorbar(a,ticks=levels)
b.set_ticklabels(ticklabels=[format(i,'.1%') for i in levels])

plt.xticks([1,2,3,4,5],labels=['性格1','性格2','性格3','性格4','性格5'])
plt.yticks([1,2,3,4,5],labels=['产品人群1','产品人群2','产品人群3','产品人群4','产品人群5'])
plt.tick_params(length=0)  #不显示刻度线

# #去掉顶部、右边 边框
# ax = plt.gca()
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)

plt.xlim(0,6)
plt.ylim(0,6)
# plt.grid()  #网格线

# plt.savefig('a_vs_b红蓝图.png',dpi=255)  #保存图片

plt.show()