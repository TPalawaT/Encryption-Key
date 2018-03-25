import bs4 as bs 
import urllib.request

sauce = urllib.request.urlopen("https://en.wikipedia.org/wiki/Xiaomi").read()
soup = bs.BeautifulSoup(sauce,'lxml')

d=[soup.get_text()]
print(d)
