from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=800x600")
driver = webdriver.Chrome(service=Service('chromedriver/chromedriver.exe'), options=chrome_options)

url = "http://repository.lppm.unila.ac.id/view/divisions/FEB4/2023.html"
driver.get(url)
time.sleep(3)

select = Select(driver.find_element(By.XPATH, '//*[@id="content"]/form/table/tbody/tr[1]/td[1]/select'))
select.select_by_value('JSON')
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="content"]/form/table/tbody/tr[1]/td[1]/input[1]').click()
time.sleep(10)