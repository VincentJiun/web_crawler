from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
import os
import time

DRIVER_PATH = os.path.join(os.getcwd(), 'chromedriver-win64', 'chromedriver.exe')


URL = 'https://www.instagram.com/'

EMAIL = 'vincent7955168@gmail.com'

PASSWORD = 'Eggsy7955168~'

class IG_Crawler():
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        # Options 設定
        self.prefs = {
            'profile.default_content_setting_values': 
                {
                    'notifications': 2
                }
            }
        self.options.add_experimental_option('prefs', self.prefs) # 關閉訊息通知
        self.options.add_experimental_option('detach', True) # 避免自動關閉瀏覽器
        self.options.add_argument('--log-level=1') # https://stackoverflow.com/questions/78530683/created-tensorflow-lite-xnnpack-delegate-for-cpu-message-randomly-appears-when
        self.driver = webdriver.Chrome(options=self.options, service=Service(DRIVER_PATH))
        self.login_state = False

    def login(self):
        self.driver.get(URL)
        username = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.NAME, "username")))
        password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.NAME, "password")))
        username.clear()
        username.send_keys(EMAIL)
        password.clear()
        password.send_keys(PASSWORD)
        time.sleep(5)
        submit = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit.click()
        # 儲存資料
        button_save = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/section/div/button')))
        button_save.click()
        time.sleep(30)
        # button_save = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/section/div/button')

    def post(self):
        # nav = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, 'x1iyjqo2 xh8yej3')))
        new_post = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label=新貼文]")))
        new_post.click()

        find = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='從電腦選擇']")))
        find.click()
        # search = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mount_0_0_dj"]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input')))
        # search.send_keys('test')
        # search.send_keys(Keys.RETURN)






if __name__ == '__main__':
    ig = IG_Crawler()
    ig.login()

