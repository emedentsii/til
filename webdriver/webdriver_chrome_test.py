from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# test
display = Display(visible=0, size=(800, 600))
display.start()

# now Chrome will run in a virtual display. 
# you will not see the browser.
try:
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get('http://www.google.com')
    print(browser.title)
    browser.quit()
except Exception as mess:
    print("Error: {}".format(mess))
display.stop()
