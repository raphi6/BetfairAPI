import requests, json, urllib

username=raphi6
password=To400actuc
appKey=Yye7sReexernACoc

payload = 'username=' + username + '&password' + password
headers = {'X-Application': appKey, 'Content-Type' = 'application/x-www-form-urlencoded'}
resp = requests.post('https://identitysso-cert.betfair.com/api/certlogin', data=payload, cert=())
