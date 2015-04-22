import requests
from BeautifulSoup import BeautifulSoup
import csv
import json
import ast
import datetime

output1 = open('Iraq_stock.txt', 'a')


url = 'http://www.isx-iq.net/isxportal/portal/sectorPerformance.html?1429164546022=&1429164622261=&1429165284817=&d-3989954-p=49&1429160117990=&1429164610718=&1429165061027=&1429164413895=&1429163557024=&1429164870500=&1429164493599=&1429163817642=&1429163868722=&1429163582557=&1429164437480=&1429163794348=&1429163625948=&1429165366960=&1429165355024=&1429164853900=&1429163454766=&toDate=09/04/2015&1429164914958=&1429165004789=&1429160151638=&1429165079467=&1429163509453=&fromDate=01/01/2010&1429164840093=&1429165299978=&1429165259370=&1429164929979=&1429163491222=&1429161815889=&1429165380040=&1429163894434=&1429164566200=&1429165045963=&1429163474760=&1429163534021=&1429164648949=&1429164596293=&1429165342569=&1429164899325=&1429165025962=&1429163694628=&1429164514503=&1429163659838=&1429164980747=&1429160204892=&1429165312832=&1429164434232=&1429165327721=&sectorId=1&1429163640292=&1429164941604=&1429164807220=&1429165392751'


response = requests.get(url)
# print response

data = []
imp = response.text

Soup_obj = BeautifulSoup(imp)
table = Soup_obj.find("table", { "class" : "table-allcontent" })

# print table 
rows = table.findAll("tr")
# print rows

for ele in rows:
	cls = ele.findAll('td')
	data = []
	for elem in cls :
		data.append(elem.text)
		if len(data) == 9 :
			# print data [0] , data[1] , data[2] , data[3] , 
			# print data[0] , data[1] ,data[2] ,data[3] ,data[4] ,ele[8]

			res =  data[0] + "|" +data[1] + "|" +data[2] + "|" +data[3] + "|" +data[4] + "|" +data[8] + '\n'
			print res 
			output1.write(res)


	