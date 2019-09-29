# 需要安装 Anaconda

import requests

r= requests.get('http://www.baidu.com/')
print(r.status_code)

print(r.text)

print(r.content)

r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})

print(r.url)

# 直接解析json
#r1 = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
#print(r1.json())


r2 = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print(r2.text)