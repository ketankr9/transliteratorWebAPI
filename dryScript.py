import dryscrape
import sys
import time
TIME_OUT=1000
if 'linux' in sys.platform:
    # start xvfb in case no X is running. Make sure xvfb
    # is installed, otherwise this won't work!
    dryscrape.start_xvfb()

# sentence that need to be transliterated
search_term = 'utsav'

# set up a web scraping session
sess = dryscrape.Session(base_url = 'http://tdil-dc.in')

# we don't need images
sess.set_attribute('auto_load_images', False)

# visit following link and fill form data
sess.visit('/san/transliteration/index_dit.html')

#the dropdown menu From's option 2 is selected
src=sess.at_xpath('//*[@id="srclang"]/option[2]')
src.select_option()
# print src.text()

#the Target dropdown menu's option 5 is selected here
tar=sess.at_xpath('//*[@id="targetlang"]/option[5]')
tar.select_option()
# print tar.text()

#fill the first input box
source=sess.at_xpath('//*[@id="source"]')
source.set(search_term)

#click on the transliterate buttion
btn =  sess.at_xpath('//*[@id="transbtn"]')
btn.click()

#get output after certain wait
time.sleep(0.1)
output = sess.at_xpath('//*[@id="target"]')

#looping TIME_OUT times untill web page is loaded
count=0
while output.text()=="" and count < TIME_OUT:
    time.sleep(0.1)
    count+=1
    output = sess.at_xpath('//*[@id="target"]')

#printing output box's content
print output.text()

# save a screenshot of the web page
sess.render('output.png')
print("Screenshot written to 'output.png' in current folder")
