from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

service = Service(executable_path=".\chromedriver.exe")
driver = webdriver.Chrome(service=service)
columns = [
    "Product name",
    "Product URL",
    "Product Price",
    "Rating",
    "Number of Reviews",
]
products = pd.DataFrame(columns=columns)


products_xpath = "//div[@class='a-section']/div[@class='sg-row']"
relative_name_xpath = ".//h2/a"
relative_price_xpath = ".//span[@class='a-price-whole']"
relative_ratings_xpath = ".//div[@class='a-section a-spacing-none a-spacing-top-micro']/div[@class='a-row a-size-small']/span[1]"
relative_reviews_xpath = ".//div[@class='a-section a-spacing-none a-spacing-top-micro']/div[@class='a-row a-size-small']/span[2]"

next_button_xpath = "//a[@class='s-pagination-item s-pagination-next s-pagination-button s-pagination-separator']"

driver.get(
    "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"
)

# 20 pages
for i in range(20):
    # each page all products
    prods = driver.find_elements(by="xpath", value=products_xpath)
    print(len(prods))
    # for each product in the page, get details
    for prod in prods:
        prod_name = prod.find_element(by="xpath", value=relative_name_xpath)
        prod_price = prod.find_element(by="xpath", value=relative_price_xpath)
        prod_price = prod_price.text
        try:
            prod_rating = prod.find_element(by="xpath", value=relative_ratings_xpath)
            prod_rating = prod_rating.text
        except:
            prod_rating = "Unrated"

        try:
            prod_reviews = prod.find_element(by="xpath", value=relative_reviews_xpath)
            prod_reviews= prod_reviews.text
        except:
            prod_reviews = "0"
        
        new_row = {
            "Product name": prod_name.text,
            "Product URL": prod_name.get_attribute("href"),
            "Product Price": prod_price,
            "Rating": prod_rating,
            "Number of Reviews": prod_reviews,
        }

        # add product details in the data frame
        products.loc[len(products)] = new_row

    # go to next page
    if i<19:
        time.sleep(5)
        next_button = driver.find_element(by="xpath",value=next_button_xpath)
        next_button.click()
        time.sleep(5)

products.to_csv(".\\result.csv", index=False)


driver.close()
driver.quit()
