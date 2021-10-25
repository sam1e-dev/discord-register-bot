import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
import time
import random
import string
import requests
browser = uc.Chrome()
browser.delete_all_cookies()

countries = open('list.txt').read().splitlines()
rco =random.choice(countries)
print(rco)
os.system('cls')
file = open("switch.bat", "w") 
file.write('@echo off\necho Switching IP...\ncd C:\\Program Files\\NordVPN\n nordvpn -c -g "'+rco+'"') 
file.close() 


os.system('switch.bat')
time.sleep(10)
seq = requests.get('https://api.ipify.org')
os.system('cls')
seqx = print ('Connected to: ',seq.text)
time.sleep(5)

S = 12  # number of characters in the string.  
# call random.choices() string module to find the string in Uppercase + numeric data.  
u4 = ''.join(random.choices(string.ascii_lowercase+string.digits, k = S))     
print(str(u4)) # print the random data  


browser.get('https://discord.com/register') 
os.system('echo @|clip')
ok2 = browser.find_element(By.XPATH, "//*[@id='app-mount']/div[2]/div/div/div/form/div/div/div[1]/div/input").send_keys(u4)
ok3 = browser.find_element(By.XPATH, "//*[@id='app-mount']/div[2]/div/div/div/form/div/div/div[1]/div/input").send_keys(Keys.CONTROL + "v")
ok4 = browser.find_element(By.XPATH, "//*[@id='app-mount']/div[2]/div/div/div/form/div/div/div[1]/div/input").send_keys("gmail.com")

S = 10  # number of characters in the string.  
# call random.choices() string module to find the string in Uppercase + numeric data.  
u2 = ''.join(random.choices(string.ascii_lowercase+string.ascii_uppercase+string.digits, k = S))     
print(str(u2)) # print the random data  

ok5 = browser.find_element(By.XPATH, "//*[@id='app-mount']/div[2]/div/div/div/form/div/div/div[2]/div/input").click()
ok6 = browser.find_element(By.XPATH, "//*[@id='app-mount']/div[2]/div/div/div/form/div/div/div[2]/div/input").send_keys(u2)

S = 16  # number of characters in the string.  
# call random.choices() string module to find the string in Uppercase + numeric data.  
u3 = ''.join(random.choices(string.ascii_lowercase+string.ascii_uppercase+string.digits, k = S))     
print(str(u3)) # print the random data  

ok7 = browser.find_element(By.XPATH, "//*[@id='app-mount']/div[2]/div/div/div/form/div/div/div[3]/div/input").click()
ok8 = browser.find_element(By.XPATH, "//*[@id='app-mount']/div[2]/div/div/div/form/div/div/div[3]/div/input").send_keys(u3, Keys.TAB, "5", Keys.TAB, "duben", Keys.TAB, "1998", Keys.TAB)
time.sleep(2)
try:
    browser.find_element(By.XPATH, "//*[@id='app-mount']/div[2]/div/div/div/form/div/div/div[5]/label/input").click() # Agree to terms and conditions
except:
    print('Cant find button, skipping...')
    pass
ok10 = browser.find_element(By.XPATH, "//*[@id='app-mount']/div[2]/div/div/div/form/div/div/div[6]/button").click()
ok11 = input('Press ENTER once captcha is done')

headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            'Host': 'discord.com',
            'Accept': '*/*',
            'Accept-Language': 'en-US',
            'Content-Type': 'application/json',
            'Referer': 'https://discord.com/register',
            'Origin': 'https://discord.com',
            'DNT': '1',
            'Connection': 'keep-alive',
        }

json = {
            'email': u4+'@gmail.com',
            'password': u3,
        }

esafaf = requests.post('https://discord.com/api/v6/auth/login', headers=headers, json=json)
rab = esafaf.json()


time.sleep(.3)
token = rab['token']
print(token)

os.system('cls')

file = open("accs.txt", "a") 
file.write(u4+'@gmail.com:'+u3+'\n') 
file.close() 

file = open("tokens.txt", "a") 
file.write(token+'\n') 
file.close() 

print('Done!\n'+u4+'@gmail.com:'+u3+':'+token)

os.system('kill.bat')

os.system('pause')