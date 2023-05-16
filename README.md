# 動態爬蟲簡易說明  
在進行爬蟲時，通常都會跟ChromeDriver搭配，模擬Chrome engine進行訊息搜索與相關作業，  
但在使用時，也需要核對下載版本與本機目前的版本是否一致，否則容易延伸後續錯誤發生，  
所以先打開Chrome檢查一下自己現在的版本吧▼  
  
![image](https://github.com/LouisAzhe/selenium-IG/assets/48307578/313cb925-9121-4f31-9000-b7caa68d32e1)
  
如上圖，我的版本是113.0.5672.93，所以在下載的時候需要下載下方的version 113，如下圖▼  
👉 [Chrome Driver 下載傳送門](https://chromedriver.chromium.org/downloads)  
  
![image](https://github.com/LouisAzhe/selenium-IG/assets/48307578/d18c8ccd-ef03-431c-8221-9dd0af166447)  
  
接著需要下載對應作業系統的壓縮檔，並將檔案解壓縮，後續程式是使用windows作業系統，搭配exe檔執行為例。  
  
![image](https://github.com/LouisAzhe/selenium-IG/assets/48307578/6dd36aff-fec0-4a80-989e-026b2a4d871c)  

前置作業完成後，我們來試著用selenium在IG上，爬幾張吉娃娃的圖，下方圖片為爬完後，將圖片下載至本機的結果▼  
  
![image](https://github.com/LouisAzhe/selenium-IG/assets/48307578/0b3ae61c-250c-43fa-b4fb-f6993e25d890)  
  
## ▶ 補充：  
- 下方code測試時間為2023/05/15，若之後有網頁元素有所變更仍需配合網頁進行調整。  
👉 [如何在IG上爬吉娃娃的圖](https://github.com/LouisAzhe/selenium-IG/blob/main/seleniumIG.py)  
  
- Selenium Documentation (可以在裡面查看相關function的使用)  
👉 [Selenium with Python](https://selenium-python.readthedocs.io/index.html)  
  
<p align="right"> Copyright &copy; 2020 - 2023 Azhe all rights reserved </p>
