import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service = Service(executable_path=".\chromedriver.exe")
driver = webdriver.Chrome()

description_id = "feature-bullets"
ASIN_xpath = "//span[contains(text(), 'ASIN')]/../span[2]"
product_description_id = "productDescription_feature_div"
manufacturer_xpath = "//span[contains(text(), 'Manufacturer')]/../span[2]"




products = pd.read_csv(".\\result.csv")
products["Description"] = [None]*len(products)
products["ASIN"] = [None]*len(products)
products["Product Description"] = [None]*len(products)
products["Manufacturer"] = [None]*len(products)

for i in range(len(products)):
    product_url = products["Product URL"][i]
    driver.get(product_url)
    time.sleep(5)
    description = driver.find_element(by='id',value=description_id)
    ASIN = driver.find_element(by="xpath", value=ASIN_xpath)
    manufacturer = driver.find_element(by="xpath", value=manufacturer_xpath)
    product_description = driver.find_element(by="id", value=product_description_id)
    products["Description"][i] =  description.text
    products["ASIN"][i] =  ASIN.text
    products["Product Description"][i] =  product_description.text
    products["Manufacturer"][i] =  manufacturer.text

products.to_csv(".\\result2.csv")
