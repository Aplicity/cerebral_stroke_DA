# 此程序是主要将data_07~10.csv的天气数据合并到一个表
import pandas as pd
import numpy as np
import time

start=time.clock()

def my_mergedata(fileName,year):
    # 参数fileName为文件名，year为年费

    df=pd.read_csv(fileName)    # 打开数据文件
    data=[]
    for i in range(12):  # 一共有12个月份，把每个月份的数据放到data中，data[0]代表第一个月份的数据
        data.append(df.iloc[:,range(8*i+1,8*(i+1)+1)])  # 表中第一列为日期，第二列开始到第9列为一个月数据中所含的字段，后面的字段重复
        data[i]['year']=year        # 在每个表中添加一个字段'year'，其值为函数的参数year
        data[i]['month']=i+1        # 添加字段month，data[0]即第一个月的数据表在表后面添加一列月份标签
        data[i]['date']=df['Date']  # 同上，添加日期
        if i>0:             # 第二个月份表格开始，各个表的字段名与第一个月份的一致，这是为了方便合并
            data[i].columns=data[0].columns

    newdata=pd.DataFrame(columns=data[0].columns)    # 新建一个空DataFrame，其字段名与第一个月份的一致，也是为了方便合并
    for i in range(12):
        newdata=pd.merge(newdata,data[i],how='outer')   # 在刚刚新建的空表里面合并每个月份的数据表
    return newdata

weather_07=my_mergedata('weather_Data/weather_07.csv',2007)
weather_08=my_mergedata('weather_Data/weather_08.csv',2008)
weather_09=my_mergedata('weather_Data/weather_09.csv',2009)
weather_10=my_mergedata('weather_Data/weather_10.csv',2010)

weatherData=pd.merge(weather_07,weather_08,how='outer')       #合并07年和08年的数据表
weatherData=pd.merge(weatherData,weather_09,how='outer')   #同上
weatherData=pd.merge(weatherData,weather_10,how='outer')   #合并

weatherData['time_stamp']=weatherData['year'].map(str)+'/'+weatherData['month'].map(str)+'/'+weatherData['date'].map(str)
# 在合并表后添加一个日期字段，规则为year／month／date，字段是数值形式，直接相加会变成一个总和数值，因此利用map函数将数值映射成字符串

patientData=pd.read_csv('patientData.csv') # 读取患者数据，在这之前已经在excel中把四年患者数据都整合到一个表中，并删除了报告日期
patientData['number']=1     # 为了方便等下分组统计每天的患病人数，先对患者数据表后面添加一个字段numbel，方便等下计数使用

patient_stat_Data=patientData.groupby('Time of incidence').count() # 以Time of incidence 为分组指标分组，统计其余字段的累计值

totData_daily = pd.merge(weatherData,patientData,left_on='time_stamp',right_on='Time of incidence')
# 以天气数据表的time_stamp 和 患者统计数据为的 Time of incidence 的交集为合并索引，合并天气数据和患者数据

totData_daily.to_csv('totData_daily.csv')       # 保存合并之后的数据到文件totData_daily.csv
end=time.clock()
print("计算耗时：%f" %(end-start))
