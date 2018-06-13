#encoding=utf-8
from selenium import webdriver
import unittest
import traceback
import time
import os
from selenium.common.exceptions import NoSuchElementException
import requests
from bs4 import BeautifulSoup
import re


def get_url():
    requests.packages.urllib3.disable_warnings()
    url = "https://ke.youdao.com"
    resq = requests.get(url, verify=False).text
    # <a href="https://ke.youdao.com/course/detail/9463?inLoc=fp_h_3&amp;Pdt=CourseWeb"
    ke_urls = re.findall(r"a href=\"(https://ke\.youdao\.com/course/detail/\d+)", resq)
    result_keurl = []
    for i in ke_urls:
        result_keurl.append(i)
    return result_keurl


def test_scroll_screenshot(filedir):
    with open("D:\\screen\\data.txt")as fp:
        for line in fp:
            if line.strip().lower == "chrome":
                driver = webdriver.Chrome(executable_path="D:\\python\\Scripts\\chromedriver.exe")
            elif line.strip().lower == "ie":
                driver = webdriver.Chrome(executable_path="D:\\python\\Scripts\\IEDriverServer.exe")
            elif line.strip().lower == "firefox":
                driver = webdriver.Chrome(executable_path="D:\\python\\Scripts\\geckodriver.exe")
            else:
                driver = webdriver.Chrome(executable_path="D:\\python\\Scripts\\chromedriver.exe")
    urls = get_url()
    for url in urls:
        driver.get(url)
        driver.maximize_window()
        time.sleep(3)
        n = 1
        if not os.path.exists(filedir):
            os.mkdir(filedir)
            print "make file dir done"
        while n < 3:
            try:
                path = os.path.join(filedir, str(time.time()) + ".png")
                result_png = driver.get_screenshot_as_file(os.path.join(filedir, str(time.time()) + ".png"))
                print u"已截图"
                time.sleep(2)
                driver.execute_script("window.scrollBy (0,document.body.scrollHeight)")
                time.sleep(1)
                n += 1
            except IOError, e:
                print e
    driver.quit()


if __name__ == '__main__':
    '''
    # 单进程截图
    t1 = time.time()
    for link in links:
        getScreenShot(link)
    print u"单进程耗时：", time.time() - t1
    # 多进程截图
    pool = Pool(5)
    t2 = time.time()
    pool.map(getScreenShot, links)
    print u"多进程耗时：", time.time() - t2
    '''
    test_scroll_screenshot("d:\\bbbb")