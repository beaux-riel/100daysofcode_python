from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "day48/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://secure-retreat-92358.herokuapp.com")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Beaux")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Walton")
email = driver.find_element(By.NAME, "email")
email.send_keys("beaux.walton@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

# wikiversity = driver.find_element(By.LINK_TEXT, "Wikiversity")
# wikiversity.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)