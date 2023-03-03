from selenium import webdriver
def add:
  f = open("/caramelslices/index.html", "a")
  f.write()
  f.close()
driver = webdriver.Chrome(executable_path="caramelslices/index.html")
driver.implicitly_wait(0.5)
driver.get("https://dbuildr")
#identify element
l= driver.find_element_by_name("q")
l.send_keys("q")
#get_attribute() to get value of input box
print("Value of input box: " + l.get_attribute('value'))
driver.close()
