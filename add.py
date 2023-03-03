from selenium import webdriver
def add:
  f = open("/caramelslices/index.html", "a")
  f.write()
  f.close()
driver = webdriver.Chrome(executable_path="caramelslices/index.html")
driver.implicitly_wait(0.5)
driver.get("https://dbuildrau.github.io/")
#identify element
l= driver.find_element_by_name("in")
l.send_keys("in")
#get_attribute() to get value of input box
print("Value of input box: " + l.get_attribute('in'))
driver.close()
