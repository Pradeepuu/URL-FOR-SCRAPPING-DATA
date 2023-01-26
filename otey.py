from select import select

import time
from typing import TextIO
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

Result = [
    'https://www.oatey.com/products/oatey-liquilock-water-absorbing-crystals--1792398291',
    'https://www.oatey.com/products/oatey-heavy-duty-gray-pvc-cement-829232139',

]
for url in Result:
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup.prettify())
    opts = Options()
    opts.headless = True
    driver = webdriver.Chrome(r"C:\Users\PK\Downloads\chromedriver_win32/chromedriver", options=opts)
    driver.get(url)
    time.sleep(3)

    # title = driver.find_element(By.TAG_NAME,'h1')
    # print(title.text)

    # sku = driver.find_element(by=By.CLASS_NAME, value='container').find_elements(by=By.TAG_NAME,value='a')
    # for x in sku:
    #     print(x.text)

    lists = []
    sku = driver.find_elements(by=By.CLASS_NAME, value='breadcrumbs')
    for x in sku:
        lists.append(x.text)
    bread = (lists[1])
    print("Breadcrumb = ", bread)

    title = driver.find_element(by=By.CLASS_NAME, value='product-title')
    title_d = title.text
    print("title = ", title_d)

    description = driver.find_element(by=By.CLASS_NAME, value='sku-description')
    description_d = description.text
    print("description = ", description_d)

    feature = driver.find_element(by=By.CLASS_NAME, value='key-features-section')
    feature_d = feature.text
    print("feature = ", feature_d)

    image = driver.find_element(by=By.CLASS_NAME, value='slick-track').find_elements(by=By.TAG_NAME,value='img')
    for img in image:
        image_d = (img.get_attribute('src'))
        print("image = ", image_d)

    pdf = driver.find_elements(by=By.CLASS_NAME, value='download-link')
    for pd in pdf:
        pdf_d = (pd.get_attribute('href'))
        print("pdf = ", pdf_d)

    attr_v = []
    attr_n = []
    table = driver.find_elements(by=By.CLASS_NAME, value='table-striped')
    i = 0
    for x in table:
        dt = x.find_elements(by=By.TAG_NAME, value='td')
        for tdd in dt:
            i = i + 1
            # print(i)
            # print(tdd.text.strip())
            if i % 2 == 0:
                attr_v.append(tdd.text)
            else:
                attr_n.append(tdd.text)
    # print(attr_n)
    # print(attr_v)
    for m, n, in zip(attr_v, attr_n):
        print(n, "====", m)

