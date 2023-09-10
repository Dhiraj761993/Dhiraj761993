#Test Case
#1)Loging using id and password
#2)Print home page title
#3)Search for Mens T Shirt
#4)Verify title
#5)Back to home page, back or forward
#5)Close

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver=webdriver.Chrome(options=options)

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

#driver.get("https://www.amazon.in/")
driver.get("https://www.amazon.in/?&ext_vrnc=hi&tag=googinhydr1-21&ref=pd_sl_4b3e4wrxds_b&adgrpid=60639568242&hvpone=&hvptwo=&hvadid=617721280315&hvpos=&hvnetw=g&hvrand=3103703337280673567&hvqmt=b&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007788&hvtargid=kwd-311187680635&hydadcr=5841_2362028")

driver.maximize_window()

act_title1=driver.title
print(act_title1)#Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in

# driver.find_element(By.ID,"nav-link-accountList-nav-line-1").click()
# driver.find_element(By.NAME,"email").send_keys("dpgaikwad88@gmail.com")
# driver.find_element(By.ID,"continue").click()
# driver.find_element(By.ID,"ap_password").send_keys("123456")
# driver.find_element(By.ID,"signInSubmit").click()

driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Mens T Shirt")
driver.find_element(By.ID,"nav-search-submit-button").click()

act_title2=driver.title
print(act_title2)
exp_title="Amazon.in : Mens T Shirt" #Amazon.in : mens T shirt
if act_title2==exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

driver.back()
driver.forward()

#driver.close()

