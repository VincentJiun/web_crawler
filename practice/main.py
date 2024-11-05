from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
import os
import time

DRIVER_PATH = os.path.join(os.getcwd(), 'chromedriver-win64', 'chromedriver.exe')

SERVEICE = Service(executable_path=DRIVER_PATH)

OPTIONS = webdriver.ChromeOptions()

URL = 'https://www.facebook.com/?locale=zh_TW'

LOGIN_URL = 'https://www.facebook.com/login/'

class Facebook_Crawler():
    def __init__(self):
        self.driver = webdriver.Chrome(service=SERVEICE, options=OPTIONS)
        self.login_state = -1

    def set_cookies(self):
        pass

    def login(self):
        if self.login_state == -1:
            self.driver.get(LOGIN_URL)
            print('開始登入')
            time.sleep(10)
        else:
            print('已登入')

if __name__ == '__main__':
    fb = Facebook_Crawler()
    fb.login()
