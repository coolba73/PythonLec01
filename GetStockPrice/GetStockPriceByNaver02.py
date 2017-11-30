import urllib
import time
import datetime
 
from urllib.request import urlopen
from bs4 import BeautifulSoup
  
stockItem = '005930'
 
url = 'http://finance.naver.com/item/sise_day.nhn?code='+ stockItem
html = urlopen(url) 
source = BeautifulSoup(html.read(), "html.parser")
 
maxPage=source.find_all("table",align="center")
mp = maxPage[0].find_all("td",class_="pgRR")
mpNum = int(mp[0].a.get('href')[-3:])

today = '{0:%Y-%m-%d}'.format(datetime.datetime.now())
fromDate = '{0:%Y-%m-%d}'.format(datetime.datetime( int(today.split('-')[0]) - 1 ,int(today.split('-')[1]) ,int(today.split('-')[2]) ))

yesStop = False;

for page in range(1, mpNum+1):

    url = 'http://finance.naver.com/item/sise_day.nhn?code=' + stockItem +'&page='+ str(page)
    html = urlopen(url)
    source = BeautifulSoup(html.read(), "html.parser")
    srlists=source.find_all("tr")
    isCheckNone = None

    # if((page % 1) == 0):
    #   time.sleep(1.50)

    for i in range(1,len(srlists)-1):
        
        if(srlists[i].span != isCheckNone):

            date = srlists[i].find_all("td",align="center")[0].text
            closestr = srlists[i].find_all("td",class_="num")[0].text.strip()

            date = date.replace(".","-")
            closePrice = float(closestr.replace(',',''))

            if (date < fromDate):
                break
                yesStop = True

            print ( date, closePrice)

    if (yesStop ==  True):
            break

print("end")

   


