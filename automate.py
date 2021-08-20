
from selenium import webdriver
import time

#åpner chrome og gitt webadresse
web = webdriver.Chrome('C:\ChromeDrivers\chromedriver.exe')
web.get('https://smartoblat.trondheimparkering.no/accounts/login/?next=/')

#websiden far tid til a laste
time.sleep(2)

#legger inn epost som brukernavnt i korrekt tekstboks
userName = "svaagan@gmail.com"
user = web.find_element_by_xpath('//*[@id="id_username"]')
user.send_keys(userName)

#legger inn passord som brukernavnt i korrekt tekstboks
passWord = "Sildråpevegen66f"
passW = web.find_element_by_xpath('//*[@id="id_password"]')
passW.send_keys(passWord)

#trykker pa "logg inn"
submit = web.find_element_by_xpath('/html/body/div/div[2]/div/form/div[3]/div[1]/button')
submit.click()

#websiden far tid til a laste
time.sleep(1)

#trykker på legg til nytt regnr
leggtil = web.find_element_by_xpath('//*[@id="userPermitAccordion"]/div/div[2]/div[3]/div[1]/button')
leggtil.click()

#websiden far tid til a laste
time.sleep(1)

#skal legge inn selve regnr i tekstboks, men FEILER her. Antagelig pga pop-up
regnr = "VJ21556"
reg = web.find_element_by_xpath('//*[@id="id_regno"]')
passW.send_keys(passWord)

#websiden far tid til a laste
time.sleep(1)

#submitter regnr fra kodesnutt over
leggtilreg = web.find_element_by_xpath('//*[@id="529923addguest"]/div/div/div[2]/form/div/div/div/span/button')
leggtilreg.click()
