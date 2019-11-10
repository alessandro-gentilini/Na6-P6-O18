from bs4 import BeautifulSoup
import sys
import os

soup = BeautifulSoup(open(sys.argv[1]), "html5lib")
lis = soup.html.body.find_all("li",recursive=False)

i=0
for li in lis:
    if i % 100==0:
        aa = li.find_all('a')
        if len(aa)==1:
            path = li.a['href']
            filename, ext = os.path.splitext(path)
            folder_name = filename.replace('./','')
            code_path = path.replace('./',sys.argv[2])
            desc = li.text 
            #print(code_path,ext,folder_name)
            #print(desc)
            print('mkdir',folder_name)
            print('cd',folder_name)
            print('wget',code_path)
            if ext=='.zip':
                print('unzip',path)
            elif ext=='.gz':
                print('gunzip',path)
            print('rm',path)
    i=i+1


