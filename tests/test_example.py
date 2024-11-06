import pytest
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def open_browser(browser):
    browser.get("https://www.google.com/")
    yield
    browser.refresh()
    
def test_example_ya(browser, open_browser):
    assert "Google" in browser.title
    btn = browser.find_element(By.CSS_SELECTOR, 'button#W0wltc') #тут находится кнопка в pop-up type=button, ID=W0wltc
    btn.click()
    browser.find_element(By.XPATH, '(//input[contains(@aria-label, "Мне повезёт")])[2]').click()
    assert browser.current_url == "https://doodles.google/"
    #time.sleep(10)

    
    
if __name__=="__main__":
    pytest.main()
