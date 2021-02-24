import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://new.land.naver.com/rooms?ms=37.5366,126.8759,16&a=APT:OPST:ABYG:OBYG:GM:OR:VL:DDDGG:JWJT:SGJT:HOJT&b=B1&e=RETAIL&g=12000&aa=SMALLSPCRENT"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
browser.find_element_by_xpath('//*[@id="region_filter"]/div/a/span[2]').click()

sleep_interval = 0.3

# 서울 지역구 js 생성 전까지 대기
try:
	WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="region_filter"]/div/div/div[2]/ul/li[1]')))
except:
	browser.quit()

gu_list = browser.find_elements_by_class_name('area_item')
gu_len = len(gu_list)
for i in range(1, gu_len + 1):
	browser.find_element_by_xpath('//*[@id="region_filter"]/div/div/div[2]/ul/li['+str(i)+']').click()
	time.sleep(sleep_interval)
	dong_list = browser.find_elements_by_class_name('area_item')
	dong_len = len(dong_list)
	for j in range(1, dong_len + 1):
		browser.find_element_by_xpath('//*[@id="region_filter"]/div/div/div[2]/ul/li['+str(j)+']').click()
		time.sleep(sleep_interval)
		time.sleep(1)
		browser.execute_script("window.scrollTo(0, 1080)")
		time.sleep(1)
		browser.find_element_by_xpath('//*[@id="region_filter"]/div/a/span[3]').click()
		time.sleep(sleep_interval)
	browser.find_element_by_xpath('//*[@id="region_filter"]/div/div/div[1]/div/a[2]').click()
	time.sleep(sleep_interval)

# soup = BeautifulSoup(browser.page_source, "lxml")
# test = soup.find("span", attrs={"area is-selected"}).find_next_sibling()
# print(test)
