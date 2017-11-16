from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities    
# enable browser logging
d = DesiredCapabilities.CHROME
d['loggingPrefs'] = { 'browser':'ALL' }
driver = webdriver.Chrome(desired_capabilities=d)
# load some site
driver.get('http://foo.com')
# print messages
for entry in driver.get_log('browser'):
    print entry
