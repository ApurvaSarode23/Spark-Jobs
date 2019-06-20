import urllib.request

from bs4 import BeautifulSoup
import re
import datetime
from  more_itertools import unique_everseen
import pandas as pd




webpage="http://hn1-devrsi.ksccfrln1ojung4rfd25mexi3b.bx.internal.cloudapp.net:8088/cluster"
page=urllib.request.urlopen(webpage)
soup=BeautifulSoup(page,'html.parser')



pattern=re.compile(r'appli[a-zA-Z]*\_\d+\_\d+')
pattern1=re.compile(r'livy.*[a-zA-Z]*\_\d+')
r1=re.findall(pattern1,soup.text)
res=re.findall(pattern,soup.text)
application_id_list=list(unique_everseen(res))


res1 = re.compile(r'\>appli[a-zA-Z]*\_\d+\_\d+.*livy.*[a-zA-Z]*\_\d+')
result=re.findall(res1,soup.text)

dictLoader={}
dictShaper={}
dictRestate={}
for a in result:
    if(str(a).__contains__('application_' and 'Loader') and not(str(a).__contains__('Test' or 'test'))):
        dictLoader.update({a[1:31]:a[44:65]})
    elif(str(a).__contains__('application_' and 'Shaper') and not(str(a).__contains__('Test' or 'test'))):
        dictShaper.update({a[1:31]:a[44:51]})
    elif(str(a).__contains__('application_' and 'Restatement') and not(str(a).__contains__('Test' or 'test'))):
        dictRestate.update({a[1:31]:a[44:77]})



from pandas import ExcelWriter

outPath='C:\\Users\\apurva.sarode\\Documents\\Apurva\\temp_excel.xlsx'
writer = ExcelWriter(outPath)




loaderApplicationId=[]
shaperApplicationId=[]
restateApplicationId=[]
loaderJob=[]
loaderTime=[]
shaperJob=[]
shaperTime=[]
restateJob=[]
restateTime=[]
tempList=['application_1544591946163_9087','application_1544591946163_9088','application_1544591946163_9087','application_1544591946163_9123']
for app_id in application_id_list:
    if(app_id in dictLoader.keys()):
        web1 = "http://hn0-devrsi.ksccfrln1ojung4rfd25mexi3b.bx.internal.cloudapp.net:18080/history/"+str(app_id)+"/1/jobs/"
        page1=urllib.request.urlopen(web1)
        soup1=BeautifulSoup(page1,'html.parser')
        res1oader = re.sub('<(li)[^>]*>', r'<\1>', soup1.text, flags=re.I)
        resultloader=re.sub('<(td)[^>]*>',r'<\1>',res1oader,flags=re.I)
        if(resultloader.__contains__("2019/02/11")):
            b=res1oader.rfind("Uptime")
            loaderApplicationId.append(app_id)
            loaderJob.append(dictLoader[app_id])
            loaderTime.append(res1oader[b+20:b+30])
            print(app_id,",",dictLoader[app_id],",",res1oader[b+20:b+30])
            df = pd.DataFrame({'Col_appId': loaderApplicationId,'Job_Name':loaderJob,'Time_Taken':loaderTime})
            df.to_excel(writer, 'Sheet1')
            writer.save()
            

    elif((app_id in dictShaper.keys()) and (app_id not in tempList)):
        web2 = "http://hn0-devrsi.ksccfrln1ojung4rfd25mexi3b.bx.internal.cloudapp.net:18080/history/" + str(app_id) + "/1/jobs/"
        print("Shaper+++++++++++",app_id)
        page2 = urllib.request.urlopen(web2)
        soup2 = BeautifulSoup(page2, 'html.parser')
        resshaper = re.sub('<(li)[^>]*>', r'<\1>', soup2.text, flags=re.I)
        resultshaper = re.sub('<(td)[^>]*>', r'<\1>', resshaper, flags=re.I)
        if (resultshaper.__contains__("2019/02/11")):
            b = resshaper.rfind("Uptime")
            shaperApplicationId.append(app_id)
            shaperJob.append(dictShaper[app_id])
            shaperTime.append(resshaper[b + 20:b + 30])
            print(app_id,",",dictShaper[app_id],",",resshaper[b + 20:b + 30])
            df1 = pd.DataFrame({'Col_appId': shaperApplicationId,'Job_Name':shaperJob,'Time_Taken':shaperTime})
            df1.to_excel(writer, 'Sheet2')
            writer.save()
            

    elif(app_id in dictRestate.keys()):
        web3 = "http://hn0-devrsi.ksccfrln1ojung4rfd25mexi3b.bx.internal.cloudapp.net:18080/history/" + str(app_id) + "/1/jobs/"
        
        page3 = urllib.request.urlopen(web3)
        soup3 = BeautifulSoup(page3, 'html.parser')
        resrestate = re.sub('<(li)[^>]*>', r'<\1>', soup3.text, flags=re.I)
        resultrestate = re.sub('<(td)[^>]*>', r'<\1>', resrestate, flags=re.I)
        if (resultrestate.__contains__("2019/02/11")):
            b = resrestate.rfind("Uptime")
            restateApplicationId.append(app_id)
            restateJob.append(dictRestate[app_id])
            restateTime.append(resrestate[b + 20:b + 30])
            print(app_id, ",", dictRestate[app_id], ",", resrestate[b + 20:b + 30])
            df2 = pd.DataFrame({'Col_appId': restateApplicationId,'Job_Name':restateJob,'Time_Taken':restateTime})
            df2.to_excel(writer, 'Sheet3')
            writer.save()
            



