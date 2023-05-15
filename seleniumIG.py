#爬取ig關鍵字圖片
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #讓電腦能模擬按鍵盤上的按鍵
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import wget

path = 'C:/Users/Louis/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(path)
url = ('https://www.instagram.com/')
driver.get(url)

#等待標籤出現才作什麼，並且會回傳你設的標籤
username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
passwowrd = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))

username.clear() #將回傳的內容清空，留下標籤準備填東西進去
passwowrd.clear() #將回傳的內容清空，留下標籤準備填東西進去

username.send_keys('你的IG帳號')
time.sleep(0.25)
passwowrd.send_keys('你的IG密碼')
time.sleep(0.25)
Xpath = '//*[@id="loginForm"]/div/div[3]'
loginbtn = driver.find_element_by_xpath(Xpath)
time.sleep(0.25)
loginbtn.click()


#點煩人的通知
Xpath2 = '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Xpath2)))
skip = driver.find_element_by_xpath(Xpath2)
skip.click()

#點搜尋
Xpath2_1 = '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div'
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Xpath2_1)))
skip = driver.find_element_by_xpath(Xpath2_1)
skip.click()

#尋找標籤
Xpath3 = '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input'
search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Xpath3)))
keyword = '#chihuahua'
search.send_keys(keyword)
time.sleep(1)
#IG 搜尋須按兩次 Enter才能進入，並且需有時間間隔
search.send_keys(Keys.ENTER)
time.sleep(1)
search.send_keys(Keys.ENTER)

time.sleep(5)
#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'x5yr21d xu96u03 x10l6tqk x13vifvy x87ps6o xh8yej3')))
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3')))

# #多生成幾張圖
# for i in range(5):
#     #將網頁滑到底1次
#     driver.execute_script('window.scrollTo(0,document.body.scrollHeight);') #透過這個函式可以執行js程式碼 x,y座標
#     time.sleep(5)

#imgs = driver.find_elements_by_class_name('x5yr21d xu96u03 x10l6tqk x13vifvy x87ps6o xh8yej3')
imgs = driver.find_elements_by_css_selector('.x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3')

PATH = os.path.join(keyword) #資料夾路徑 根據關鍵字命名資料夾
os.mkdir(PATH) #創建資料夾

count = 1
for img in imgs:
    save_as = os.path.join(PATH,keyword+str(count)+'.jpg') #下載到電腦的路徑
    print(img.get_attribute('src'))
    wget.download(img.get_attribute('src'),save_as) #第一個參數是圖片在網上的路徑,第二個是載到電腦的哪裡
    count+=1

print('Application Finish')
driver.quit()
os.startfile(PATH)
