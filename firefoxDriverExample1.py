# Python program to demonstrate 
# selenium. Install gecko driver for Selenium. 
# python -m pip install selenium
# https://www.geeksforgeeks.org/how-to-install-selenium-in-python/

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

opts = FirefoxOptions()
opts.add_argument("-devtools")

FFprofile = webdriver.FirefoxProfile()
# FFprofile.set_preference('network.http.http3.enabled', True)
FFprofile.set_preference('network.http.http3.enabled', False)

driver = webdriver.Firefox(options=opts, firefox_profile=FFprofile)
# Not possible in Firefox, only in Chrome
# driver.set_network_conditions(offline=False, latency=250, download_throughput=500 * 1000, upload_throughput=500 * 1000) # maximal throughput in kbit/s

# hyperlink = "https://www.bbc.com" 
# hyperlink = "https://www.google.com"
hyperlink = "https://www.litespeedtech.com"
# hyperlink = "http://localhost" 
driver.get(hyperlink) 

''' Use Navigation Timing  API to calculate the timings that matter the most '''   
     
navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")
loadEventEnd = driver.execute_script("return window.performance.timing.loadEventEnd")

''' Calculate the performance'''
backendPerformance_calc = responseStart - navigationStart
frontendPerformance_calc = domComplete - responseStart
loadPerformance_calc = loadEventEnd - navigationStart
print("Load Time Results for %s" % hyperlink)
print(driver.title)
print("Back End: %s ms" % backendPerformance_calc)
print("Front End: %s ms" % frontendPerformance_calc)
print("Total: %s ms" % (backendPerformance_calc + frontendPerformance_calc))
print("Load Time: %s ms" % loadPerformance_calc)

# driver.quit()