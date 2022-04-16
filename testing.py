from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://automationpractice.com/index.php")
#print(driver.title)

login = driver.find_element(By.CLASS_NAME, 'login')
login.click()
time.sleep(5)

#1st account Create
email = driver.find_element(By.NAME, 'email_create')
email.send_keys('nuzhatzahan199@gmail.com')
submit = driver.find_element(By.ID, 'SubmitCreate')
submit.click()
#print("hello")
time.sleep(5)

#Personal Information
gender1 = driver.find_element(By.ID, 'uniform-id_gender2')
gender1.click()
time.sleep(2)

cfname = driver.find_element(By.ID, 'customer_firstname')
cfname.send_keys('Nuzhat')
time.sleep(2)
clname = driver.find_element(By.ID, 'customer_lastname')
clname.send_keys('Zahan')
time.sleep(2)
mail=driver.find_element(By.ID, 'email')
mail.clear( )
mail.send_keys('nuzhatzahan199@gmail.com')
time.sleep(2)
passwd=driver.find_element(By.ID, 'passwd')
passwd.send_keys('nuzhatzahan199')
time.sleep(2)

selectday = Select(driver.find_element(By.ID, 'days'))
selectday.select_by_value('9')
time.sleep(2)

selectmonth = Select(driver.find_element(By.ID, 'months'))
selectmonth.select_by_value('7')
time.sleep(2)
selectyear = Select(driver.find_element(By.ID, 'years'))
selectyear.select_by_value('1997')
time.sleep(2)

newsletter=driver.find_element(By.ID, 'uniform-newsletter')
newsletter.click()
time.sleep(2)
spoffers=driver.find_element(By.ID, 'uniform-optin')
spoffers.click()
time.sleep(2)

#address information
fname = driver.find_element(By.ID, 'firstname')
fname.send_keys('Nuzhat')
time.sleep(2)
lname = driver.find_element(By.ID, 'lastname')
lname.send_keys('Zahan')
time.sleep(2)

company = driver.find_element(By.ID, 'company')
company.send_keys('abcde')
time.sleep(2)
address1 = driver.find_element(By.ID, 'address1')
address1.send_keys('a,ffd,fsdfd')
time.sleep(2)
address2 = driver.find_element(By.ID, 'address2')
address2.send_keys('a,ffd,fsdfd')
time.sleep(2)

city= driver.find_element(By.ID, 'city')
city.send_keys('dffg')
time.sleep(2)

selectstate = Select(driver.find_element(By.ID, 'id_state'))
selectstate.select_by_value('1')
time.sleep(2)

postcode= driver.find_element(By.ID, 'postcode')
postcode.send_keys('11111')
time.sleep(2)

selectcountry = Select(driver.find_element(By.ID, 'id_country'))
selectcountry.select_by_value('21')
time.sleep(2)

other= driver.find_element(By.ID, 'other')
other.send_keys('+880 1992230697')
time.sleep(2)
phone= driver.find_element(By.ID, 'phone')
phone.send_keys('+880 1992230697')
time.sleep(2)
mobile= driver.find_element(By.ID, 'phone_mobile')
mobile.send_keys('+880 1992230697')
time.sleep(2)
alias= driver.find_element(By.ID, 'alias')
alias.send_keys('mnmnmn')
time.sleep(2)

submitAccount= driver.find_element(By.ID, 'submitAccount')
submitAccount.click()
time.sleep(12)

back = driver.find_element(By.CLASS_NAME, 'btn btn-default button button-small')
back.click()
time.sleep(20)