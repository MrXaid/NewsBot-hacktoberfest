def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.spVoice")
    speak.speak(str)
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

op = urlopen('https://news.google.com/news/rss')
rd = op.read()
op.close()
sp_page = soup(rd, "html.parser")
news_list = sp_page.find_all("item")
for news in news_list:
    a = news.title.text
    b = news.link.text
    c = "You will  be hearing world's top news"
    print(news.title.text)
    print(news.link.text)
    #print(news.pubDate.text)
    print('-' * 60)
    speak(c)
    speak(a)
    speak(b)



