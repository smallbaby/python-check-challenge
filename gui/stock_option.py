# -*- coding: utf-8 -*-
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.barchart.com/options/highest-implied-volatility")
#web1 = driver.find_element_by_class_name("odd")
web1 = driver.find_element("class", "odd")
print(web1)
print(web1.text)
driver.close()