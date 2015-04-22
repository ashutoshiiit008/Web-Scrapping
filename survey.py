import requests
from BeautifulSoup import BeautifulSoup
import json
import traceback
import csv

#Change "Referer" and "curr_id" in headers and data to crawl for every country.

# output1 = open('D:\\Innovaccer\\Tim Reisen\\Output\\Stock\\Step_2_Out.txt', 'w')




output1 = open('output.txt', 'w')

headers = { 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'en-GB,en-US;q=0.8,en;q=0.6',
'Connection':'keep-alive',
'Host':'trai.gov.in',
'Referer':'http://trai.gov.in/Content/QosUser/1_QosUser.aspx/ctl00$ContentPlaceHolder1$gv_Qos',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
'X-Requested-With':'XMLHttpRequest'}

# headers = { 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
# 'Accept-Encoding':'gzip, deflate, sdch' , 
# 'Accept-Language':'en-GB,en-US;q=0.8,en;q=0.6' ,
# 'Connection': 'keep-alive' ,
# 'Cookie':'JSESSIONID=51E45C11ACC568777C6154F9FDD7C852; __utmt=1; __utma=151860267.388916865.1428904697.1428904697.1428909451.2; __utmb=151860267.4.10.1428909451; __utmc=151860267; __utmz=151860267.1428904697.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
# 'Host':'www.csx.com.kh' ,
# 'Referer':'http://www.csx.com.kh/data/index/daily.do?lang=en&MNCD=60101&indexGroupCode=001&fromDate=20100101&toDate=20150408',
# 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'}

# headers = { 'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' , 
# 'Accept-Encoding':'gzip, deflate, sdch',
# 'Accept-Language':'en-GB,en-US;q=0.8,en;q=0.6',
# 'Connection':'keep-alive',
# 'Cookie':'JSESSIONID=074E64DC93C7AD8D4FD708554A8AA0A3; __utmt=1; __utma=86659333.446052782.1428905413.1428905413.1428907918.2; __utmb=86659333.2.10.1428907918; __utmc=86659333; __utmz=86659333.1428905413.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
# 'Host':'www.lsx.com.la',
# 'Referer':'http://www.lsx.com.la/market/index/daily.do?lang=en&indexGroupCode=001&fromDate=20100101&toDate=20150408',
# 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'}

# headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
# 'Accept-Encoding':'gzip, deflate',
# 'Accept-Language':'en-GB,en-US;q=0.8,en;q=0.6' ,
# 'Cache-Control': 'max-age=0',
# 'Connection':'keep-alive',
# 'Content-Length':'35',
# 'Content-Type': 'application/x-www-form-urlencoded',
# 'Cookie':'ASPSESSIONIDAARQBDRC=KMKPEHDBPDGLNDPFFMIBPDBP',
# 'Host': 'www.csx.com.ky',
# 'Origin':'http://www.csx.com.ky',
# 'Referer':'http://www.csx.com.ky/TradeList/TradeList.asp',
# 'User-Agent' :'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'}

url = 'http://trai.gov.in/Content/QosUser/1_QosUser.aspx/ctl00$ContentPlaceHolder1$gv_Qos'

response = requests.post(url, data = { '__EVENTTARGET':  'ctl00$ContentPlaceHolder1$gv_Qos', '__EVENTARGUMENT': 'Page$3'}, headers = headers)



data = []
imp = response.text.encode('utf-8')
Soup_obj = BeautifulSoup(imp)
print imp
# table = Soup_obj.find("div", { "class" : "gridevent_1" })
# print table
# rows = table.findAll("tr")
# for row in rows:
# 	cols = row.findAll('td')
# 	print cols , "???????"
# 	cols = [ele.text.strip() for ele in cols]
# 	data.append([ele for ele in cols if ele])
# for ele in data:
# 	# print ele 
# 	if len(ele) > 0:
# 		res=  ele[0] + "|" +ele[1] + "|" +ele[2] + "|" +ele[3] + "|" +ele[4] + "|" +ele[5] + "|" +ele[6] + "|" + ele[7] + "|" + ele[8]  + '\n'
# 		output1.write(res)
# 		print res
# output1.close()


