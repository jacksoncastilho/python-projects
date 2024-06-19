import requests

site = requests.get("http://businesscorp.com.br/")
print(f"site --> {site.status_code}\r\n")

