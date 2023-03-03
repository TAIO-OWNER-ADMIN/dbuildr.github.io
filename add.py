import BeautifulSoup4
soup = BeautifulSoup(html)
inputs=soup.find("input", {"id": "input-id"})
print inputs[0]['value']
f = open("/caramelslices/code.html", "a")
f.write(inputs)
f.close()
