from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import sys
# test
display = Display(visible=0, size=(800, 600))
display.start()

# now Firefox will run in a virtual display. 
# you will not see the browser.
try:
	binary = FirefoxBinary("/usr/bin/firefox", log_file=sys.stdout) 
	browser = webdriver.Firefox(firefox_binary=binary)
	browser.get('http://www.google.com')
	print browser.title
	browser.quit()
except Exception, mess:
	print("Error: {}".format(mess) )
display.stop()
