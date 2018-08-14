# cerebral_stroke_DA
脑卒中发病环境因素分析
## 背景
  - 脑卒中（俗称脑中风）是目前威胁人类生命的严重疾病之一，它的发生是一个漫长的过程，一旦得病就很难逆转。这种疾病的诱发已经被证实与环境因素，包括气温和湿度之间存在密切的关系。对脑卒中的发病环境因素进行分析，其目的是为了进行疾病的风险评估，对脑卒中高危人群能够及时采取干预措施，也让尚未得病的健康人，或者亚健康人了解自己得脑卒中风险程度，进行自我保护。同时，通过数据模型的建立，掌握疾病发病率的规律，对于卫生行政部门和医疗机构合理调配医务力量、改善就诊治疗环境、配置床位和医疗药物等都具有实际的指导意义。

## 数据说明
- **原数据**
  
  数据（见Appendix-C1）来源于中国某城市各家医院2007年1月至2010年12月的脑卒中发病病例信息以及相应期间当地的逐日气象资料（Appendix-C2）
  - Appendix-C1属性说明
    - Sex(性别)： 1--男，2--女
    - Occupation(职业): 1--- 农民, 2--- 工人, 3--- 退休人员, 4--- 教师, 5--- 渔民, 6--- 医务人员, 7--- 职工, 8--- 离退人员, 空格--- 其他或缺失
    - Note:
      * (a)在“Time of incidence (发病时间) ” 和 “Report time (诊断报告时间)” 中存在不同的时间格式以及错误 (如: #### 或空格)
      * (b)一些数据存在部分缺失 (如: “Age (年龄)”中的 ### 或空格)
      
  - Appendix-C2属性说明
    - Date (日期):  day- 天
    - Aver (High, Low) pres --- 平均(最高，最低)气压 (百帕)
    - Aver (High, Low) temp --- ：平均(最高，最底)温度 (摄氏)
    - Aver (Min) RH --- 平均 (最小)相对湿度 (百分比)
    
- **处理数据**
  - paitent_Data 
    - paitent_Data_1.csv   -- (对应Appendix-C1/data1.xls)
    - paitent_Data_2.csv   -- (对应Appendix-C1/data2.xls)
    - paitent_Data_3.csv   -- (对应Appendix-C1/data3.xls)
    - paitent_Data_4.csv   -- (对应Appendix-C1/data4.xls)
    - after_clean_paitent_Data_3.csv  -- (程序patientData_clean.py针对paitent_Data_3.csv清理结果)
    
  -  weathet_Data
     - weather_07.csv  -- (对应Appendix-C2/data5.xls/sheet07) 
     - weather_08.csv  -- (对应Appendix-C2/data5.xls/sheet08) 
     - weather_09.csv  -- (对应Appendix-C2/data5.xls/sheet09) 
     - weather_10.csv  -- (对应Appendix-C2/data5.xls/sheet10) 

  - 分析数据
  	- patientData.csv  -- （在Excel中把四年病人数据汇总，其中paitent_Data_3.csv的数据替换成after_clean_paitent_Data_3.csv里的数据）
  	- totData_daily.csv    -- （程序weatherData_merge.py处理结果，把weahter_07~10.csv的天气数据合并到一个表，日度数据）
  	- month_patinet_Data.csv    -- (程序stat_month.py针对日度数据totData_daily.csv统计成月度数据)
    
## 问题提出
   - 根据病人基本信息，对发病人群进行统计描述
   - 建立数学模型研究脑卒中发病率与气温、气压、相对湿度间的关系
   - 阅和搜集文献中有关脑卒中高危人群的重要特征和关键指标，结合1、2中所得结论，对高危人群提出预警和干预的建议方案

## 文件说明
  - patientData_clean.py 
      
    
    因为原数据中data3.xls中 Time of incidence字段中日期数据比较混乱，比如有2009／1／1，也有2009-1-1。此程序是为了统一所有字段的格式为 yyyy/mm/dd
    
  - weathrtData_merge.py
  
    将weahter_07~10.csv的天气数据合并到一个表
  
  - stat_month.py
  
    将totData_daily.csv日度数据数据统计为月度数据
    
  - report.docx
    
    分析报告
