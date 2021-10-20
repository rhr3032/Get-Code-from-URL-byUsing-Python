import urllib.request

url = input("enter url ")

req_url = urllib.request.urlopen(url)

print(req_url.read())