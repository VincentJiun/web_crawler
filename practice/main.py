from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
import os
import time

DRIVER_PATH = os.path.join(os.getcwd(), 'chromedriver-win64', 'chromedriver.exe')


URL = 'https://www.facebook.com/'

LOGIN_URL = 'https://www.facebook.com/login/'

EMAIL = 'vincent7955168@gmail.com'

PASSWORD = 'Eggsy7955168~'

class Facebook_Crawler():
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('detach', True)
        self.options.add_argument('--log-level=1') # https://stackoverflow.com/questions/78530683/created-tensorflow-lite-xnnpack-delegate-for-cpu-message-randomly-appears-when
        self.driver = webdriver.Chrome(options=self.options) # 避免自動關閉瀏覽器
        self.login_state = -1

    def set_cookies(self):
        pass

    def login(self):
        if self.login_state == -1:
            self.driver.get(URL)
            print('開始登入')
            self.email = self.driver.find_element(By.ID, 'email')
            self.email.clear()
            self.email.send_keys(EMAIL)

            self.password = self.driver.find_element(By.ID, 'pass')
            self.password.clear()
            self.password.send_keys(PASSWORD)

            time.sleep(5)

            self.submit = self.driver.find_element(By.NAME, 'login')
            self.submit.click()
        else:
            print('已登入')

if __name__ == '__main__':
    fb = Facebook_Crawler()
    fb.login()
