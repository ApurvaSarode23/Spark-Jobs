import urllib.request

from bs4 import BeautifulSoup
import re
import datetime
from  more_itertools import unique_everseen
import pandas as pd




webpage="http://hn1-devrsi.ksccfrln1ojung4rfd25mexi3b.bx.internal.cloudapp.net:8088/cluster"
page=urllib.request.urlopen(webpage)
soup=BeautifulSoup(page,'html.parser')
# print(soup)

# pattern = re.compile(r'.*id=(\d+).*.(\d\d:\d\d:\d\d).*')
pattern=re.compile(r'appli[a-zA-Z]*\_\d+\_\d+')
pattern1=re.compile(r'livy.*[a-zA-Z]*\_\d+')
r1=re.findall(pattern1,soup.text)
res=re.findall(pattern,soup.text)
application_id_list=list(unique_everseen(res))


res1 = re.compile(r'\>appli[a-zA-Z]*\_\d+\_\d+.*livy.*[a-zA-Z]*\_\d+')
result=re.findall(res1,soup.text)
# print(result)
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


print(dictLoader)
print(dictShaper)
print(dictRestate)


# loaderList=[]
# loaderAppIdList=[]
# shaperList=[]
# shaperAppIdList=[]
# restateList=[]
# restateAppIdList=[]


# for w in r1:
#     if(w.__contains__('Loader') and not(w.__contains__('Test' or 'test'))):
#         loaderList.append(w[5:30])
#     elif(w.__contains__('Shaper') and not(w.__contains__('Test' or 'test'))):
#           shaperList.append(w[5:13])
#     elif(w.__contains__('Restatement') and not(w.__contains__('Test' or 'test'))):
#         restateList.append(w[5:37])
#
#
# print(loaderList)
# print(shaperList)
# print(restateList)
#
from pandas import ExcelWriter

outPath='C:\\Users\\apurva.sarode\\Documents\\Apurva\\temp_excel.xlsx'
writer = ExcelWriter(outPath)


# unused=["/application_1544591946163_8597","/application_1544591946163_8588","/application_1544591946163_8587","/application_1544591946163_8546","/application_1544591946163_8541","/application_1544591946163_8540","/application_1544591946163_8351","/application_1544591946163_8350","/application_1544591946163_8340","/application_1544591946163_8338","/application_1544591946163_8337","/application_1544591946163_8336","/application_1544591946163_8332","/application_1544591946163_8306","/application_1544591946163_8305","/application_1544591946163_8133","/application_1544591946163_7619","/application_1544591946163_7618","/application_1544591946163_8653","/application_1544591946163_8777","/application_1544591946163_8821","/application_1544591946163_8777","/application_1544591946163_8081","/application_1544591946163_8080","/application_1544591946163_8079","/application_1544591946163_8078",
#         "/application_1544591946163_8891","/application_1544591946163_8890","/application_1544591946163_8889","/application_1544591946163_8888","/application_1544591946163_8887","/application_1544591946163_8886","/application_1544591946163_8885","/application_1544591946163_8884","/application_1544591946163_8734","/application_1544591946163_8733","/application_1544591946163_8732","/application_1544591946163_8731","/application_1544591946163_8730","/application_1544591946163_8729","/application_1544591946163_8728","/application_1544591946163_8727","/application_1544591946163_8667","/application_1544591946163_8138","/application_1544591946163_8134","/application_1544591946163_7617","/application_1544591946163_7616","/application_1544591946163_7615","/application_1544591946163_7614","/application_1544591946163_7368"]

# temp_web="http://hn0-devrsi.ksccfrln1ojung4rfd25mexi3b.bx.internal.cloudapp.net:18080/history/application_1544591946163_8025/1/jobs/"
# temp_page=urllib.request.urlopen(temp_web)
# temp_soup=BeautifulSoup(temp_page,'html.parser')
# temp_loader=re.sub('<(li)[^>]*>', r'<\1>', temp_soup.text, flags=re.I)
# temp_res=re.sub('<(td)[^>]*>',r'<\1>',temp_loader,flags=re.I)
# print(temp_loader)
# if(temp_res.__contains__("2019/01/19")):
#     b = temp_loader.rfind("Uptime")
#     print(temp_res[b+20:b+30])

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
        # print(app_id in dictLoader.keys())
        web1 = "http://hn0-devrsi.ksccfrln1ojung4rfd25mexi3b.bx.internal.cloudapp.net:18080/history/"+str(app_id)+"/1/jobs/"
        # print("Loader+++++++++++++++++",app_id)
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
            # print("+++++++++++++++++++++++++++++++++++++++++++")
            # print(df)


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
            # print(df1)

    elif(app_id in dictRestate.keys()):
        web3 = "http://hn0-devrsi.ksccfrln1ojung4rfd25mexi3b.bx.internal.cloudapp.net:18080/history/" + str(app_id) + "/1/jobs/"
        # print("Resatement+++++++++++", app_id)
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
            # print(df2)



