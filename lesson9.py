import urllib.request


opener = urllib.request.build_opener()
reponse = opener.open('https://coinmarketcap.com/')

print(reponse.read())

