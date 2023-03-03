from selenium import webdriver
driver = webdriver.Chrome(executable_path="caramelslices/index.html")
driver.implicitly_wait(0.5)
driver.get("https://taio-owner-admin.github.io/dbuildr.github.io")
#identify element
l= driver.find_element_by_name("in")
l.send_keys("in")
x = l.get_attribute('in'))
driver.close()

def add():
  f = open("/caramelslices/index.html", "a")
  f.write(x)
  f.close()
