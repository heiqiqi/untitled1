import csv
import  re
import time
from bs4 import BeautifulSoup
import pandas as pd
import requests
from pandas import DataFrame
# url='http://www.tianqihoubao.com/lishi/beijing/month/201901.html'
def gturl(url):
    a=requests.get(url)
    soup = BeautifulSoup(a.text, 'lxml')
    soup=str(soup)
    reg=re.compile('<td.*?a href="(.*?)".*?</td>',re.S)
    reg2=re.compile('<td.*?title="(.*?)".*?</td>',re.S)
    reg3 = re.compile('<tr>.*?<td>.*?a href=.*?<\/td>.*?<td>(.*?)<\/td>.*?<\/tr>', re.S)
    reg4 = re.compile('<tr>.*?<td>.*?a href=.*?<\/td>.*?<td>.*?<\/td>.*?<td>(.*?)<\/td>.*?<\/tr>', re.S)
    reg5=re.compile('<tr>.*?<td>.*?a href=.*?<\/td>.*?<td>.*?<\/td>.*?<td>.*?<\/td>.*?<td>(.*?)<\/td>.*?<\/tr>',re.S)
    html=re.findall(reg,soup)
    html2=re.findall(reg2,soup)
    data=[]
    data1=[]
    data3=[]
    data4=[]
    data5=[]
    data2=[]
    html3=re.findall(reg3,soup)
    html4 = re.findall(reg4, soup)
    html5 = re.findall(reg5, soup)
    for a in html:
        data.append('www.tianqihoubao.com/'+a)
    for b in html2:
        b = b.strip()
        data1.append(b)
    for i in html3:
        a = i.strip().replace('\n', '').split("/")[0].strip()
        b = i.strip().replace('\n', '').split("/")[1].strip()
        s=a+'/'+b
        data3.append(s)
    for c in html4:
        x = c.strip().replace('\n', '').split("/")[0].strip()
        y = c.strip().replace('\n', '').split("/")[1].strip()
        data4.append(x)
        data5.append(y)
    for t in html5:
        k = t.strip().replace('\r', '').split('/')[0]
        data2.append(k)
    #rows=zip(data,data1,data3,data4,data5)
    # with open(r'C:\Users\16006\PycharmProjects\untitled7\pabaobao\tianqi.csv', "a+",newline='') as f:
    #     f_csv = csv.writer(f)
    #     for row in rows:
    #         f_csv.writerows(row)
    # row={'website':data}
    # df1 = pd.DataFrame(row)
    # df1.to_csv('./website.csv',mode='a')
    rows={'date':data1,'weather situation':data3,'mixtem':data5,'maxtem':data4,'wind':data2}
    df=pd.DataFrame(rows)
    df.to_csv('./historytianqi1.csv',mode='a')
cities = ['dongguang','hangzhou']
years = ['2016','2017','2018']
months = ['01','02','03','04','05','06', '07', '08','09','10','11','12']
if __name__ == '__main__':
    for city in cities:
            for year in years:
                for month in months:
                    url = 'http://www.tianqihoubao.com/lishi/' + city + '/month/' + year + month + '.html'
                    html2= gturl(url)
                    print(city + year + month + ' is OK')
                    time.sleep(1)
