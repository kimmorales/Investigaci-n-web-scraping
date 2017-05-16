import bs4 as bs
import urllib.request
#import pandas as pd

sauce = urllib.request.urlopen('http://crautos.com/rautosnuevos/').read()
soup = bs.BeautifulSoup(sauce,'lxml')

for table in soup.find_all(class_='cardetail'):
    print(table.text.strip())
    

for table in soup.find_all(class_='small'):
    print(table.get(''))
    print(table.text)

for url in soup.find_all('a'):
    print(url.get('href'))






    
