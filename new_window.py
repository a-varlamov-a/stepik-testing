from selenium import webdriver
import math as m
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
def calc(a):
  return str(m.log(abs(12*m.sin(a))))

browser.get(link)

#go to new window: browser.switch_to.window(window_name)
#new_window = browser.window_handles[1]
#first_window = browser.window_handles[0]

browser.find_element_by_tag_name("button").click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
x = int(browser.find_element_by_id("input_value").text)
answer = calc(x)
end = browser.find_element_by_id("answer")
end.send_keys(answer)
browser.find_element_by_tag_name("button").click()
alert = browser.switch_to.alert
alert_text = alert.text.split()
alert.accept()
answer = alert_text[-1]

print(answer)