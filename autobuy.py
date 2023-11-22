import time
from selenium import webdriver
import pyfiglet as f
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import webbrowser 


browser = driver = webdriver.Chrome()

# Login ke web JKT48
driver.get('https://jkt48.com/login?lang=id')
email=driver.find_element(By.XPATH,'//*[@id="login_id"]')
password=driver.find_element(By.XPATH,'//*[@id="login_password"]')
login=driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[1]/div/form/button')
action=ActionChains(driver)
action.click(email)
action.send_keys('yourname@gmail.com')
action.click(password)
action.send_keys('ur_password')
action.click(login)
action.perform()

# Link Produk
link_produk ='https://jkt48.com/theater/schedule/id/2622?lang=id'
cookie='AHWqTUkjG0PhlyiUHjl5Hd4fuCOWkMI9ge05qVzWjBm1bY2x507TqJlY4TgjizZi='


def finish():
    style = f.figlet_format("CIEE DAPET")
    time.sleep(1)
    print(style)

def error():
    style = f.figlet_format("SYSTEM ERROR TELAH DI PERBARUI")
    time.sleep(1)
    print(style)

#FUNGSI TOMBOL BELI

def tombol_beli():
    try:
        # TOMBOL BELI OFC
        centang = WebDriverWait(browser, 1200).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div/div[2]/div[1]/table/tbody/tr[2]/td[2]/a')))
        browser.execute_script("arguments[0].click();", centang)

        # Centang Syarat dan Ketentuan
        centang = WebDriverWait(browser, 1200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="agree2"]')))
        browser.execute_script("arguments[0].click();", centang)

        # Klik Pembelian tiket event
        Pembelian = WebDriverWait(browser, 1200).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[2]/form/div[2]/button')))
        browser.execute_script("arguments[0].click();", Pembelian)
        finish()
       
    except NoSuchElementException as e:
        print(e)
        error()


# MENU UTAMA PROGRAM DI EKSEKUSI
def main():
    jam_device = time.strftime("%H:%M:%S", time.localtime())
    time.sleep(1)
    browser.get(link_produk)
    jam = int(input("\033[32m[+] Masukan Jam untuk memulai beli : "))
    menit = int(input("\033[32m[+] Masukan Menit untuk memulai beli : "))
    detik = int(input("\033[32m[+] Masukan Detik untuk memulai beli : "))
    waktu = '{:02d}:{:02d}:{:02d}'.format(jam, menit, detik)

    while jam_device != waktu :
        jam_device_INT = int(time.strftime("%H%M%S", time.localtime()))
        waktu_int='{:02d}{:02d}{:02d}'.format(jam, menit, detik)
        nilai = int(waktu_int)

        if  jam_device_INT <= nilai:
            browser.refresh()
            print("\033[32m[+] INFO:\033[31m", time.strftime("%H:%M:%S", time.localtime()), "\033[93mWAKTU BELUM MULAI.!")
        else:
            break

    tombol_beli()

if __name__ == "__main__":
    main()
