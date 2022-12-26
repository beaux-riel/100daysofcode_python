from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "day48/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.ca/Windows-Mini-Single-Board-Computer/dp/B0BDFDTCD4/ref=sr_1_2?crid=1J27JDM0EUFRO&keywords=lattepanda&qid=1671687865&sprefix=latte+panda%2Caps%2C178&sr=8-2")
price_symbol = driver.find_element(By.CLASS_NAME, "a-price-symbol")
price_whole = driver.find_element(By.CLASS_NAME, "a-price-whole")
price_fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction")
price_total = f'{price_symbol.text}{price_whole.text}.{price_fraction.text}'

print(price_total)

# driver.close()
driver.quit()