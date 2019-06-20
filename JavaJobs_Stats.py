import pyodbc
import pandas as pd
from pandas import ExcelWriter

outPath='C:\\Users\\apurva.sarode\\Documents\\Apurva\\BM_Java_Jobs.xlsx'
writer = ExcelWriter(outPath)


server = 'devz1db001'
username = 'devCISDBuser'
password = 'mcVnx3m3M9'
database = 'CIS'
table_name = '[cisaudit].[STATUS_MESSAGE]'

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=devz1db001;DATABASE=CIS;UID=devCISDBuser;PWD=mcVnx3m3M9;Trusted connection=TRUE')
cursor = cnxn.cursor()


processKey=input("Enter a process key")
componentId=input("Enter component id")

cursor.execute("select * from CIS.cisaudit.STATUS_MESSAGE order by CREATE_DATE desc")

time_diff=cursor.execute('declare @start_time datetime2, @end_time datetime2;'
"select @start_time = TIMESTAMP  from CIS.cisaudit.STATUS_MESSAGE where MAIN_PROCESS_KEY=(?) and COMPONENT_ID=(?) and COMPONENT_STATUS='started';"
"select @end_time = TIMESTAMP  from CIS.cisaudit.STATUS_MESSAGE where MAIN_PROCESS_KEY=(?) and COMPONENT_ID=(?) and COMPONENT_STATUS='complete';"
'Select  DATEDIFF(SECOND, @start_time, @end_time);',(processKey),(componentId),(processKey),(componentId))


processKeyList=[]
time_taken=[]
componentIdList=[]
for row in cursor.fetchall():
    processKeyList.append(processKey)
    componentIdList.append(componentId)
    t1=row[0]
    # print(t1)
    time_taken.append(t1)
    df=pd.DataFrame({"ProcessKey":processKeyList,"Component_ID":componentIdList,"Time_taken":time_taken})
    df.to_excel(writer, 'Sheet1')
    writer.save()




