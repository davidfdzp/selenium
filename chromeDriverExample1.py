''' Loosely based on the example code in http://www.obeythetestinggoat.com/how-to-get-selenium-to-wait-for-page-load-after-a-click.html
Import the necessary packages required for execution 
python -m pip install selenium
https://www.geeksforgeeks.org/how-to-install-selenium-in-python/
Install chromedriver for Selenium.
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

opts = ChromeOptions()
# By default, QUIC is enabled
# opts.add_argument("--disable-quic")
opts.add_argument("--auto-open-devtools-for-tabs")
opts.use_chromium = True

''' Chrome web driver interface
'''
driver = webdriver.Chrome(options=opts)

# additional latency (ms)
# driver.set_network_conditions(offline=False, latency=250, download_throughput=500 * 1000, upload_throughput=500 * 1000) # maximal throughput in kbit/s
# Starlink: 40 ms latency, 50 Mbit/s
# https://www.fool.com/investing/2020/10/27/spacex-reveals-pricing-for-beta-testing-its-starli/
# Measured 425 Mbit/s donwload, 395 Mbit/s upload, 1.48 ms ping
# driver.set_network_conditions(offline=False, latency=40, download_throughput=50 * 1000000, upload_throughput=50 * 1000000) # maximal throughput in kbit/s
# Measured 42.34 Mbit/s download, 42.55 Mbit/s upload, 1.47 ms ping (localhost), but 42.7 ms in librespeed.org
driver.set_network_conditions(offline=False, latency=40, download_throughput=50 * 100000, upload_throughput=50 * 100000)
# Measured 0.37 Mbit/s download, 0.43 Mbit/s upload, 1.52 ms ping, 1.38 ms jitter
# driver.set_network_conditions(offline=False, latency=40, download_throughput=50 * 1000, upload_throughput=50 * 1000) # maximal throughput in kbit/s

# driver = webdriver.Chrome()
# https://www.alexa.com/topsites
# https://www.http3check.net/
# https://w3techs.com/technologies/details/ce-http3

# TODO: make a loop and test load times of these 5 sites with HTTP/2 vs. HTTP/3 for different Internet accesses
# hyperlink = "http://www.google.com"
# hyperlink = "http://www.youtube.com"
# hyperlink = "http://www.facebook.com"
# hyperlink = "http://instagram.com"
# hyperlink = "https://www.litespeedtech.com"

# hyperlink = "http://lambdatest.com"
# hyperlink = "https://www.fast.com"
# IPv6
# hyperlink = "http://localhost"
# IPv4
hyperlink = "http://127.0.0.1"
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
# print(driver.get_network_conditions())
print("Back End: %s ms" % backendPerformance_calc)
print("Front End: %s ms" % frontendPerformance_calc)
print("Total: %s ms" % (backendPerformance_calc + frontendPerformance_calc))
print("Load Time: %s ms" % loadPerformance_calc)

# driver.quit()