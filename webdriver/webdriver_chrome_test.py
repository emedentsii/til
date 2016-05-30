from pyvirtualdisplay import Display
from selenium import webdriver

# test
display = Display(visible=0, size=(800, 600))
display.start()

# now Firefox will run in a virtual display. 
# you will not see the browser.
try:
    browser = webdriver.Chrome()
    browser.get('http://www.google.com')
    print(browser.title)
    browser.quit()
except Exception as mess:
    print("Error: {}".format(mess))
display.stop()
