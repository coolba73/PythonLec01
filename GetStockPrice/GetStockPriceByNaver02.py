import urllib
import time
import datetime
 
from urllib.request import urlopen
from bs4 import BeautifulSoup
  
# stockItem = '005930'

# ========================================================================================================================================================
def GetStockPrice(ItemCode):
    
    if (ItemCode == "KOSPI200"):
        urlsource = 'http://finance.naver.com/sise/sise_index_day.nhn?code='
        ItemCode = 'KPI200'
    else:
        urlsource = 'http://finance.naver.com/item/sise_day.nhn?code='

    url = urlsource+ ItemCode
    html = urlopen(url) 
    source = BeautifulSoup(html.read(), "html.parser")

    mpNum = 10000

    today = '{0:%Y-%m-%d}'.format(datetime.datetime.now())
    fromDate = '{0:%Y-%m-%d}'.format(datetime.datetime( int(today.split('-')[0]) - 1 ,int(today.split('-')[1]) ,int(today.split('-')[2]) ))

    yesStop = False;

    StockPriceList = []
    dayInfo = {}

    preHtml = ''

    for page in range(1, mpNum+1):

        url = urlsource + ItemCode +'&page='+ str(page)
        html = urlopen(url)

        if (preHtml == html):
            break

        source = BeautifulSoup(html.read(), "html.parser")
        srlists=source.find_all("tr")
        isCheckNone = None

        # if((page % 1) == 0):
        #   time.sleep(1.50)

        for i in range(1,len(srlists)-1):
            
            if(srlists[i].span != isCheckNone):
               

                # print ( srlists[i].find_all("td",class_="date")[0].text )
                # print ( srlists[i].find_all("td",class_="number_1")[0].text )
                # print(srlists)

                if (ItemCode == 'KPI200'):
                    date = srlists[i].find_all("td",class_="date")[0].text 
                    closestr = srlists[i].find_all("td",class_="number_1")[0].text 
                else:
                    date = srlists[i].find_all("td",align="center")[0].text
                    closestr = srlists[i].find_all("td",class_="num")[0].text.strip()                        

                date = date.replace(".","-")
                closePrice = float(closestr.replace(',',''))

                if (date < fromDate):
                    yesStop = True
                    break

                dayInfo = {}
                dayInfo["Index"] = date
                dayInfo["Close"] = closePrice

                StockPriceList.append(dayInfo)

                # print ( date, closePrice)

        if (yesStop ==  True):
                break
        
        preHtml = html

    print("end")
    result = {}
    result[ItemCode] = StockPriceList
    return result 
# ========================================================================================================================================================
   
# re = GetStockPrice("005930")
re = GetStockPrice("KOSPI200")

print(re)


