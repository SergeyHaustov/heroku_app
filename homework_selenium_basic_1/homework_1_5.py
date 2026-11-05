from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--start-maximized')
options.add_argument('--disable-notifications')

driver = webdriver.Chrome(options=options)
driver.get("https://the-internet.herokuapp.com/typos")

for n in range(10):
    text = driver.find_element(By.XPATH, "//p[2]")
    assert text.text == "Sometimes you'll see a typo, other times you won't.", f"Попытка {n + 1}"
    driver.refresh()
driver.quit()