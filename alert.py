from selenium import webdriver
import math as m
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"

browser.get(link)

# for OK: alert = browser.switch_to.alert
#alert.accept() 

# get text: alert = browser.switch_to.alert
#alert_text = alert.text

# to confirm: confirm = browser.switch_to.alert
#confirm.accept()

#confirm.dismiss() - cancel

#to write text:
#prompt = browser.switch_to.alert
#prompt.send_keys("My answer")
#prompt.accept()

browser.find_element_by_tag_name("button").click()
confirm = browser.switch_to.alert
confirm.accept() 

x = int(browser.find_element_by_id("input_value").text)
answer = str(m.log(abs(12*m.sin(x))))

end = browser.find_element_by_id("answer")
end.send_keys(answer)
browser.find_element_by_tag_name("button").click()