import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import ICR_1 as ICR
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display



def get_cita(id, cd):
    width=1000
    height=500
    window_width = int(width) if width is not None else 1000
    window_height = int(height) if height is not None else 500
    display = Display(visible=0, size=(1366, 768))
    display.start()
    id = str(id)
    cd = str(cd)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")


    url = "http://barcelona.kdmid.ru/queue/OrderInfo.aspx?id="+ id + "&cd=" + cd
    driver = webdriver.Chrome(options=chrome_options)
    #driver = webdriver.Chrome()
    driver.get(url)

    driver.save_screenshot("screenshot.png")
    time.sleep(5)
    captcha = ICR.get_captcha()

    print(captcha)

    #inputElement = driver.find_element_by_id("ctl00_MainContent_txtCode")
    inputElement = driver.find_element(by=By.ID, value= 'ctl00_MainContent_txtCode')
    inputElement.send_keys(captcha)
    time.sleep(1)

    inputElement = driver.find_element(by=By.ID, value= 'ctl00_MainContent_ButtonA').click()
    time.sleep(1)

    try:
        inputElement = driver.find_element(by=By.ID, value= 'ctl00_MainContent_ButtonB').click()
        print('Eureka!!, Captcha correct')
        time.sleep(1)
        texto = "Извините, но в настоящий момент на интересующее Вас консульское действие в системе предварительной записи нет свободного времени."
        posted = driver.find_element(by=By.ID, value= 'center-panel').text
        #print(posted)
        if texto in posted:
            return True, 'No citas availables'
        else:
            return True, 'ATTENTION!! Citas Available!!!'
    except:
        return False, "Captcha identification has failed, trying again...."

