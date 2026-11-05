import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from conftest import browser


@pytest.mark.basic
def test_add_remove(browser):
    browser.get("https://the-internet.herokuapp.com/add_remove_elements/")

    add_element = browser.find_element(By.XPATH, "//button[text()='Add Element']")
    add_element.click()
    add_element.click()
    delete = browser.find_element(By.XPATH, "//button[text()='Delete']")
    delete_elements = browser.find_elements(By.XPATH, "//button[text()='Delete']")

    assert len(delete_elements) == 2

    delete.click()
    delete_elements = browser.find_elements(By.XPATH, "//button[text()='Delete']")

    assert len(delete_elements) == 1


@pytest.mark.basic
def test_checkboxes(browser):
    browser.get("https://the-internet.herokuapp.com/checkboxes")
    checkbox_1 = browser.find_element(By.XPATH, "//input[1]")
    checkbox_2 = browser.find_element(By.XPATH, "//input[2]")

    assert checkbox_1.is_selected() == False
    assert checkbox_2.is_selected() == True

    checkbox_1.click()
    checkbox_2.click()

    assert checkbox_1.is_selected() == True
    assert checkbox_2.is_selected() == False


@pytest.mark.basic
def test_dropdown(browser):
    browser.get("https://the-internet.herokuapp.com/dropdown")
    dropdown = browser.find_element(By.ID, "dropdown")
    select = Select(dropdown)
    option_text = [option.text for option in select.options]
    assert option_text[0] == "Please select an option"
    assert option_text[1] == "Option 1"
    assert option_text[2] == "Option 2"

    select.select_by_index(1)
    assert select.first_selected_option.text == "Option 1"

    select.select_by_index(2)
    assert select.first_selected_option.text == "Option 2"


@pytest.mark.basic
class TestInputs:
    @pytest.mark.parametrize("symbol", ["a", "b", "г"])
    def test_alphabet(self, browser, symbol):
        browser.get("https://the-internet.herokuapp.com/inputs")
        input_form = browser.find_element(By.TAG_NAME, "input")
        input_form.send_keys(symbol)
        assert input_form.get_attribute("value") == ""

    @pytest.mark.parametrize("number", [1.2, 5.55, -10.005, 1e2])
    def test_float(self, browser, number):
        browser.get("https://the-internet.herokuapp.com/inputs")
        input_form = browser.find_element(By.TAG_NAME, "input")
        input_form.send_keys(number)
        assert input_form.get_attribute("value") == str(number)

    def test_arrows(self, browser):
        browser.get("https://the-internet.herokuapp.com/inputs")
        input_form = browser.find_element(By.TAG_NAME, "input")
        input_form.send_keys("5")
        assert input_form.get_attribute("value") == "5"

        input_form.send_keys(Keys.ARROW_UP)
        assert input_form.get_attribute("value") == "6"

        input_form.send_keys(Keys.ARROW_DOWN)
        assert input_form.get_attribute("value") == "5"


@pytest.mark.basic
@pytest.mark.xfail
def test_typos(browser):
    browser.get("https://the-internet.herokuapp.com/typos")

    for n in range(10):
        text = browser.find_element(By.XPATH, "//p[2]")
        assert text.text == "Sometimes you'll see a typo, other times you won't.", f"Попытка {n + 1}"
        browser.refresh()
