import requests
from BeautifulSoup import BeautifulSoup
import csv

output1 = open('D:\\Innovaccer\\Tim Reisen\\Output\\Stock\\Step_1_Out.txt', 'w')




for row in tex:
	output1 = open('D:\\Innovaccer\\Tim Reisen\\Output\\Stock\\'+str(row[0])+'.txt', 'w')
	
	for i in range(0,46):
		try:
			idnum = 30*i
			print idnum
			cntry = row[0]
			url = str(row[2]) + str(idnum)
			print url
			
			response = requests.get(url)
			
			data = []
			imp = response.text
			
			Soup_obj = BeautifulSoup(imp)
			table = Soup_obj.find("table", { "class" : "gf-table historical_price" })
			rows = table.findAll("tr")
		except:
			pass
		
		for x in rows:
			cols = x.findAll('td')
			cols = [ele.text.strip() for ele in cols]
			data.append([ele for ele in cols if ele]) 

		for ele in data:
			# print len(ele)
			if len(ele) > 0:
				res=  ele[0] + "|" +ele[1] + "|" +ele[2] + "|" +ele[3] + "|" +ele[4] + "|" +ele[5] + '\n'
				output1.write(res)

	output1.close()




