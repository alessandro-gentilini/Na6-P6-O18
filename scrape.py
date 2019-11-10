from bs4 import BeautifulSoup
import sys

soup = BeautifulSoup(open(sys.argv[1]), "html5lib")
lis = soup.html.body.find_all("li",recursive=False)

for li in lis:
    aa = li.find_all('a')
    if len(aa)==1:
        print(li.a['href'].replace('./',sys.argv[2]))


