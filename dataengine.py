from selenium import webdriver
import re
import time
from selenium.webdriver.chrome.options import Options
import httplib2
import json
import random
from multiprocessing import Process, Manager
import concurrent.futures
import scheduler
import pickle



def getSingle(arglist):
    rurl = arglist[0]
    client = arglist[1]
    ticker = arglist[2]
    token = arglist[3]
    contentDict = arglist[4]
    url = "https://gdp.nasdaq.com/bookviewer/services/bvService/getData"
    payload = "{\"payload\":{\"symbol\":\"%s\",\"displayOnly\":\"0\",\"mmid\":\"ALL\",\"type\":1},\"triggeredByPolling\":true}" % ticker

    headers = {
        'authority': 'gdp.nasdaq.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'accept': 'application/json, text/plain, */*',
        'origin': 'https://gdp.nasdaq.com',
        'x-xsrf-token': '%s' % token,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
        'content-type': 'application/json;charset=UTF-8',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'referer': '%s' % rurl,
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'XSRF-TOKEN=%s; visid_incap_816592=mHW3VI7iQzyshgLXfoW97Op9+10AAAAAQUIPAAAAAAADnkXTNvUgbfsGtRTcdeUU; incap_ses_947_816592=p2DRfTELtTbGPO8WW2wkDaR5A14AAAAAxYVlswxMIdaZO1wkjXx32Q==; incap_ses_542_816592=KBMsMQKC8AbNJ/Z0jpOFB/l6A14AAAAAsKJH9LxPHTXpdJI001pBdA=='% token
    }
    response, content = client.request(url, 'POST', headers=headers, body=payload)
    try:
        d = json.loads(content)
    except json.decoder.JSONDecodeError:
        print(ticker)
        print('json failed')
        return
    appendNew(contentDict,ticker,d)
    print('one downloaded')
    time.sleep(0.001)
'''
def getSingle(arglist):
    rurl = arglist[0]
    client = arglist[1]
    ticker = arglist[2]
    token = arglist[3]
    contentDict = arglist[4]
    url = "https://gdp.nasdaq.com/bookviewer/services/bvService/getData"
    payload = "{\"payload\":{\"symbol\":\"%s\",\"displayOnly\":\"0\",\"mmid\":\"ALL\",\"type\":1},\"triggeredByPolling\":true}" % ticker
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'cookie': 'XSRF-TOKEN=%s; visid_incap_816592=mHW3VI7iQzyshgLXfoW97Op9+10AAAAAQUIPAAAAAAADnkXTNvUgbfsGtRTcdeUU; incap_ses_947_816592=p2DRfTELtTbGPO8WW2wkDaR5A14AAAAAxYVlswxMIdaZO1wkjXx32Q==; incap_ses_542_816592=KBMsMQKC8AbNJ/Z0jpOFB/l6A14AAAAAsKJH9LxPHTXpdJI001pBdA==' % token,
        'authority': 'gdp.nasdaq.com',
        'method': 'POST',
        'path': '/bookviewer/services/bvService/getData',
        'scheme': 'https',
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
        'content-length': '95',
        'origin': 'https://gdp.nasdaq.com',
        'referer': '%s' % rurl,
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'x-xsrf-token': '%s' % token
    }
    response, content = client.request(url, 'POST', headers=headers, body=payload)
    try:
        d = json.loads(content)
    except json.decoder.JSONDecodeError:
        print(ticker)
        print('failed')
        return
    appendNew(contentDict,ticker,d)
    #time.sleep(0.001)
    
    '''

def appendNew(contentDict,ticker,data):
    if(len(contentDict[ticker])>0):
        last = contentDict[ticker][-1]
        if(data != last):
            contentDict[ticker].append(data)
    else:
        contentDict[ticker].append(data)



class DataEngine:
    #launch pages for requests

    #Obtain a token by manually initiate a connection.
    def __init__(self,token,n_urls = 16):
        self.n_urls = n_urls
        self.scheduler = scheduler.Scheduler({},n_urls)

        #Manager is the storage unit
        #self.manager = Manager()
        #self.contentDict = self.manager.dict()

        #Http clientpool
        self.generateHttpClients()

        #Session Token
        self.token = token

        #AcquireURLSandAuthenticate them
        self.establishConnection(n_urls)

        #Dictionary for storing downloaded data
        self.ContentDict = {}

        #used to store tickers that fail to download
        self.failedTicker = []

    def generateHttpClients(self):
        self.httpClientQueue = []
        for i in range(self.n_urls):
            http = httplib2.Http(".cache", disable_ssl_certificate_validation=True)
            self.httpClientQueue.append(http)

    def updatePriority(self,priorityDict):
        #Both Scheduler and Manager are empty on startup, so must populate both of them upon startup

        #Update scheduler first
        self.scheduler.updateScheduler(priorityDict=priorityDict)

        #Update Manager
        keys = priorityDict.keys()
        for k in keys:
            if k not in self.ContentDict.keys():
                #self.contentDict[k] = self.manager.list()
                self.ContentDict[k] = []

    def getHttpClient(self):
        client = self.httpClientQueue.pop(0)
        self.httpClientQueue.append(client)
        return client

    def authenticate(self,url):
        httpclient = self.getHttpClient()
        ourl = "https://gdp.nasdaq.com/bookviewer/services/bvService/authenticateUser"
        src = url
        address_token = re.search("token=(.*)",src,re.IGNORECASE).group(1)
        payload = "{\"token\":\"%s\",\"uniqueIdentifier\":null}"%address_token
        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'cookie': 'XSRF-TOKEN=%s; visid_incap_816592=mHW3VI7iQzyshgLXfoW97Op9+10AAAAAQUIPAAAAAAADnkXTNvUgbfsGtRTcdeUU; '%self.token,
            'authority': 'gdp.nasdaq.com',
            'method': 'POST',
            'path': '/bookviewer/services/bvService/authenticateUser',
            'scheme': 'https',
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
            'content-length': '68',
            'origin': 'https://gdp.nasdaq.com',
            'referer': '%s'%url,
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin'
        }

        response, content = httpclient.request(ourl, 'POST', headers=headers, body=payload)
        d = json.loads(content)
        self.token = d['data']['sessionToken']

    def establishConnection(self,n_urls):

        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {'profile.managed_default_content_settings.javascript': 2})
        chrome_options.set_headless(True)
        print('starting up web browser')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get("https://data.nasdaq.com/BookViewer.aspx")
        driver.find_element_by_id("txtUserName").send_keys("7818207")
        driver.find_element_by_id("txtPassword").send_keys("TomTian1996")
        driver.find_element_by_id("btnLogin").click()

        print('obtaining url lists')
        self.urllist = []
        self.authenticateStatus = []
        cookies = []
        for i in range(n_urls):
            driver.find_element_by_id("PageContent_btnLaunchBv3").click()
            time.sleep(0.3)
            cookies.append(driver.get_cookies())
            #driver.switch_to.window(driver.window_handles[i+1])
            #driver.find_element_by_id("mpid-input").send_keys(slist[i])
            #driver.find_element_by_class_name("green-button.left").click()
            src = driver.page_source
            match = re.search("window.open\((.*)\)",src,re.IGNORECASE).group(1)
            url = match.split(",")[0][1:-1]
            self.urllist.append(url)
        print('Authenticating urls')
        for url in self.urllist:
            self.authenticate(url)

    def streamData(self):
        
        ####################
        import time
        start_time = time.time()
        ####################
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=17) as e:
            counter = 0
            while (True):
                nextsym = self.scheduler.getNext()
                arglist = [random.choice(self.urllist),self.getHttpClient(),nextsym,self.token,self.ContentDict]
                e.submit(getSingle, arglist)
                counter+=1
                 
                if(counter % 3000 == 0):
                    e.shutdown(wait = True)
                    print(time.time() - start_time)
                    pickle_out = open("contentdict.pickle","wb")
                    pickle.dump(self.ContentDict, pickle_out)
                    pickle_out.close()
                    return;


    def getDataFromList(self,symbols):
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as e:
            for s in symbols:
                arglist = [random.choice(self.urllist), self.getHttpClient(), s, self.token,
                           self.ContentDict]
                e.submit(getSingle,arglist)
                time.sleep(0.001)
    
    def psuedoStream(self):

        import time


        counter = 0
        global_start = time.time()
        while(True):
            arglist = [random.choice(self.urllist), self.getHttpClient(), self.scheduler.getNext(), self.token,
                   self.ContentDict]
            start_time = time.time()
            getSingle(arglist)
            counter += 1

            if(counter == 300):
                print('total:')
                print(time.time() - global_start)
                return



    def getContentDict(self):
        return self.ContentDict