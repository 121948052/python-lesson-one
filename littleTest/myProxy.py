import requests

session = requests.Session()
ip = '58.220.95.30'
port = '10174'
proxies = {'http': 'http://{}:{}'.format(ip, port), 'https': 'https://{}:{}'.format(ip, port)}
session.proxies = proxies
response = session.get('https://www.zhipin.com/c101280600/?query=')
print(response.text)