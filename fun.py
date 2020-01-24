from seleniumrequests import Chrome


webdriver = Chrome()
webdriver.get("https://data.nasdaq.com/BookViewer.aspx")
webdriver.find_element_by_id("txtUserName").send_keys("7818207")
webdriver.find_element_by_id("txtPassword").send_keys("TomTian1996")
webdriver.find_element_by_id("btnLogin").click()
webdriver.find_element_by_id("PageContent_btnLaunchBv3").click()
webdriver.switch_to.window(webdriver.window_handles[1])
webdriver.find_element_by_id("mpid-input").send_keys("AAPL")
webdriver.find_element_by_class_name("green-button.left").click()

response = webdriver.request('POST', 'https://gdp.nasdaq.com/bookviewer/services/bvService/getData', data={"payload":{"symbol":"AAPL","displayOnly":"0","mmid":"ALL","type":'1'},"triggeredByPolling":'true'})



from hyper import HTTPConnection
c = HTTPConnection('gdp.nasdaq.com:443')
c.request('GET','/bookviewer/?token=UZ1N1cJE23G7MMQdUNLGDjRIJEHVdbVL')

import certifi
print(certifi.where())


#Login
import httplib2
h = httplib2.Http(".cache",disable_ssl_certificate_validation=True)
(resp_headers, content) = h.request("https://gdp.nasdaq.com:443/bookviewer/?token=kJfAAjIMFGbZfXN1ZfWhlfVWbQXj1RgH", "GET")


#Authenticate
import urllib.parse


headers = {'Content-type':'application/json;charset=UTF-8','cookie':'XSRF-TOKEN=ahYB9iKKIR19HVIGMOOLdjl2DEeHT1N4; clientPrefs=||||lightg; _ga=GA1.2.1077599951.1574003379; _fbp=fb.1.1574003379191.471110038; __qca=P0-621622859-1574003379552; __gads=ID=9bfb2738c447382e:T=1574003381:S=ALNI_MbHJjOM3TZycFKWFOxUENxNGsfnIA; s_pers=%20bc%3D2%7C1574089805820%3B%20s_nr%3D1574004055252-New%7C1581780055252%3B; tc_ptid=3W0GIrf4BZ6azcyQTj91kW; tc_ptidexpiry=1637149473116; visid_incap_816592=mHW3VI7iQzyshgLXfoW97Op9+10AAAAAQUIPAAAAAAADnkXTNvUgbfsGtRTcdeUU; incap_ses_198_816592=hMb/eDT6EXntE5jl5XK/AkKqA14AAAAAs4lIdk3vVtHw91Oid98p/A==','authority':'gdp.nasdaq.com','method':'POST','path':'/bookviewer/services/bvService/authenticateUser','scheme':'https','accept':'application/json, text/plain, */*','accept-encoding':'gzip, deflate, br','accept-language':'en-US,en;q=0.9','content-length':'68','origin':'https://gdp.nasdaq.com','referer':'https://gdp.nasdaq.com:443/bookviewer/?token=TMdmmG367QcmE1RA4LUUQHWhYNKhdm9c','sec-fetch-mode':'cors','sec-fetch-site':'same-origin'}
headers = {'Content-type':'application/json;charset=UTF-8','authority':'gdp.nasdaq.com','method':'POST','path':'/bookviewer/services/bvService/authenticateUser','origin':'https://gdp.nasdaq.com','referer':'https://gdp.nasdaq.com:443/bookviewer/?token=NlTONMJL7NVRA2jaaiVCXSTLiOQ1b4dH'}
headers = {'Content-type':'application/json;charset=UTF-8'}
body = {'token':'TMdmmG367QcmE1RA4LUUQHWhYNKhdm9c','uniqueIdentifier':'null'}
http = httplib2.Http(".cache",disable_ssl_certificate_validation=True)
url = "https://gdp.nasdaq.com/bookviewer/services/bvService/authenticateUser"
response, content = http.request(url, 'POST', headers=headers, body=urllib.parse.urlencode(body))



#Get stock data
headers = {'Content-Type':'application/json;charset=UTF-8','cookie':'XSRF-TOKEN=NDYydXVqajh0bTl0aXBqMmVjdXFiNzhzZTc; visid_incap_816592=iw7452urSVewpwH83pSMzKN5A14AAAAAQUIPAAAAAABMIyj7/VavelrrdFT6aj1K; incap_ses_947_816592=p2DRfTELtTbGPO8WW2wkDaR5A14AAAAAxYVlswxMIdaZO1wkjXx32Q==; incap_ses_542_816592=KBMsMQKC8AbNJ/Z0jpOFB/l6A14AAAAAsKJH9LxPHTXpdJI001pBdA==','authority':'gdp.nasdaq.com','method':'POST','path':'/bookviewer/services/bvService/getData','scheme':'https','accept':'application/json, text/plain, */*','accept-encoding':'gzip, deflate, br','accept-language':'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6','content-length':'95','origin':'https://gdp.nasdaq.com','referer':'https://gdp.nasdaq.com:443/bookviewer/?token=cGB9FlLGgG8XBj48FeQOUgWbD34AkWF4','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','x-xsrf-token':'NDYydXVqajh0bTl0aXBqMmVjdXFiNzhzZTc'}
headers = {'sec-fetch-mode':'cors','x-xsrf-token':'NDYydXVqajh0bTl0aXBqMmVjdXFiNzhzZTc','referer':'https://gdp.nasdaq.com:443/bookviewer/?token=cGB9FlLGgG8XBj48FeQOUgWbD34AkWF4'}
body = {"payload":{"symbol":"NDAQ","displayOnly":"0","mmid":"ALL","type":'1'},"triggeredByPolling":'true'}
url = 'https://gdp.nasdaq.com/bookviewer/services/bvService/getData'
response, content = http.request(url, 'POST',headers = headers, body=urllib.parse.urlencode(body))


#Working codes below<3<3


import httplib2
h = httplib2.Http(".cache",disable_ssl_certificate_validation=True)
url = "https://gdp.nasdaq.com/bookviewer/services/bvService/authenticateUser"

payload = "{\"token\":\"UCEDUIiJjZBAMOdW3ba9NPYTLBBOTTdk\",\"uniqueIdentifier\":null}"
headers = {
  'Content-Type': 'application/json;charset=UTF-8',
  'cookie': 'XSRF-TOKEN=MmhlY3EyOHAxNHNwN2J2NGlmdmI5c3Vmc3A;visid_incap_816592=mHW3VI7iQzyshgLXfoW97Op9+10AAAAAQUIPAAAAAAADnkXTNvUgbfsGtRTcdeUU;',
  'authority': 'gdp.nasdaq.com',
  'method': 'POST',
  'path': '/bookviewer/services/bvService/authenticateUser',
  'scheme': 'https',
  'accept': 'application/json, text/plain, */*',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
  'content-length': '68',
  'origin': 'https://gdp.nasdaq.com',
  'referer': 'https://gdp.nasdaq.com:443/bookviewer/?token=UCEDUIiJjZBAMOdW3ba9NPYTLBBOTTdk',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin'
}

response, content = h.request(url, 'POST',headers = headers,body=payload)



#Get data
import httplib2
h = httplib2.Http(".cache",disable_ssl_certificate_validation=True)
url = "https://gdp.nasdaq.com/bookviewer/services/bvService/getData"

payload = "{\"payload\":{\"symbol\":\"AAPL\",\"displayOnly\":\"0\",\"mmid\":\"ALL\",\"type\":1},\"triggeredByPolling\":true}"
headers = {
  'Content-Type': 'application/json;charset=UTF-8',
  'cookie': 'XSRF-TOKEN=MmJmdnA0Y3ZyZmY2Y2xlZXZra2hrNzg3MTM; visid_incap_816592=mHW3VI7iQzyshgLXfoW97Op9+10AAAAAQUIPAAAAAAADnkXTNvUgbfsGtRTcdeUU; incap_ses_947_816592=p2DRfTELtTbGPO8WW2wkDaR5A14AAAAAxYVlswxMIdaZO1wkjXx32Q==; incap_ses_542_816592=KBMsMQKC8AbNJ/Z0jpOFB/l6A14AAAAAsKJH9LxPHTXpdJI001pBdA==',
  'authority': 'gdp.nasdaq.com',
  'method': 'POST',
  'path': '/bookviewer/services/bvService/getData',
  'scheme': 'https',
  'accept': 'application/json, text/plain, */*',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
  'content-length': '95',
  'origin': 'https://gdp.nasdaq.com',
  'referer': 'https://gdp.nasdaq.com/bookviewer/?token=EUgjNKj32HK6FHPPLhU4TFe7gikN8aZZ',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'x-xsrf-token': 'MmJmdnA0Y3ZyZmY2Y2xlZXZra2hrNzg3MTM'
}

response, content = h.request(url, 'POST',headers = headers,body=payload)

#Ping Server
import httplib2
h = httplib2.Http(".cache",disable_ssl_certificate_validation=True)
url = "https://gdp.nasdaq.com/bookviewer/services/bvService/pingServer"

payload = "{\"payload\":{\"triggeredByPolling\":\"false\"}"
headers = {
  'Content-Type': 'application/json;charset=UTF-8',
  'cookie': 'XSRF-TOKEN=MmhlY3EyOHAxNHNwN2J2NGlmdmI5c3Vmc3A; visid_incap_816592=mHW3VI7iQzyshgLXfoW97Op9+10AAAAAQUIPAAAAAAADnkXTNvUgbfsGtRTcdeUU; incap_ses_947_816592=p2DRfTELtTbGPO8WW2wkDaR5A14AAAAAxYVlswxMIdaZO1wkjXx32Q==; incap_ses_542_816592=KBMsMQKC8AbNJ/Z0jpOFB/l6A14AAAAAsKJH9LxPHTXpdJI001pBdA==',
  'authority': 'gdp.nasdaq.com',
  'method': 'POST',
  'path': '/bookviewer/services/bvService/getData',
  'scheme': 'https',
  'accept': 'application/json, text/plain, */*',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
  'content-length': '95',
  'origin': 'https://gdp.nasdaq.com',
  'referer': 'https://gdp.nasdaq.com/bookviewer/?token=1cL41LGIdFUjNNbHQj7fAJVgWjdHRGSV',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'x-xsrf-token': 'MmhlY3EyOHAxNHNwN2J2NGlmdmI5c3Vmc3A'
}

response, content = h.request(url, 'POST',headers = headers,body=payload)

#PoolExecutor

import concurrent.futures
import time
def download(ticker):
    time.sleep(0.2)
    print(ticker)

import random

def next():
  rlist = ['AAPL','TWTR','CONN','DAFAQ']
  return random.choice(rlist)

import concurrent.futures
if __name__ == '__main__'
    with concurrent.futures.ProcessPoolExecutor(max_workers=8) as e:
      while(True):
        e.submit(download,'aapl')