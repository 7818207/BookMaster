from selenium import webdriver
import re
import time
from selenium.webdriver.chrome.options import Options
class URLfetcher:

    def fetchURL(self, n):
        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {'profile.managed_default_content_settings.javascript': 2})

        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get("https://data.nasdaq.com/BookViewer.aspx")
        driver.find_element_by_id("txtUserName").send_keys("7818207")
        driver.find_element_by_id("txtPassword").send_keys("TomTian1996")
        driver.find_element_by_id("btnLogin").click()

        urllist = []
        cookies = []
        for i in range(n):
            driver.find_element_by_id("PageContent_btnLaunchBv3").click()
            time.sleep(0.3)
            cookies.append(driver.get_cookies())
            #driver.switch_to.window(driver.window_handles[i+1])
            #driver.find_element_by_id("mpid-input").send_keys(slist[i])
            #driver.find_element_by_class_name("green-button.left").click()
            src = driver.page_source
            match = re.search("window.open\((.*)\)",src,re.IGNORECASE).group(1)
            url = match.split(",")[0][1:-1]
            urllist.append(url)
        return urllist