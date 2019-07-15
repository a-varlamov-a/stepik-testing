from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math as m
def calc(a):
  return str(m.log(abs(12*m.sin(a))))

opt = webdriver.ChromeOptions()
opt.add_experimental_option('w3c', False)
browser = webdriver.Chrome(chrome_options=opt)
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR")
    )
browser.find_element_by_id("book").click()

x = int(browser.find_element_by_id("input_value").text)
answer = calc(x)
end = browser.find_element_by_id("answer")
end.send_keys(answer)
browser.find_element_by_id("solve").click()