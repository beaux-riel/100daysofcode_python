from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def tweet_at_provider(self):
    self.driver.get("https://twitter.com/login")

    time.sleep(2)
    email = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
    password = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')

    email.send_keys(TWITTER_EMAIL)
    password.send_keys(TWITTER_PASSWORD)
    time.sleep(2)
    password.send_keys(Keys.ENTER)

    time.sleep(5)
    tweet_compose = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

    tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
    tweet_compose.send_keys(tweet)
    time.sleep(3)

    tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
    tweet_button.click()

    time.sleep(2)
    self.driver.quit()