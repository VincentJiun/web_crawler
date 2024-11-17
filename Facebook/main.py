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


URL = 'https://www.facebook.com/'

# LOGIN_URL = 'https://www.facebook.com/login/'

# EMAIL = 'vincent7955168@gmail.com'

# PASSWORD = 'Eggsy7955168~'

POST_URL = 'https://www.facebook.com/,https://www.google.com/'

def account():
    result = []
    with open('./config/account.ini', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()  # 去除行首尾的空白字符
            if line:  # 確保非空行
                # 解析每行的內容
                parts = line.split(',')
                entry = {}
                for part in parts:
                    key, value = part.split('=')
                    entry[key] = value
                result.append(entry)
    return result









EMAIL = 'egg790508@hotmail.com'

PASSWORD = 'Eggsy7955168~'

WAIT_MIN = 3

class Facebook_Crawler():
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
        print('開始登入')
        # 搜尋 帳號/密碼 輸入框
        self.username = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, 'email')))
        self.password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, 'pass')))
        self.submit = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.NAME, 'login')))
        self.username.send_keys(EMAIL)
        self.password.send_keys(PASSWORD)
        time.sleep(5)
        self.submit.click()
        print(f'請在{WAIT_MIN}分鐘內驗證登入!!!')
        try:
            # 尋找首頁的Search Bar
            self.search = WebDriverWait(self.driver, int(WAIT_MIN*60)).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type=search]')))
            print('登入成功')
            self.login_state = True

        except:
            print('登入失敗')
            self.driver.quit()
        

    def post(self):
        self.login()
        time.sleep(5)

        if self.login_state:
            print('開始搜尋')
            self.search.click()
            # search.clear()
            self.search.send_keys('按讚')
            time.sleep(10)
            self.search.send_keys(Keys.RETURN)
            time.sleep(30)
            print('搜尋完畢')
            self.driver.quit()

        

        
             
        # <span class="x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft">嘗試其他方式</span>




if __name__ == '__main__':
    acc = account()
    for a in acc:
        if a['email']=='egg790508@hotmail.com':
            print(a['password'])
    # fb = Facebook_Crawler()
    # fb.post()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.chrome.options import Options
# import os
# import time

# DRIVER_PATH = os.path.join(os.getcwd(), './chromedriver-win64', 'chromedriver.exe')


# URL = 'https://www.facebook.com/'

# LOGIN_URL = 'https://www.facebook.com/login/'

# EMAIL = 'egg790508@hotmail.com'

# PASSWORD = 'Eggsy7955168~'

# class Facebook_Crawler():
#     def __init__(self):
#         self.options = webdriver.ChromeOptions()
#         # Options 設定
#         self.prefs = {
#             'profile.default_content_setting_values': 
#                 {
#                     'notifications': 2
#                 }
#             }
#         self.options.add_experimental_option('prefs', self.prefs) # 關閉訊息通知
#         self.options.add_experimental_option('detach', True) # 避免自動關閉瀏覽器
#         self.options.add_argument('--log-level=1') # https://stackoverflow.com/questions/78530683/created-tensorflow-lite-xnnpack-delegate-for-cpu-message-randomly-appears-when
#         self.driver = webdriver.Chrome(options=self.options) 
#         self.login_state = -1

#     def set_cookies(self):
#         pass

#     def login(self):
#         while self.login_state == -1:
#             self.driver.get(URL)
#             print('開始登入')
#             # 輸入帳號
#             self.driver.implicitly_wait(30)
#             self.email = self.driver.find_element(By.ID, 'email')
#             self.email.clear()
#             self.email.send_keys(EMAIL)
#             # 輸入密碼
#             self.password = self.driver.find_element(By.ID, 'pass')
#             self.password.clear()
#             self.password.send_keys(PASSWORD)
#             time.sleep(5)
#             # 點擊登入
#             self.submit = self.driver.find_element(By.NAME, 'login')
#             self.submit.click()

            
            
            
#             self.login_state = 1


#         print('已登入')

#         # 社團貼文 xpath
#         # /html/body/div[1]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div[4]/div/div[2]/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[1]/span

#         # 聯絡人email xpath
#         # /html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/span

#         # 行動電話
#         # /html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/span

#         # 沒有聯絡資料可顯示
#         # /html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div/div[2]/div/div/div[2]/span
# if __name__ == '__main__':
#     fb = Facebook_Crawler()
#     fb.login()

