from selenium import webdriver

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://oke.io/C1Jd')

elem = driver.find_element_by_id('recaptcha-anchor')
elem.click()