from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
import xlsxwriter
from selenium.common.exceptions import NoSuchElementException
workbook = xlsxwriter.Workbook('clashofclans20.csv')
worksheet = workbook.add_worksheet()


#############
options = webdriver.ChromeOptions()
driver = webdriver.Chrome('chromedriver',options=options)
driver.get("https://cafebazaar.ir/app/com.supercell.clashofclans")

    #####################

time.sleep(7)
a=0
while a < 500:

 try:
    buttons = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH,'//button[@class="btn btn-primary-alt"]')))
    a=a+1
    print(a)
 except TimeoutException:
  break
 else:
    for button in buttons:
        a=a+1
        time.sleep(3)
        button.click()
        print(a)
elems = driver.find_elements_by_xpath('//div[@class="AppComment AppCommentsList__item"]')
i=1
for elem in elems:    
    phone2 = elem.find_element_by_xpath('.//div[@class="AppComment__body break-words"]').text
    #print(phone2)  
    worksheet.write(i, 0, i)
    worksheet.write(i, 1, str(phone2))
    i=i+1                   
workbook.close()



