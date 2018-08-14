# 以下程序主要是将totData_daily.csv日度数据数据统计为月度数据

import pandas as pd
import numpy as np

totData_daily=pd.read_csv('totData_daily.csv')  #用pandas打开汇总后的病人数据

df_2007=totData_daily.loc[(totData_daily['year']==2007)]    #以下是处理2007年的病人数据
df_2007_stat=pd.DataFrame()                      #先建立一个空表

df_2007_stat['count']=df_2007.groupby('month')['number'].sum()          #在新建的空表中添加一列，列名为count，放的是07年每个月患病人数
df_2007_stat['Aver pres']=df_2007.groupby('month')['Aver pres'].mean()  #在新建的空表中添加一列，列名为count，放的是07年每个月的平均气压
df_2007_stat['Low pres']=df_2007.groupby('month')['Low pres'].min()      #每个月的最小气压
df_2007_stat['High pres']=df_2007.groupby('month')['High pres'].max()     #最大气压
df_2007_stat['Aver temp']=df_2007.groupby('month')['Aver temp'].mean()      #平均气温
df_2007_stat['Low temp']=df_2007.groupby('month')['Low temp'].min()         #最低气温
df_2007_stat['High temp']=df_2007.groupby('month')['High temp'].max()       #最高气温
df_2007_stat['Aver RH']=df_2007.groupby('month')['Aver RH'].mean()          #平均湿度
df_2007_stat['Min RH']=df_2007.groupby('month')['Min RH'].min()              #最低湿度

df_2007_stat['Aver pres std']=df_2007.groupby('month')['Aver pres'].std()        #平均气压的标准差
df_2007_stat['Low pres std']=df_2007.groupby('month')['Low pres'].std()         #最低气压的标准差
df_2007_stat['High pres std']=df_2007.groupby('month')['High pres'].std()       #最高气压的标准差
df_2007_stat['Aver temp std']=df_2007.groupby('month')['Aver temp'].std()        #平均气温的标准差
df_2007_stat['Low temp std']=df_2007.groupby('month')['Low temp'].std()          #最低气温的标准差
df_2007_stat['High temp std']=df_2007.groupby('month')['High temp'].std()        #最高气温的标准差
df_2007_stat['Aver RH std']=df_2007.groupby('month')['Aver RH'].std()            #平均湿度的标准差
df_2007_stat['Min RH std']=df_2007.groupby('month')['Min RH'].std()         #最低湿度的标准差

######################下面只是统计08年的同样指标

df_2008=totData_daily.loc[(totData_daily['year']==2008)]
df_2008_stat=pd.DataFrame()

df_2008_stat['count']=df_2008.groupby('month')['number'].sum()
df_2008_stat['Aver pres']=df_2008.groupby('month')['Aver pres'].mean()
df_2008_stat['Low pres']=df_2008.groupby('month')['Low pres'].min()
df_2008_stat['High pres']=df_2008.groupby('month')['High pres'].max()
df_2008_stat['Aver temp']=df_2008.groupby('month')['Aver temp'].mean()
df_2008_stat['Low temp']=df_2008.groupby('month')['Low temp'].min()
df_2008_stat['High temp']=df_2008.groupby('month')['High temp'].max()
df_2008_stat['Aver RH']=df_2008.groupby('month')['Aver RH'].mean()
df_2008_stat['Min RH']=df_2008.groupby('month')['Min RH'].min()

df_2008_stat['Aver pres std']=df_2008.groupby('month')['Aver pres'].std()
df_2008_stat['Low pres std']=df_2008.groupby('month')['Low pres'].std()
df_2008_stat['High pres std']=df_2008.groupby('month')['High pres'].std()
df_2008_stat['Aver temp std']=df_2008.groupby('month')['Aver temp'].std()
df_2008_stat['Low temp std']=df_2008.groupby('month')['Low temp'].std()
df_2008_stat['High temp std']=df_2008.groupby('month')['High temp'].std()
df_2008_stat['Aver RH std']=df_2008.groupby('month')['Aver RH'].std()
df_2008_stat['Min RH std']=df_2008.groupby('month')['Min RH'].std()

######################
df_2009=totData_daily.loc[(totData_daily['year']==2009)]
df_2009_stat=pd.DataFrame()

df_2009_stat['count']=df_2009.groupby('month')['number'].sum()
df_2009_stat['Aver pres']=df_2009.groupby('month')['Aver pres'].mean()
df_2009_stat['Low pres']=df_2009.groupby('month')['Low pres'].min()
df_2009_stat['High pres']=df_2009.groupby('month')['High pres'].max()
df_2009_stat['Aver temp']=df_2009.groupby('month')['Aver temp'].mean()
df_2009_stat['Low temp']=df_2009.groupby('month')['Low temp'].min()
df_2009_stat['High temp']=df_2009.groupby('month')['High temp'].max()
df_2009_stat['Aver RH']=df_2009.groupby('month')['Aver RH'].mean()
df_2009_stat['Min RH']=df_2009.groupby('month')['Min RH'].min()

df_2009_stat['Aver pres std']=df_2009.groupby('month')['Aver pres'].std()
df_2009_stat['Low pres std']=df_2009.groupby('month')['Low pres'].std()
df_2009_stat['High pres std']=df_2009.groupby('month')['High pres'].std()
df_2009_stat['Aver temp std']=df_2009.groupby('month')['Aver temp'].std()
df_2009_stat['Low temp std']=df_2009.groupby('month')['Low temp'].std()
df_2009_stat['High temp std']=df_2009.groupby('month')['High temp'].std()
df_2009_stat['Aver RH std']=df_2009.groupby('month')['Aver RH'].std()
df_2009_stat['Min RH std']=df_2009.groupby('month')['Min RH'].std()

######################
df_2010=totData_daily.loc[(totData_daily['year']==2010)]
df_2010_stat=pd.DataFrame()

df_2010_stat['count']=df_2010.groupby('month')['number'].sum()
df_2010_stat['Aver pres']=df_2010.groupby('month')['Aver pres'].mean()
df_2010_stat['Low pres']=df_2010.groupby('month')['Low pres'].min()
df_2010_stat['High pres']=df_2010.groupby('month')['High pres'].max()
df_2010_stat['Aver temp']=df_2010.groupby('month')['Aver temp'].mean()
df_2010_stat['Low temp']=df_2010.groupby('month')['Low temp'].min()
df_2010_stat['High temp']=df_2010.groupby('month')['High temp'].max()
df_2010_stat['Aver RH']=df_2010.groupby('month')['Aver RH'].mean()
df_2010_stat['Min RH']=df_2010.groupby('month')['Min RH'].min()

df_2010_stat['Aver pres std']=df_2010.groupby('month')['Aver pres'].std()
df_2010_stat['Low pres std']=df_2010.groupby('month')['Low pres'].std()
df_2010_stat['High pres std']=df_2010.groupby('month')['High pres'].std()
df_2010_stat['Aver temp std']=df_2010.groupby('month')['Aver temp'].std()
df_2010_stat['Low temp std']=df_2010.groupby('month')['Low temp'].std()
df_2010_stat['High temp std']=df_2010.groupby('month')['High temp'].std()
df_2010_stat['Aver RH std']=df_2010.groupby('month')['Aver RH'].std()
df_2010_stat['Min RH std']=df_2010.groupby('month')['Min RH'].std()

######################
data=df_2007_stat.merge(df_2008_stat,how='outer')
data=data.merge(df_2009_stat,how='outer')
data=data.merge(df_2010_stat,how='outer')

data.to_csv('month_patient_Data.csv')


# 以上用循环会简洁很多，然而我在notebook 上是逐个表处理的，不想写了，直接复制过来