# 因为原数据中data3.xls中 Time of incidence字段中日期数据比较混乱，比如有2009／1／1，也有2009-1-1
# 此程序是为了统一所有字段的格式为 yyyy/mm/dd

import pandas as pd
import numpy as np

def loadData(fileName):     #该函数的作用为 逐行读取数据
    dataMat=[]
    df=open(fileName)
    for line in df.readlines():
        lineArr=line.strip().split(',')[:4]  # strip()为删去每行中开头和结尾的空格，split为以"，"分割数据，分割完之后去前4个字段作为每行的内容
        dataMat.append(lineArr)
        columns=dataMat[0]      # 表中的第一行为字段名称，不做处理，单独抽出
        data=dataMat[1:]        # 抽取第一行之后的数据
    return data,columns

data,columns=loadData('patient_Data/patient_Data_3.csv')      # 读取数据

time=[]

for i in range(len(data)):
    line=data[i][3].split('-')        #每一行中第四列为Time of incidence，以"-" 分割数据
    time.append(line)                  # 分割后的数据 添加到新建的time 空list中

# 上面的循环 把 类似 2007-1-1的数据 分成【2007，1，1】，但 类似 2007／1／1的数据仍然是【2007／1／1】

Time_stamp=[]

for i in range(len(time)):
    if len(time[i])==1:             # 【2007，1，1】长度为3，【2007／1／1】的长度为1
        line=time[i][0].split('/')  #  把类似 2007／1／1 分成【2007，1，1】
    else:
        line=time[i]                 # 其余数据 保持不变
    Time_stamp.append(line)          # 把以上的数据依次添加到 新建的 Time_stamp空列中

Time_of_report=[]
for i in range(len(Time_stamp)):      # 以下的循环主要是 把 分割后的类【2007，1，1】合并成 【2007／1／1】
    year=str(Time_stamp[i][0])         # 再合并之前 需要把数据类型转换 字符串 str
    month=str(Time_stamp[i][1])
    date=str(Time_stamp[i][2])
    stamp=year+'/'+month+'/'+date
    Time_of_report.append(stamp)

df=pd.read_csv('patient_Data/patient_Data_3.csv')       # 用pandas 打开原始数据
df['Time of incidence']=Time_of_report     # 用处理好的数据替换原来的Time of incidence 数据

df.to_csv('patient_Data/after_clean_patient_Data_3.csv')                    #保存文件为 after_clean_patient_Data_3.csv