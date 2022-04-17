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
time.sleep(2)

#####1st account Create######

#email = driver.find_element(By.NAME, 'email_create')
#email.send_keys('nuzhatzahan199@gmail.com')
#submit = driver.find_element(By.ID, 'SubmitCreate')
#submit.click()
#print("hello")
#time.sleep(5)

#Personal Information
#gender1 = driver.find_element(By.ID, 'uniform-id_gender2')
#gender1.click()
#time.sleep(2)

#cfname = driver.find_element(By.ID, 'customer_firstname')
#cfname.send_keys('Nuzhat')
#time.sleep(2)
#clname = driver.find_element(By.ID, 'customer_lastname')
#clname.send_keys('Zahan')
#time.sleep(2)
#mail=driver.find_element(By.ID, 'email')
#mail.clear()
#mail.send_keys('nuzhatzahan199@gmail.com')
#time.sleep(2)
#passwd=driver.find_element(By.ID, 'passwd')
#passwd.send_keys('nuzhatzahan199')
#time.sleep(2)

#selectday = Select(driver.find_element(By.ID, 'days'))
#selectday.select_by_value('9')
#time.sleep(2)

#selectmonth = Select(driver.find_element(By.ID, 'months'))
#selectmonth.select_by_value('7')
#time.sleep(2)
#selectyear = Select(driver.find_element(By.ID, 'years'))
#selectyear.select_by_value('1997')
#time.sleep(2)

#newsletter=driver.find_element(By.ID, 'uniform-newsletter')
#newsletter.click()
#time.sleep(2)
#spoffers=driver.find_element(By.ID, 'uniform-optin')
#spoffers.click()
#time.sleep(2)

#address information
#fname = driver.find_element(By.ID, 'firstname')
#fname.send_keys('Nuzhat')
#time.sleep(2)
#lname = driver.find_element(By.ID, 'lastname')
#lname.send_keys('Zahan')
#time.sleep(2)

#company = driver.find_element(By.ID, 'company')
#company.send_keys('abcde')
#time.sleep(2)
#address1 = driver.find_element(By.ID, 'address1')
#address1.send_keys('a,ffd,fsdfd')
#time.sleep(2)
#address2 = driver.find_element(By.ID, 'address2')
#address2.send_keys('a,ffd,fsdfd')
#time.sleep(2)

#city= driver.find_element(By.ID, 'city')
#city.send_keys('dffg')
#time.sleep(2)

#selectstate = Select(driver.find_element(By.ID, 'id_state'))
#selectstate.select_by_value('1')
#time.sleep(2)

#postcode= driver.find_element(By.ID, 'postcode')
#postcode.send_keys('11111')
#time.sleep(2)

#selectcountry = Select(driver.find_element(By.ID, 'id_country'))
#selectcountry.select_by_value('21')
#time.sleep(2)

#other= driver.find_element(By.ID, 'other')
#other.send_keys('+880 1992230697')
#time.sleep(2)
#phone= driver.find_element(By.ID, 'phone')
#phone.send_keys('+880 1992230697')
#time.sleep(2)
#mobile= driver.find_element(By.ID, 'phone_mobile')
#mobile.send_keys('+880 1992230697')
#time.sleep(2)
#alias= driver.find_element(By.ID, 'alias')
#alias.send_keys('mnmnmn')
#time.sleep(2)

#submitAccount= driver.find_element(By.ID, 'submitAccount')
#submitAccount.click()
#time.sleep(12)



####2nd Account Creation#######

#email_2 = driver.find_element(By.NAME, 'email_create')
#email_2.send_keys('nzahan171199@bscse.uiu.ac.bd')
#submit_2 = driver.find_element(By.ID, 'SubmitCreate')
#submit_2.click()
#time.sleep(5)

#Personal Information
#gender_2 = driver.find_element(By.ID, 'uniform-id_gender1')
#gender_2.click()
#cfname_2 = driver.find_element(By.ID, 'customer_firstname')
#cfname_2.sendkeys('Nihad')
#time.sleep(2)
#clname_2 = driver.find_element(By.ID, 'customer_lastname')
#clname_2.send_keys('Zahan')
#time.sleep(2)

#mail_2=driver.find_element(By.ID, 'email')
#mail_2.clear()
#mail_2.send_keys('nzahan171199@bscse.uiu.ac.bd')
#passwd_2=driver.find_element(By.ID, 'passwd')
#passwd_2.send_keys('nzahan199')
#time.sleep(2)


#selectday_2 = Select(driver.find_element(By.ID, 'days'))
#selectday_2.select_by_value('19')
#time.sleep(2)
#selectmonth_2 = Select(driver.find_element(By.ID, 'months'))
#selectmonth_2.select_by_value('10')
#time.sleep(2)
#selectyear_2 = Select(driver.find_element(By.ID, 'years'))
#selectyear_2.select_by_value('1995')
#time.sleep(2)


#newsletter_2=driver.find_element(By.ID, 'uniform-newsletter')
#newsletter_2.click()
#time.sleep(2)
#spoffers_2=driver.find_element(By.ID, 'uniform-optin')
#spoffers_2.click()
#time.sleep(2)

#address information

#fname_2 = driver.find_element(By.ID, 'firstname')
#fname_2.send_keys('Nihad')
#time.sleep(2)
#lname_2 = driver.find_element(By.ID, 'lastname')
#lname_2.send_keys('Zahan')
#time.sleep(2)

#company_2 = driver.find_element(By.ID, 'company')
#company_2.send_keys('abcde')
#address1_2 = driver.find_element(By.ID, 'address1')
#address1_2.send_keys('a,ffd,fsdfd')
#time.sleep(2)
#address2_2 = driver.find_element(By.ID, 'address2')
#address2_2.send_keys('a,ffd,fsdfd')
#time.sleep(2)

#city_2= driver.find_element(By.ID, 'city')
#city_2.send_keys('dffg')
#time.sleep(2)

#selectstate_2 = Select(driver.find_element(By.ID, 'id_state'))
#selectstate_2.select_by_value('1')
#time.sleep(2)

#postcode_2= driver.find_element(By.ID, 'postcode')
#postcode_2.send_keys('11111')
#time.sleep(2)

#selectcountry_2 = Select(driver.find_element(By.ID, 'id_country'))
#selectcountry_2.select_by_value('21')
#time.sleep(2)

#other_2= driver.find_element(By.ID, 'other')
#other_2.send_keys('+880 1992230697')
#time.sleep(2)

#phone_2= driver.find_element(By.ID, 'phone')
#phone_2.send_keys('+880 1992230697')
#time.sleep(2)
#mobile_2= driver.find_element(By.ID, 'phone_mobile')
#mobile_2.send_keys('+880 1992230697')
#time.sleep(2)
#alias_2= driver.find_element(By.ID, 'alias')
#alias_2.send_keys('mnmnmn')
#time.sleep(2)

#submitAccount_2= driver.find_element(By.ID, 'submitAccount')
#submitAccount_2.click()
#time.sleep(12)

#back = driver.find_element(By.CLASS_NAME, 'btn btn-default button button-small')
#back.click()
#time.sleep(20)


#####login an account#####

loginemail = driver.find_element(By.NAME, 'email')
loginemail.send_keys('nuzhatzahan199@gmail.com')
time.sleep(1)
loginpasswd = driver.find_element(By.NAME, 'passwd')
loginpasswd.send_keys('nuzhatzahan199')
time.sleep(1)
submitlogin = driver.find_element(By.ID, 'SubmitLogin')
submitlogin.click()

time.sleep(2)

#####Casual Dresses Section ####

women = driver.find_element(By.CLASS_NAME, 'sf-with-ul')
women.click()
dress = driver.find_element(By.LINK_TEXT, 'Dresses')
dress.click()
cdress = driver.find_element(By.LINK_TEXT, 'Casual Dresses')
cdress.click()
time.sleep(2)

cart = driver.find_element(By.LINK_TEXT, 'Add to cart')
cart.click()
time.sleep(2)
shopping = driver.find_element(By.CSS_SELECTOR, ("[title=\"Continue shopping\"]"))
shopping.click()
time.sleep(2)


##### Tshirt Section #####
#tshirts= driver.find_element(By.CSS_SELECTOR, ("[title=\"T-shirts\"]"))
#tshirts.click()
#tshirts = driver.find_element(By.LINK_TEXT, 'T-shirts')
#tshirts.click()
#time.sleep(1)
#bluefilter =  driver.find_element(By.ID, 'layered_id_attribute_group_14')
#bluefilter.click()
#time.sleep(2)
#cart_shirt = driver.find_element(By.LINK_TEXT, 'Add to cart')
#cart_shirt.click()
#time.sleep(2)


##### Check out Section ####

ccart = driver.find_element(By.CSS_SELECTOR, ("[title=\"View my shopping cart\"]"))
ccart.click()
time.sleep(1)

checkout = driver.find_element(By.LINK_TEXT, 'Proceed to checkout')
checkout.click()
time.sleep(2)

ncheckout = driver.find_element(By.NAME, 'processAddress')
ncheckout.click()
time.sleep(5)

terms = driver.find_element(By.NAME, 'cgv')
terms.click()

order = driver.find_element(By.NAME, 'processCarrier')
order.click()

payment = driver.find_element(By.CSS_SELECTOR, ("[title=\"Pay by check.\"]"))
payment.click()
time.sleep(1)

confirm = driver.find_element(By.XPATH, '//button[normalize-space()="I confirm my order"]')
confirm.click()
time.sleep(5)