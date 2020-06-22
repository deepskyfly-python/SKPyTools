from bs4 import BeautifulSoup
import requests

# inputFile = open("test.htm")
requestFile = requests.get('http://www.baidu.com', timeout=10)

soup = BeautifulSoup(requestFile.content,'html.parser')

# print(soup.p)

for pp in soup.find_all('p'):
    print(pp)