import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# CONSTANTS
PROMISED_DOWN = 200
PROMISED_UP = 200
CHROME_DRIVER_PATH = "YOUR CHROME DRIVER PATH"
TWITTER_EMAIL = "YOUR EMAIL ADDRESS"
TWITTER_PASSWORD = "YOUR PASSWORD"

# URLS
speed_test_url = "https://www.speedtest.net/"
twitter_url = "https://twitter.com/i/flow/login"

service = Service(CHROME_DRIVER_PATH)


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=driver_path)
        self.up = PROMISED_UP
        self.down = PROMISED_DOWN
        self.up_and_down = ("up", "down")

    def get_internet_speed(self):
        self.driver.get(url=speed_test_url)

        time.sleep(3)
        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()
        time.sleep(45)
        download_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div['
                                                            '2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div['
                                                            '1]/div[ '
                                                            '2]/div/div[2]/span').text
        upload_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                          '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
                                                          '3]/div/div[2]/span').text
        print(f"Download speed: {download_speed}")
        print(f"Upload speed: {upload_speed}")
        self.up_and_down = (upload_speed, download_speed)

    def tweet_at_provider(self):
        self.driver.get(url=twitter_url)
        up = self.up_and_down[0]
        down = self.up_and_down[1]

        time.sleep(5)
        email_field = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                         '2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div['
                                                         '2]/div/input')
        email_field.send_keys(TWITTER_EMAIL)
        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                         '2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        next_button.click()

        time.sleep(3)
        password_field = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                            '2]/div/div/div[2]/div[2]/div[1]/div/div/div['
                                                            '3]/div/label/div/div[2]/div[1]/input')
        password_field.send_keys(TWITTER_PASSWORD)
        password_field.send_keys(Keys.ENTER)
        # login_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
        #                                                   '2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        # login_button.click()

        time.sleep(5)
        my_message = f"Hey internet Provider, why is my internet speed {down}mbps down/{up}mbps up when I pay for " \
                     f"100mbps up/100mbps down?"
        tweet_input_field = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div['
                                                               '2]/main/div/div/div/div/div/div[2]/div/div[2]/div['
                                                               '1]/div/div/div/div[2]/div['
                                                               '1]/div/div/div/div/div/div/div/div/div/label/div['
                                                               '1]/div/div/div/div/div[2]/div/div/div/div')
        tweet_input_field.send_keys(my_message)
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div['
                                                          '2]/main/div/div/div/div/div/div[2]/div/div[2]/div['
                                                          '1]/div/div/div/div[2]/div[3]/div/div/div[2]/div['
                                                          '3]/div/span/span')
        tweet_button.click()

    def quit_webdriver(self):
        time.sleep(5)
        self.driver.quit()


my_bot = InternetSpeedTwitterBot(service)

my_bot.get_internet_speed()
my_bot.tweet_at_provider()
my_bot.quit_webdriver()
