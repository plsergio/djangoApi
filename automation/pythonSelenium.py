from selenium.webdriver import Firefox
# para o Firefox é preciso colocar o arquivo geckodriver em  ~/local/bin/
# https://github.com/mozilla/geckodriver/releases
from selenium.webdriver.firefox.options import Options

import pyautogui

for i in range(10):
    pyautogui.moveTo(100,100,duration=0.25)
    pyautogui.moveTo(200,100,duration=0.25)
    pyautogui.moveTo(200,200,duration=0.25)
    pyautogui.moveTo(100,200,duration=0.25)

opts = Options()
opts.headless = True

#browser = Firefox()
browser = Firefox(options=opts)
browser.get('https://duckduckgo.com')

search_form = browser.find_element_by_id('search_form_input_homepage')
search_form.send_keys('real python')
search_form.submit()

results = browser.find_elements_by_class_name('result__a')
print(results[0].text)

browser.close()
#quit()