from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--start-maximized')
options.add_argument('--disable-notifications')

driver = webdriver.Chrome(options=options)
driver.get("https://the-internet.herokuapp.com/inputs")
input_form = driver.find_element(By.TAG_NAME, "input")
input_form.send_keys("a")
assert input_form.get_attribute("value") == ""

input_form.send_keys("1e2")
assert input_form.get_attribute("value") == "1e2"

input_form.clear()
input_form.send_keys("1.2")
assert input_form.get_attribute("value") == "1.2"

input_form.clear()
input_form.send_keys("5")
assert input_form.get_attribute("value") == "5"

input_form.send_keys(Keys.ARROW_UP)
assert input_form.get_attribute("value") == "6"

input_form.send_keys(Keys.ARROW_DOWN)
assert input_form.get_attribute("value") == "5"

driver.quit()