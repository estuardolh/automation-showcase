from selenium import webdriver

from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

import sys

username = "estuardolh"

if len(sys.argv) > 1:
    username = sys.argv[1]

serviceObj = Service("/usr/bin/geckodriver")

firefoxOptions = Options()
firefoxOptions.add_argument('--headless')

driver = webdriver.Firefox(service=serviceObj, options=firefoxOptions)
driver.get("https://www.github.com/" + username)

repositoriesLabel = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/main/div[1]/div/div/div[2]/div/nav/a[2]").text

print(repositoriesLabel.split()[1])
driver.close()