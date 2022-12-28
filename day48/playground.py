from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "day48/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org")
# price_symbol = driver.find_element(By.CLASS_NAME, "a-price-symbol")
# price_whole = driver.find_element(By.CLASS_NAME, "a-price-whole")
# price_fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction")
# price_total = f'{price_symbol.text}{price_whole.text}.{price_fraction.text}'
# print(price_total)

# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar)

# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)
