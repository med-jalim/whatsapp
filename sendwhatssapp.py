
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time
import psutil
import random

for process in psutil.process_iter(attrs=['pid', 'name']):
    if process.info['name'] in ('chrome.exe', 'chromedriver.exe'):
        process.terminate() 

def setup_driver():
    user_data_dir = r"C:\Users\moham\AppData\Local\Google\Chrome\User Data"
    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir={user_data_dir}") 
    # options.add_argument("--profile-directory=Default") 

    #options.add_argument("--headless=new")           #ila briti Tb9a tchof ach kytra 7Ydi had line
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--mute-audio")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36"
    )
    driver = uc.Chrome(options=options)
    return driver




def send_key(driver, xpath, key):
    try:
        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.send_keys(key)
        element.send_keys(Keys.ENTER)
    except Exception as e:
        print(f"Error in send_key: {e}")



def click_element_with_xpath(driver, xpath):
    try:
        element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
        actions = ActionChains(driver)
        actions.move_to_element(element)
        time.sleep(random.uniform(2, 5))
        actions.click().perform()
        time.sleep(random.uniform(2, 5))
    except Exception as e:
        print(f"Error in click_element_with_mouse: {e}")





def send(driver,contact_name,message,times):
    try:
        
        if contact_name!='_':
            send_key(driver,'//*[@id="side"]/div[1]/div/div[2]/div/div/div[1]/p',contact_name)
            time.sleep(2)
        
        

        for i in range(1,times+1):
           send_key(driver,"//div[@contenteditable='true' and @data-tab='10']",f'{message} {i}')
           

    except Exception as e:
            print(f"Error in main loop: {e}")
    finally:
        print("finision hh")




def main():
    try:
        contact=input('entrer contact: ')
        message=input('entrer message: ')
        nombre=int(input('entrer nombre: '))
        driver=setup_driver()
        driver.get("https://web.whatsapp.com")
        send(driver,contact,message,nombre)                

    except Exception as e :
        print(f"error in main loop: {e}")
    finally:
        time.sleep(20)
        driver.quit()





main()


   
